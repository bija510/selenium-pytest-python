import configparser
import os

config = configparser.RawConfigParser()
config.read(os.getcwd()+"/configuration/config.ini")
#config.read("../configuration/config.ini")
class ReadConfig:
	@staticmethod
	def getApplicationURL():
		url = config.get('Environment variable', 'baseUrl')
		print("===>"+url)
		return url

	@staticmethod
	def getUserName():
		username = config.get('Environment variable', 'userName')
		return username


	@staticmethod
	def getPassword():
		password = config.get('Environment variable', 'password')
		return password
