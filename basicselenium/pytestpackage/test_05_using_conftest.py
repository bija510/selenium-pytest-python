import pytest

"""
to run all --------------> py.test -v -s
to run only one class ---> py.test -v -s test_03_setup_and_teardown.py
to run only one method --> py.test -v -s test_05_using_conftest.py::test_methodA
                      ---> py.test -v -s test_05_using_conftest.py --browser firefox
"""
def test_methodA(oneTimeSetUp, setUp):
    print("Running method A")

def test_methodB(oneTimeSetUp, setUp):
    print("Running method B")