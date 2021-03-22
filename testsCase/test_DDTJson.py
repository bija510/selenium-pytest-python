import json
from pagesObjects.DDTjsonPage import DDTjsonPage

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

class Testdemoauto:

	def test_register(self, setup):
		self.driver = setup
		self.dd = DDTjsonPage(self.driver)
		self.dd.openUrl("http://demo.automationtesting.in/Register.html")
		self.dd.enterFirstName(firstName)
		self.dd.enterLastName(lastName)
		self.dd.enterAddress(city+' '+state+' '+postalCode)
		self.dd.enterPhoneNumbers(type2 + phoneNumber1)
