# intellin-automated-tests-dashboard

Tests written in Python, checking UI side of CCG [dashboard.](https://dashboardtest.intellin.com/)

## Things needed before running tests

1. PyCharm Community Edition, can be downloaded from [here](https://www.jetbrains.com/pycharm/download/#section=windows)

2. [Python 3.7.x](https://www.python.org/downloads/)

3. Install required packages using:

```bash
pip install -r requirements.txt
```

Environment variables set to:

```bash
BASE_URL = https://dashboardtest.intellin.com/login/
CCG_PASS = ccg clinician password
CCG_USER = ccg clinician email
INVALID_PASS = ccg clinician invalid password 
```

## Running tests
After launching PyCharm with the project
```bash
cd Tests
```
To run all tests inside the directory, run this command:
```bash
pytest
or python -m pytest
```

To run a test module, do the following:
```bash
pytest <module name>
i.e. pytest test_loginPage.py
```
To run a specific test, do the following:
```bash
pytest <module name> <class name> <test name>
i.e. pytest test_Login.py::LoginTests::test_valid_login
```

## Reports

.html reports will be automatically generated and stored in Tests/__reports directory