import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add repo root to path
sys.path.append(os.getcwd())

import tools_mod
from tools_mod import execute_tool, _TOOL_REGISTRY

class TestToolExecutionFlow(unittest.TestCase):
    def setUp(self):
        # Backup original registry
        self.original_registry = _TOOL_REGISTRY.copy()

    def tearDown(self):
        # Restore registry
        _TOOL_REGISTRY.clear()
        _TOOL_REGISTRY.update(self.original_registry)

    def test_execute_tool_dispatch(self):
        # Create a mock tool function
        mock_tool = MagicMock(return_value="mock_result")

        # Register it
        _TOOL_REGISTRY["mock_tool"] = mock_tool

        # Execute it
        result = execute_tool("mock_tool", {"arg1": "value1"})

        # Verify
        self.assertEqual(result, "mock_result")
        mock_tool.assert_called_once_with(arg1="value1")

    def test_legacy_fallback(self):
        # Ensure we can still hit legacy paths if not in registry
        # We can mock execute_memory_tool
        with patch('tools_mod.execute_memory_tool', return_value="memory_result") as mock_mem:
            # We need to ensure the tool name is in MEMORY_TOOL_NAMES
            tools_mod.MEMORY_TOOL_NAMES.add("mock_memory_tool")

            result = execute_tool("mock_memory_tool", {})
            self.assertEqual(result, "memory_result")
            mock_mem.assert_called_once()

            # Clean up
            tools_mod.MEMORY_TOOL_NAMES.remove("mock_memory_tool")

    def test_modern_modules_coverage(self):
        # Verify that all tools from modern_modules are in the registry
        for module in tools_mod.modern_modules:
            if hasattr(module, 'library'):
                for name, func in module.library.items():
                    self.assertIn(name, _TOOL_REGISTRY)
                    self.assertEqual(_TOOL_REGISTRY[name], func)

if __name__ == "__main__":
    unittest.main()
