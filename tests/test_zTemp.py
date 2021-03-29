from selenium import webdriver
from pages.DDTjsonPage import DDTjsonPage
import pytest
from utilites.custom_logger import logGen

class Testdemoauto:  #Class name should start from >>--> Test
	global aa
	aa="apple"

	def test_register(self, setup):
		aa= "ball"
		print(aa)


	def test_register1(self, setup):
		aa="Cat"
		print(aa)

		#pytest -v -s test_zTemp.py --browser chrome