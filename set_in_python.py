a={1,3,4,2,4,5}
print(type(a))
print(a)

#this syntax will create an empty dictionary not empty set
b={}
print(type(b))

#empty set can be created by:
b = set()
print(type(b))

#adding vlaues
b.add(34)
b.add(22)
b.add(35)
b.add(45)
b.add(41)
b.add(40)
b.add(38)
b.add('100')
# b.add(22)
#we can not add list or dictionary in set
#we cannot change the values in set
#b.add({3:4})
#b.add([4:7])

print(len(b))

b.remove(34)

print(b.pop()) #removes the arbitrary elements from the set
print('union',b.union({38, 10, 60,42,34 ,88}))
print('intersaction',b.intersection({38, 10, 60,42,34 ,88}))
# print('clear',b.clear())
print(b)