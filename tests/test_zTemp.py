
import os
import logging

class Testdemoauto:  #Class name should start from >>--> Test

	def test_register(self):
		logging.basicConfig(filename='C://Users//Bijaya Chhetri//workspace_python//selenium-pytest-python//logs//Test1.log', level=logging.DEBUG)
		logger = logging.getLogger()
		logger.setLevel(logging.INFO)
		logger.warning("just warning")
		logger.info("just info")
		logger.error("Just error")

		#pytest -v -s tests\test_zTemp.py
