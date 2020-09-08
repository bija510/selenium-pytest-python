import json
from selenium import webdriver
import time

#read file
myjsonfile =open('../testData/inputData.json', 'r')
jsondata = myjsonfile.read()

#parse
obj = json.loads(jsondata)

# from the json-String
firstName = (str(obj['firstName']))
lastName = (str(obj['gender']))
gender = (str(obj['lastName']))

# From the json-object
city = str(obj['address'].get("city"))
postalCode = str(obj['address'].get("postalCode"))
state = str(obj['address'].get("state"))

#For the json-Array
list = obj['phoneNumbers']
phoneNumber1 = list[0].get("number")
type1 = list[0].get("type")

phoneNumber2 = list[1].get("number")
type2 = list[1].get("type")


class DatadriverJson:
	def jsonData(self):
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.get('http://demo.automationtesting.in/Register.html')
		driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys(firstName)
		driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys(lastName)
		driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[2]/div/textarea").send_keys(city+' '+state+' '+postalCode)
		driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[4]/div/input").send_keys(type2+phoneNumber1)

		time.sleep(4)

cc =DatadriverJson()
cc.jsonData()
