"""
File I/O
Reading a file -> .read()
Reading line by line -> .readline()
"""
# instead of hard coding we have to do this
#from pathlib import Path
#path = Path(__file__).parent / "../H Working with File/firstFile.txt"

from pathlib import Path

path = Path(__file__).parent / "../H Working with File/firstFile.txt"
my_file = open(path, 'r')

print(str(my_file.read()))
my_file.close()

print("Line by line ========>>")

my_file_line = open(path, 'r')
print(str(my_file_line.readline()))
print(str(my_file_line.readline()))
print(str(my_file_line.readline()))

my_file_line.close()