# Pytest Automation Setup

## Initial Setup

### Steps:
1. Open **File** → **Settings** → **Project letskoteit** → **Open** → **Project Interpreter**
2. Click on the **+** sign and install the following dependencies:
    - `selenium`
    - `pytest`
    - `pytest-html` (for report generation)
    - `pyxl`

### Always Run as Administrator
To ensure smooth execution, always run scripts with administrative privileges.

## Check pip3 version
```sh
pip3 --version
```
## Update pip 
```sh
python.exe -m pip install --upgrade pip
```

## Installation

### Install specific version and show selenium version
```sh
pip3 install selenium==4.29
```
```sh
pip3 show selenium
```
### Install the latest version of Selenium with Python
```sh
pip install -U selenium
```

To install Pytest, use one of the following methods:
### Using pip:
```sh
pip3 install pytest
```

### Using Project Interpreter (in an IDE like PyCharm):
1. Navigate to `File` > `Settings` > `Project` > `Project Interpreter`
2. Click on `+`
3. Search for `pytest` and install it

## Running Tests

### Running all tests from the terminal:
```sh
py.test
```

### Running tests with full details:
```sh
py.test -v -s
```

### Running a specific file or class:
```sh
py.test -s test_01_setup_and_yield_no_class.py
```

### Running a single method:
```sh
pytest -v -s test_01_setup_and_yield_no_class.py::test_methodB
```

## Pytest Naming Conventions

Pytest follows strict naming conventions. If these conventions are not followed, pytest will not recognize and execute the tests.

### Naming Rules:
- **File Names:** Should start or end with `test`, e.g., `example_test.py or test_example.py`
- **Class Names:** Should start or end with `Test`, e.g., `TestDemo1 or Demo1Test`
- **Test Method Names:** Should start with `test_`, e.g., `def test_example():`

For more details, refer to the official documentation: [Pytest Naming Conventions](http://pytest.readthedocs.io/en/reorganize-docs/new-docs/user/naming_conventions.html)


## Batch File Tips
- Use comments in batch files with:
  - `REM`
  - `::`
- Add `pause` at the end to keep the console open.
- Use **Tab** for auto-completion in CMD.

### Install WebDriver Manager
```sh
pip install webdriver_manager
```

### Check Installed Plugins
```sh
pip list
```

## Running Tests with pytest

### Basic Commands:
```sh
pytest -v -s testsCase/test_zTemp.py --browser chrome
```
> Note: `pytest` and `py.test` are the same.

### Running Tests:
Navigate to the test directory:
```sh
cd C:\Users\Bijaya Chhetri\workspace_python\letskodeit\testsCase
```
Run a single test:
```sh
pytest -v -s test_login.py
```
Run on a specific browser:
```sh
pytest -v -s test_login.py --browser chrome
pytest -v -s test_login.py --browser firefox
```
Run tests in parallel (max 3 processes):
```sh
pytest -v -s -n=3 test_login.py --browser chrome
```
Open terminal in the package directory and run all tests:
```sh
pytest
```
Run with detailed output:
```sh
pytest -v -s
```
Run an individual test case:
```sh
pytest -s test_case_demo1.py
```

## Generating Reports

### Generate an HTML Report:
```sh
pytest -v -s --html=../Reports/report.html test_login.py --browser chrome
```
### Run and Generate a Regression Test Report:
```sh
pytest -v -s -m "regression" --html=../Reports/reportRegression.html --browser chrome
```
### Run and Generate a Smoke Test Report:
```sh
pytest -v -s -m "smoke" --html=../Reports/reportSmoke.html --browser chrome
```
### Run Both Smoke and Regression Tests:
```sh
pytest -v -s -m "smoke or regression" --html=../Reports/reportRegnSmoke.html --browser chrome
```

## Additional pytest-selenium Features

### Using Fixtures:
`pytest-selenium` provides a built-in driver fixture for managing WebDriver instances.
```python
def test_example(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
```

### Specifying Browser via CLI:
```sh
pytest --driver Chrome
pytest --driver Firefox
```

### Capturing Screenshots on Failure:
```sh
pytest --capture=sys --html=report.html
```

### Running Tests with Headless Mode:
```sh
pytest --driver Chrome --capability headless true
```

## Useful Links

- **GitHub Project :** https://github.com/pavanoltraining/nopCommerceProject
- **Demo Application:** http://admin-demo.nopcommerce.com
- **User Email:** `admin@yourstore.com`
- **Password**: `admin`

This document provides a structured approach to setting up and executing pytest automation scripts, incorporating best practices and efficient test execution strategies.
