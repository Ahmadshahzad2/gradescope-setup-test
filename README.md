
# Gradescope Setup and Testing for `mid` Function

This repository contains a Gradescope-compatible testing setup for the `mid` function, which returns the middle character of an input string. If the string length is even, the function returns an empty string.

## Project Structure

The repository includes the following files and directories:

- **`ex1.py`**: Contains the `mid` function implementation.
- **`tests/`**: Directory containing various test files to validate different aspects of the `mid` function's behavior in Gradescope.

## Test Files Overview

The following test files cover a wide range of scenarios:

1. **`test_complex.py`**: Tests complex cases for the `mid` function, including handling of longer strings and edge cases with parentheses and precedence.

2. **`test_files.py`**: Checks for the presence of required files (like `ex1.py`) to ensure that the submission is complete.

3. **`test_integration.py`**: Performs integration tests simulating user interaction with the `mid` function in a command-line environment.

4. **`test_leaderboard.py`**: Tracks metrics like accuracy, allowing for leaderboard scoring in Gradescope.

5. **`test_partial.py`**: Uses partial credit grading to reward students for handling individual cases correctly, even if some conditions fail.

6. **`test_simple.py`**: Basic unit tests to confirm correct functionality for standard cases and simple inputs.

7. **`test_unknown.py`**: Ensures that the function handles unexpected or large inputs gracefully.

## Setup Instructions

To run tests locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Ahmadshahzad2/gradescope-setup-test.git
   cd gradescope-setup-test
   ```

2. Run tests with `unittest`:
   ```bash
   python -m unittest discover -s tests
   ```

3. For Gradescope setup, ensure all required files (`ex1.py`, `tests/`) are included in your submission.

## Usage of `mid` Function

The `mid` function is designed to return the middle character of a string `s`:

```python
from ex1 import mid
print(mid("hello"))  # Output: "l"
print(mid("abcd"))   # Output: ""
```


