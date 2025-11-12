# 🧪 Pytest Automation Setup

## 🚀 Overview
This project is a **Selenium Python Test Automation Framework** designed for scalable, maintainable, and efficient test automation. It leverages **Pytest** for test execution, **Page Object Model (POM)** for structure, and **Allure Reports** for visual reporting.

---

## 🛠️ Technologies & Libraries
- **Selenium** – Browser automation  
- **Pytest** – Test execution and management  
- **Page Object Model (POM)** – Maintainable test structure  
- **Allure Report** – Test reporting  

---

## 📁 Project Structure
```sh
selenium-python-framework/
├── tests/
│   ├── test_login.py  
├── pages/
│   ├── login_page.py  
├── config/
│   ├── config.yaml  # Configuration (URL, credentials, etc.)
├── utils/
│   ├── browser_setup.py  # WebDriver initialization  
├── reports/
├── requirements.txt
├── pytest.ini
├── README.md
```

---

## ⚡ Initial Setup

### Installing Dependencies
1. Open **File → Settings → Project → Project Interpreter**  
2. Click **+** and install:
   - `selenium`
   - `pytest`
   - `pytest-html` (report generation)
   - `pyxl`

> 💡 Always run scripts as **Administrator** for smooth execution.

### Verify & Upgrade pip
```sh
pip3 --version
python.exe -m pip install --upgrade pip
```

### Install Selenium
```sh
pip3 install selenium==4.27.1
pip3 show selenium
```
Or install the latest version:
```sh
pip install -U selenium
```

### Install Pytest
```sh
pip3 install pytest
```
Or via IDE Project Interpreter.

---

## 🏃‍♂️ Running Tests

### Basic Commands
```sh
pytest -v -s                  # Verbose output
pytest -s test_login.py        # Run specific test file
pytest -v -s test_login.py::test_methodB  # Run specific method
```

### Running Tests on Specific Browsers
```sh
pytest -v -s test_login.py --browser chrome
pytest -v -s test_login.py --browser firefox
```

### Parallel Execution
```sh
pytest -v -s -n=3 test_login.py --browser chrome
```

---

## 📑 Pytest Naming Conventions
- **File Names:** `test_*.py` or `*_test.py`  
- **Class Names:** `Test*` or `*Test`  
- **Method Names:** `test_*()`  

[Official Pytest Naming Guide](http://pytest.readthedocs.io/en/reorganize-docs/new-docs/user/naming_conventions.html)

---

## 🖥️ Generating Reports

### HTML Report
```sh
pytest -v -s --html=../Reports/report.html test_login.py --browser chrome
```

### Regression / Smoke Reports
```sh
pytest -v -s -m "regression" --html=../Reports/reportRegression.html --browser chrome
pytest -v -s -m "smoke" --html=../Reports/reportSmoke.html --browser chrome
pytest -v -s -m "smoke or regression" --html=../Reports/reportRegnSmoke.html --browser chrome
```

---

## 🔧 Additional Features

### Using Fixtures
```python
def test_example(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
```

### Headless Mode
```sh
pytest --driver Chrome --capability headless true
```

### Screenshots on Failure
```sh
pytest --capture=sys --html=report.html
```

---

## 📌 Useful Links
- **GitHub Project:** [nopCommerceProject](https://github.com/pavanoltraining/nopCommerceProject)  
- **Demo Application:** [Admin Demo](http://admin-demo.nopcommerce.com)  
- **Credentials:**  
  - Email: `admin@yourstore.com`  
  - Password: `admin`

---

This README provides a structured guide for **setting up, executing, and reporting pytest automation scripts**, with best practices for maintainable and scalable testing.

