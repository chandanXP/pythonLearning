class A:
     var_code_A = 1
     same = 911
     def a(self):
          print("message from parent class A.")
class B:
     var_code_B = 2
     same =101
     def b(self):
          print("message from parent class B")
class Child(A, B):
     def a(self):
          print("message coming from parent A. inherited in child class.")
     def b(self):
          print("message coming from parent B. inherited in child class.")
     def childMethod(self):
          print("message from child method.")

# child instanciation 
c= Child()
c.a()
c.b()
c.childMethod()
print(c.var_code_A)
print(c.var_code_B)
print(c.same)

# parent isinstanciation
pA = A()
pA.a()
print(pA.var_code_A)

pB = B()
pB.b()
print(pB.var_code_B)