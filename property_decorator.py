class Employee:
     company = "Bharat Gas"
     salary  = 5600
     salary_bonus = 500
     # total_salary = 6100
     @property #will convert the method into a propety of a class [getter]
     def totalSalary(self):
          return self.salary + self.salary_bonus
     @totalSalary.setter
     def totalSalary(self, val):
          self.salary_bonus = val-self.salary
e = Employee()
print(e.totalSalary)

e.totalSalary = 5800 #setter
print(e.salary_bonus)