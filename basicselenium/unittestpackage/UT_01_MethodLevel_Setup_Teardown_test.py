import unittest
"""
to Execute from CMD
cd project path and ==> python -m unittest UnitTestPackage\test_case_demo1.py
148. Writing First Test Case
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
