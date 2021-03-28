import unittest
"""
------------------------------------------------------------------------------------------------------------------
to Execute from CMD
------------------------------------------------------------------------------------------------------------------
To run 1 python file 
1. cd project path and ==> python -m unittest unittestpackage\test_01_methodlevel_setup_teardown.py
2. another way===========> python unittestpackage\test_01_methodlevel_setup_teardown.py
------------------------------------------------------------------------------------------------------------------
3. To run 1 Method=======> python unittestpackage\test_01_methodlevel_setup_teardown.py TestCaseDemo1.test_methodA
4. click on green trangle left to Class or method to Run 
   [NOTE:- Test in class name & test_ should be present in the Mehtod otherwise no Run btn comes up]
------------------------------------------------------------------------------------------------------------------
"""

class TestCaseDemo1(unittest.TestCase):

    def setUp(self):
        print("I will run once before every testdemo")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("I will run after every testdemo")


if __name__ == '__main__':
    unittest.main(verbosity=2)
