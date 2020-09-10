cd testsCase


py.test -v -s test_loginDDT.py --browser chrome
REM py.test -v -s test_login.py --browser chrome
REM py.test -v -s test_login.py --browser firefox
REM py.test -v -s test_login.py --browser edge
REM py.test -v -s test_login.py

REM py.test -v -s -n=2 test_login.py --browser chrome

REM py.test -v -s --html=../Reports/report.html test_login.py --browser chrome

REM py.test -v -s -m "regression" --html=../Reports/reportRegression.html --browser chrome
REM py.test -v -s -m "smoke" --html=../Reports/reportSmoke.html --browser chrome
REM py.test -v -s -m "smoke or regression" --html=../Reports/reportRegnSmoke.html --browser chrome

pause