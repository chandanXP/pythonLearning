class RailwayForm:
     val = 100
     formType = 'railway form'
     def print_data(self):
          print(f"name is  {self.name}")
          print(f"age is  {self.age}")
          print(f"train is {self.train}")
          
Passenger = RailwayForm()
Passenger.name = "chandan"
Passenger.age = 23
Passenger.train = "Rajdhani Exp"
Passenger.val = 90 #updating object attribute
Passenger.print_data()
RailwayForm.val =98 #updating object attribute
print(RailwayForm.val)