import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools_mod.debug_test import run_tests

if __name__ == "__main__":
    test_files = ["tests/agent_verify_prompt.py", "tests/test_tool_execution_flow.py"]
    all_passed = True

    for test_file in test_files:
        print(f"Running verification on {test_file}...")
        results = run_tests(test_file)
        for key, value in results.items():
            print(f"--- {key.upper()} ---")
            print(value)
            print("-" * (len(key) + 8))

            # Simple check if tests failed
            if key == "tests" and ("FAIL" in value or "ERROR" in value):
                all_passed = False

    if not all_passed:
        sys.exit(1)
