"""
Execute statement repeatedly
Conditions are used to stop the execution of loops
Iteration items are Strings, list, Tuple, Dictionary
"""
# String for loop and Looping through the letter in the word Banana
for x in "Banana":
    print(x)

my_string = 'abcabc'

for c in my_string:
    if c == 'a':
        print('A', end='')
    else:
        print(c, end='')
print()

# list for loop
cars = ['bmw', 'benz', 'honda']
for car in cars:
    print(car)

nums = [1, 2, 3]
for n in nums:
    print(n * 10)
print("*" * 20)

# Dictionary for loop
d = {'one': 1, 'two': 2, 'three': 3}
for k in d:
    print(k + "" + str(d[k]))
print("*" * 20)

for k, v in d.items():
    print(k)
    print(v)
