"""
Lecture 23
Examples to show how the string formatting works in python
"""
city = "nyc"
event = "show"
greet = "thanks"

print("welcome to " + city + " and enjoy the " + event)
print("welcome to %s" % city)
print("welcome to %s and enjoy the %s" % (city, event))

print("welcome to %s and enjoy the %s and %s you " % (city, event, greet))
a = "great stuff"
print(len(a))
"""
Result:-
welcome to nyc and enjoy the show
welcome to nyc
welcome to nyc and enjoy the show
welcome to nyc and enjoy the show and thanks you 
11
"""
