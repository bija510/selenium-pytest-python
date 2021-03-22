"""
File I/O
'w' -> Write-Only Mode
'r' -> Read-only Mode
'r+' -> Read And Write Mode
'a' -> Append Mode
"""
#Work with .txt file, .properties

from pathlib import Path


path = Path(__file__).parent / "../H Working with File/firstFile.txt"
my_list = ["camel", "ball", "cat"]
my_file = open(path, "w")

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()