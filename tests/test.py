import sys
from io import StringIO
import os
import threading
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import read_map, test_compass

def run_test(input_file, expected_output_file):
    input_file_path = os.path.join(os.path.dirname(__file__), 'inputs', input_file)
    expected_output_file_path = os.path.join(os.path.dirname(__file__), 'expected_outputs', expected_output_file)

    with open(input_file_path, 'r') as f:
        input_data = f.read().strip()
    with open(expected_output_file_path, 'r') as f:
        expected_output = f.read().strip()

    sys.stdin = StringIO(input_data)
    captured_output = StringIO()
    sys.stdout = captured_output

    def target():
        try:
            if input_data.startswith("test_compass"):
                # Extract parameters for test_compass from the input data
                params_str = input_data[input_data.find("(")+1:input_data.find(")")]
                params = [int(param.strip()) for param in params_str.split(",")]
                test_compass(*params)
            else:
                sys.argv = ["main.py", "0"]  # Provide the necessary command-line argument
                read_map()
        except Exception as e:
            print(f"{Fore.RED}Test {input_file} failed: {e}")

    thread = threading.Thread(target=target)
    thread.start()
    thread.join(timeout=5)  # Timeout after 5 seconds

    if thread.is_alive():
        print(f"{Fore.RED}Test {input_file} failed: Timeout")
        thread.join()  # Ensure the thread is cleaned up
        return False, "Timeout"

    output = captured_output.getvalue().strip()
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__

    # For test_compass, we don't compare the output due to randomness
    if input_data.startswith("test_compass"):
        if "failed" in output.lower():
            print(f"{Fore.RED}Test {input_file} failed: {output}")
            return False, output
        else:
            print(f"{Fore.GREEN}Test {input_file} passed")
            return True, None

    # For other tests, compare the output with the expected output
    if output == expected_output:
        print(f"{Fore.GREEN}Test {input_file} passed")
        return True, None
    else:
        print(f"{Fore.RED}Test {input_file} failed: Expected: {expected_output}, but got: {output}")
        return False, output

# Base directory for tests
base_dir = os.path.abspath(os.path.dirname(__file__))

# Directories for inputs and expected outputs
inputs_dir = os.path.join(base_dir, "inputs")
expected_outputs_dir = os.path.join(base_dir, "expected_outputs")

# Get all test input files
input_files = sorted(os.listdir(inputs_dir))
expected_output_files = sorted(os.listdir(expected_outputs_dir))

# Ensure the number of input files matches the number of expected output files
assert len(input_files) == len(expected_output_files), "Mismatch between number of input and expected output files"

# Run all test cases
total_tests = len(input_files)
passed_tests = 0
failed_tests = []

for input_file, expected_output_file in zip(input_files, expected_output_files):
    input_file_path = os.path.join(inputs_dir, input_file)
    expected_output_file_path = os.path.join(expected_outputs_dir, expected_output_file)
    print(f"Running test with input file: {input_file_path} and expected output file: {expected_output_file_path}")
    passed, output = run_test(input_file_path, expected_output_file_path)
    if passed:
        passed_tests += 1
    else:
        failed_tests.append((input_file, output, expected_output_file_path))

# Print summary
print(f"\n{Fore.GREEN if passed_tests == total_tests else Fore.RED}Summary: {passed_tests} out of {total_tests} tests passed.")

if failed_tests:
    print(f"\n{Fore.RED}Failed Tests:")
    for input_file, output, expected_output_file in failed_tests:
        expected_output_file_path = os.path.join(expected_outputs_dir, expected_output_file)
        with open(expected_output_file_path, 'r') as f:
            expected_output = f.read().strip()
        print(f"\nTest {input_file} failed:")
        print(f"Expected: {expected_output}")
        print(f"Got: {output}")
        print(f"Input data for {input_file}:")
        input_file_path = os.path.join(inputs_dir, input_file)
        with open(input_file_path, 'r') as f:
            input_data = f.read().strip()
        print(f"{input_data}")