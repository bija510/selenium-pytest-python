import unittest
from basicselenium.unittestpackage.test_02_class_and_methodlevel_setup_teardown import TestCaseDemo2
from basicselenium.unittestpackage.test_03_same_as_02 import TestClass2
from basicselenium.unittestpackage.test_04_asserts import SimpleTest

# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)
tc3 = unittest.TestLoader().loadTestsFromTestCase(SimpleTest)


# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

#To Run from  terminal type this ==> python UnitTestPackage/Z_test_suite_demo.py
#python UnitTestPackage/Z_test_suite_demo.py --html=../Reports/report22.html --browser chrome