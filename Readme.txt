initial setUp
1.File-->Setting-->Project letskoteit-->open -->project interpertior-->click + sign -->
a)selenium
b)pytest
c)pytest-html for Report
d)pyxl
+
Always run as Admin
1. To use Comment in bat File we can use {" REM ", " :: "} infront of the command
2. At he end we can write pause also
3. Also in CMD we can write little+ tab --> give auto completion

***************************************************************************
Note: we can write:- pytest -v -s testsCase/test_zTemp.py --browser chrome
***************************************************************************
pytest = py.test samehing
***************************************************************************

https://github.com/pavanoltraining/nopCommerceProject
http://admin-demo.nopcommerce.com
useremail=admin@yourstore.com
password=admin
1. C:\Users\Bijaya Chhetri\workspace_python\letskodeit\testsCase>
2. py.test -v -s test_login.py
3. py.test -v -s test_login.py --browser chrome
4. py.test -v -s test_login.py --browser firefox
5. Run parallel max -3 ===>How many method we have just pass num
6. py.test -v -s -n=2 test_login.py --browser chrome
7. To run Anything we have to Run from CMD or terminal ==r-click package -->
8. Open in terminal --> py.test
9. To run full with details--> py.test -v -s
10. To run individual --> py.test -s test_case_demo1.py
11. py.test -v -s --html=../Reports/report.html test_login.py --browser chrome
12. py.test -v -s -m "regression" --html=../Reports/reportRegression.html --browser chrome
13. py.test -v -s -m "smoke" --html=../Reports/reportSmoke.html --browser chrome
14. py.test -v -s -m "smoke or regression" --html=../Reports/reportRegnSmoke.html --browser chrome


