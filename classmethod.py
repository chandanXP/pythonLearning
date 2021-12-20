class A:
     res = True
     @classmethod
     def a(self):
          if(A.res):
               print(f"Response: {A.res}")
          else:
               print(f"Response: {~(A.res)}")
o = A()
o.a()