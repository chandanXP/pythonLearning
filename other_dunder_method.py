class Number:
     def __init__(self,num) :
          self.num = num
     def __add__(self, obj):
          print("let's add")
          return self.num + obj.num #operational overloading
     def __mul__(self , obj):
          return self.num * obj.num  #operational overloading
     def __sub__(self , obj):
          print("applying customized operation on '-'")
          return self.num * obj.num * 10 #operational overloading
     def __str__(self):
          return f"Decimal Number: {self.num}"  #return object as string
     def __len__(self):
          return 1 #return length of an object

n1 = Number(4)
n2 = Number(6)
n = Number(10)
 
sum = n1 + n2  #n1(self) + n2(obj2)
mul =  n1 * n2
# sub = n1 - n2
sub =  n2 -n1 #__sub__ will be called

print(sum)
print(mul)
print(sub)
print(n)
print(len(n))