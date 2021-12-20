from typing import Concatenate


name = "Chandan" #indexed: 0,1,2,3,4,.....
greeting ="Good morning "

# Concatenation
print(type(name))
print(greeting +name)

print(name[0]) 
# name[2] = 's' -->does not work

#slicing a string
print(name[1:5])
print(name[:3])# same as name[0:3]
print(name[2:])# same as name[2:6]

#negative indexing
print(name[-4: -1])#this is same as name[1:4], -1 is last element
print(name[-1])

#skipping
print(name[0:6:2])#skipp after one word

# print(len(name))
# print(name.endswith("z"))
# print(name.count('a'))
# print(name.capitalize())
# print(name.find("and")) #first ouccurence
# print(name.replace("and", ">.<"))