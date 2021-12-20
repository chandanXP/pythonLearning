for i in range(1,10):
     print(i)

for i in range(1,10, 2): #({start}, {range}, {step size})
     print(i)

for i in range(1,10):
     print(i)
     if(i==5):
          break
else:
     print("this is inside for loop's else condition. you can use it in while loop as well")