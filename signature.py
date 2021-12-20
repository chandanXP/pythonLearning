class Employee:
     company = "Google"
     salary = 400
     def getSalary(self,signatue):
          print(f"salary is {self.amt} in {self.company}\n{signatue}")
     @staticmethod
     def greetUser():
          print("hello there!")
chandan = Employee()
chandan.amt = 50000
chandan.greetUser() 
chandan.getSalary("Thank you!")
