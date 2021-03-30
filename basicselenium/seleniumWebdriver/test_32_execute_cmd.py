import os


class TestExecuteFromCmd():



	def test_execute_and_remain(self):
		#(1) CMD /K – execute a command and then remain:
		#os.system('cmd /k "Your Command Prompt Command"')
		path = "cd "+ os.getcwd() + "\\basicselenium\\seleniumWebdriver"
		print("==>"+path)
		os.system('cmd /k '+ path)

		os.system('cmd /k "pytest \\basicselenium\\seleniumWebdriver test_21_mouse_event.py"')

"""
	def test_execute_and_terminate(self):
		#(2) CMD /C – execute a command and then terminate:
		#os.system('cmd /c "Your Command Prompt Command"')

		os.system('cmd /c "color a & date"')"""