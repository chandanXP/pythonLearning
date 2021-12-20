class Employee:
     company = "Google"
     salary = 400
     def getSalary(self):
          print(f"salary is {self.amt} in {self.company}")
     @staticmethod
     def greetUser():
          print("hello there!")
chandan = Employee()
chandan.amt = 50000
chandan.getSalary()
chandan.greetUser() #we cannot use self here
#chandan.greetUser(self) #we cannot use self here