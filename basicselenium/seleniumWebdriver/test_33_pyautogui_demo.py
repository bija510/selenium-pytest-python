import pyautogui

##########################################################################################
# https://pyautogui.readthedocs.io/en/latest/
# To Run:- first run & then ==> shift + f10
# just place the mouse then it will give the location number in ===>
# Need to open the chrome & just move the mouse to the search & run to get the x & y-axis
##########################################################################################

def test_demo():

	print(pyautogui.position())
	pyautogui.click(189, 64)
	pyautogui.typewrite("apple")
	# pyautogui.hotkey("ctrl", "a")
	# pyautogui.hotkey("ctrl", "c")
	pyautogui.hotkey("control", "space") # double keyboard function

	pyautogui.typewrite("device")
	pyautogui.typewrite(["enter"])