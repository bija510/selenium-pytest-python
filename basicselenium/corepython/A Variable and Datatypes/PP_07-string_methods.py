"""Examples to show available string methods in python"""
# Accessing characters in a string
# index starts from zero

first = "nyc"[0]
city = "sfo"
print(first) #Result:- n
ft = city[0]
print(ft) # Result:-s

"""
len()
lower()
upper()
str()
"""

stri = "This Is a Mixed Case"
print(stri.lower())
print(stri.upper())
print(len(stri))  #Result len=Length = 20

print(stri + str(2)) #This Is a Mixed Case2

"""
Concatenation
"""
print("Hello " + " " + " World !!!")
print(first + " " + city)