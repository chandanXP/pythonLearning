class Employee:
     company = "Google"
     def showDetails(self):
          print("this is an employee")


class Programmer(Employee):
     Language = "Python"
     company = "YouTube"
     def getLanguage(self):
          print(f"Laguage is {self.Language}")
     def showDetails(self):
          print("this is a Programmer")

     

e = Employee()
e.showDetails()
print(e.company)

p= Programmer()
p.showDetails()
print(p.company)
