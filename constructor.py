class Employee:
     company = "Google"
     salary = 400
     # def __init__(self) :
     #     print("New user is created..")
     def __init__(self , name , salary, subunit) :
          self.name = name
          self.salary = salary
          self.subunit = subunit
          print("New user is created..")
     def getDetails(self):
          print(f"Name: {self.name}")
          print(f"Salary: {self.salary}")
          print(f"Sub Unit: {self.subunit}")
     def getSalary(self,signatue):
          print(f"Age is {self.age} in {self.company}\n{signatue}")

chandan = Employee("chandan" , 100, "YouTube")
chandan.age = 24
chandan.getDetails()
chandan.getSalary("Thank you!")
 