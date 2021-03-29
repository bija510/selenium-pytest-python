from selenium import webdriver
from pages.DDTjsonPage import DDTjsonPage
import pytest
from utilites.custom_logger import logGen
import configparser
import os

class Testdemoauto:  #Class name should start from >>--> Test

	def test_register(self):


		config = configparser.RawConfigParser()
		config.read(os.getcwd() + "\\configuration\\config.ini")

		print("===>"+os.getcwd() + "\\configuration\\config.ini")
		print("===>"+"..\\configuration\\config.ini")
		#pytest -v -s test_zTemp.py --browser chrome