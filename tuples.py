t= (1,2,3,4)
print(t[0])
# t[2] = 33 will not work
t1 =() #empty tuple
t2 = (100,) #tuple with single element, t2 = (1000) is wrong way

#methods in tuples
t3 = (1,2,3,1,1,5,4,3,5,2,1,4,0,4,3,1)
print(t3.count(1))
print(sum(t3))
print(t3.index(1)) #1 is at index '0'

