
pytest tests\test_01_login.py
REM py.test -v -s tests\test_01_login.py --browser edge
REM py.test -v -s tests\test_01_login.py --browser firefox
REM py.test -v -s tests\test_01_login.py --browser edge
REM py.test -v -s tests\test_01_login.py

REM py.test -v -s -n=2 tests\test_01_login.py --browser edge

REM py.test -v -s --html=./Reports/report1.html tests\test_01_login.py --browser edge

REM py.test -v -s -m "regression" --html=./Reports/reportRegression.html tests --browser edge
REM py.test -v -s -m "smoke" --html=./Reports/reportSmoke.html tests --browser edge
REM py.test -v -s -m "smoke or regression" --html=./Reports/reportRegnSmoke.html tests --browser edge

pause