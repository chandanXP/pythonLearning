'''
n=5
prdt =1
 
for i in range(n):
     prdt = prdt *(i+1)
print(prdt)
'''

def fact(n):
     prdt =1
     for i in range(n):
          prdt = prdt *(i+1)
     return prdt
print(fact(5))

#factorial recursive
def recurse_fact(n):
     if n is 0 or n is 1:
          return 1
     return n*recurse_fact(n-1)

f = recurse_fact(100)
print(f)