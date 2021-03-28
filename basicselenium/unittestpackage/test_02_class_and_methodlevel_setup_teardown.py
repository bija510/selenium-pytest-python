import unittest

"""
to Execute from CMD
cd project path and ==> python -m unittest UnitTestPackage\test_case_demo1.py
"""
class TestCaseDemo2(unittest.TestCase):

    @classmethod # called Decorator in Python & Annoatation in java
    def setUpClass(cls):
        print("==" * 30)
        print("I will run only once before all tests")
        print("==" * 30)

    def setUp(self):
        print("I will run once before every testdemo")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("I will run after every testdemo")

    @classmethod
    def tearDownClass(cls):
        print("==" * 30)
        print("I will run only once after all tests")
        print("==" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)