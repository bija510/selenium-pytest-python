import unittest
from basicselenium.seleniumWebdriver.test_01_chrome_firefox_edge import TestLocalDriver
from basicselenium.seleniumWebdriver.test_02_headless_chrome_firefox_edge import TestRemoteDriver
from basicselenium.seleniumWebdriver.test_03_open_close_browser import TestOpenCloseBrowser

# Get all sel_demo_package from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLocalDriver)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestRemoteDriver)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestOpenCloseBrowser)


# Create a test suite combining TestClass1 and TestClass2
regressionTest = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(regressionTest)
