class Employee:
     def __init__(self):
          print("constructor")
     def display(self):
          pass

class Users(Employee):
     def display(self):
         print("Hello user")
     
     
chandan = Users()
chandan.display()
