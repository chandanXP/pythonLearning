val = 10
x = "There are %d types of people." %val
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s"%(binary,do_not)

print(x)
print(y)

# we can pass everything in '%r', and will be printed as it is 
print("I said : %r."%x) 
print("I also said: '%s'."%y)  

hilarious = False
# res = False
joke_evaluation = "Isn't that joke so funny?! %r"
# print(joke_evaluation)

# we can use string formating in disjoint way
print(joke_evaluation % hilarious)

w = "This is the left side of... "
e = "a string with a right side."

# adding two string 
print(w + e)
