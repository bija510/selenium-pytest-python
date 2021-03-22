import unittest
from UnitTestPackage.UT_02_ClassAndMethodLevel_Setup_Teardown_test import TestCaseDemo2
from UnitTestPackage.UT_03_sameAs_UT_02 import TestClass2
from UnitTestPackage.UT_04_Asserts_test import SimpleTest

# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)
tc3 = unittest.TestLoader().loadTestsFromTestCase(SimpleTest)


# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

#to Run from  terminal type this ==> python UnitTestPackage/Z_test_suite_demo.py
