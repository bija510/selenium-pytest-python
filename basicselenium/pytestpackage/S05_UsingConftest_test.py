import pytest

"""
to run all --------------> py.test -v -s
to run only one class ---> py.test -v -s S03_SetUpAndTearDown_test.py
to run only one method --> py.test -v -s S05_UsingConftest_test.py::test_methodA
                      ---> py.test -v -s S05_UsingConftest_test.py --browser firefox
"""
def test_methodA(oneTimeSetUp, setUp):
    print("Running method A")

def test_methodB(oneTimeSetUp, setUp):
    print("Running method B")