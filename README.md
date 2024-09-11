# CS144-SUTest-Cases

Unofficial-test cases for the first hand in are  designed to validate the functionality of the read_map and test_compass functions.
These test cases ensure that the program correctly reads input, constructs the simulation map, and uses the compass class tosimulateentity movement.

# Disclaimer

These test cases are provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the test cases or the use or other dealings in the test cases. Use them at your own risk.

# Project Reguirements

1. pip install su-stdlibs-python --upgrade
2. pip install su-cs144-projectlibs


# Project Structure

project_root/
├── src/
│   ├── __pycache__/
│   ├── bee.py
│   ├── flower.py
│   ├── main.py
│   ├── map.py
│   ├── README.md
├── tests/
│   ├── expected_outputs/
│   │   ├── expected_output_1.txt
│   │   ├── expected_output_2.txt
│   │   ├── expected_output_3.txt
│   │   ├── expected_output_4.txt
│   │   ├── expected_output_5.txt
│   │   ├── expected_output_6.txt
│   │   ├── expected_output_7.txt
│   ├── inputs/
│   │   ├── test_input_1.txt
│   │   ├── test_input_2.txt
│   │   ├── test_input_3.txt
│   │   ├── test_input_4.txt
│   │   ├── test_input_5.txt
│   │   ├── test_input_6.txt
│   │   ├── test_input_7.txt
│   ├── test.py

# Update.gitignore Update

To ensurethat these test cases are notpushed to your repository, add the following lines to your gitignore file

- tests/inputs/
- tests/expected_outputs/

# Cloning the test cases

run: git clone git@github.com:pontshomagane/CS144-SUTest-Cases.git

## Running the Tests

1. **Ensure Dependencies are Installed**:
   Make sure you have all the necessary dependencies installed. You can use `pip` to install any required packages.

2. **Navigate to the Project Root**:
   Open a terminal and navigate to the root directory of your project.

3. **Run the Tests**:
   Execute the `test.py` script to run the test cases. This script will read the input files from the project_root/tests/inputs and compare with the output in
   project_root/tests/expected_outputs

   ```sh
   python tests/test.py