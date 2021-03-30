"""
Logging Demo 1
Logging Levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
import logging

def test_logFile():
	logging.basicConfig(filename='selenium-pytest-python/loggingpackage/Test1.log',level=logging.DEBUG)
	logging.warning("warning message")
	logging.info("info message")
	logging.error("error message")
