import logging
import os


class logGen:
	@staticmethod
	def loggen():
		print("===>"+os.getcwd()+"/logs/autom.log")
		logging.basicConfig(filename=os.getcwd()+"/logs/autom.conf" ,
		                  format= '%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p' )
		logger = logging.getLogger()
		logger.setLevel(logging.INFO)
		return logger
