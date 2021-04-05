import os
import subprocess

class TestExecuteFromCmd():


#  https://datatofish.com/command-prompt-python/
	def test_open_cmd_1st_way(self):
		# This will open the command line
		os.system("start cmd")
		os.system('cmd /k ' + 'java -version')

	def test_open_cmd_2nd_way(self):
		subprocess.call('start', shell=True)



