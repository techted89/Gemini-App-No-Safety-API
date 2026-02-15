from . import core, web, file_ops, memory, database, learning, display, git, nlp, debug_test, tool_creator, knowledge, system
from .memory import execute_memory_tool
from .database import execute_database_tool
from .display import display_image_task
from .learning import learn_repo_task, learn_directory_task, learn_url_task
from utils.file_system import save_to_file
import traceback

# Modern Modules Configuration
modern_modules = [
    core, web, file_ops, git, nlp, debug_test, tool_creator, knowledge, system, learning, display
]

# Build Registry for O(1) Lookup
_TOOL_REGISTRY = {}
for module in modern_modules:
    if hasattr(module, 'library'):
        _TOOL_REGISTRY.update(module.library)

# Legacy Module Caches
MEMORY_TOOL_NAMES = {t['name'] for t in memory.tool_definitions() if isinstance(t, dict) and 'name' in t}
DATABASE_TOOL_NAMES = {t['name'] for t in database.tool_definitions() if isinstance(t, dict) and 'name' in t}

def get_all_tool_definitions():
    """
    Returns a flat list of all tool definitions (Tools or Dicts).
    """
    all_tools = []

    # Modern Modules (Return List[genai.types.Tool])
    for module in modern_modules:
        all_tools.extend(module.tool_definitions())

    # Legacy Modules (Return List[Dict] or List[Tool])
    all_tools.extend(memory.tool_definitions())
    all_tools.extend(database.tool_definitions())
    # Display was previously legacy/manual, now modern

    return all_tools

def tool_definitions():
    # Dynamically call get_all_tool_definitions each time
    # to support runtime updates (e.g., via tool_creator)
    return get_all_tool_definitions()

def execute_tool(name, args):
    """
    Executes a tool by name with the given arguments.
    Catches exceptions and returns detailed tracebacks.
    """
    try:
        # 1. Modern Library Lookup (O(1))
        if name in _TOOL_REGISTRY:
            return _TOOL_REGISTRY[name](**args)

        # 2. Legacy / Special Cases

        # Memory Tools
        if name in MEMORY_TOOL_NAMES:
            return execute_memory_tool(name, args)

        # Database Tools
        if name in DATABASE_TOOL_NAMES:
            return execute_database_tool(name, args)

        # Backward Compatibility
        if name == "save_to_file":
            return save_to_file(args.get('filename'), args.get('content'))

        return f"Tool {name} not found."

    except Exception as e:
        return f"Error executing tool '{name}': {e}\nTraceback:\n{traceback.format_exc()}"
