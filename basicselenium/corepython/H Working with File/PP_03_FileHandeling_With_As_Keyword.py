"""
With / As Keywords
"""
# print("Normal Write Start")
# my_write = open("textfile.txt", "w")
# my_write.write("Trying to write to the file")
# my_write.close()
#
# print("Normal Read Start")
# my_read = open("textfile.txt", "r")
# print(str(my_read.read()))

from pathlib import Path
path = Path(__file__).parent / "../H Working with File/withas.txt"

with open(path, "w") as with_as_write:
    with_as_write.write("example of with as write/read")

with open(path, "r") as with_as_read:
    print(str(with_as_read.read()))