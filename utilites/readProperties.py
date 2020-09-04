import configparser

config = configparser.RawConfigParser()
config.read("../Configuration/config.ini")

class ReadConfig:
	@staticmethod
	def getApplicationURL():
		url = config.get('Environment variable', 'baseURL')
		return url

	@staticmethod
	def getUserName():
		username = config.get('Environment variable', 'userName')
		return username


	@staticmethod
	def getPassword():
		password = config.get('Environment variable', 'password')
		return password
