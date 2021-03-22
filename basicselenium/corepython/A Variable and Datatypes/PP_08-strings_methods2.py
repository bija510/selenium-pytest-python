"""
Examples to show available string methods in python
"""
# Replace Method
a = "1abc2abc3abc4abc"
print(a.replace('abc', 'ABC'))

# we Cannot not change String are immutable
# Sub-Strings
# starting index is inclusive

sub = a[1:6] #Result:- abc2a
step = a[1:6:2] #Result:-aca

print("****************")

print(sub)
print(step)

b = "Apple"
