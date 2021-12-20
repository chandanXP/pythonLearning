class Amazon:
     code =100
     items= {"iPhone" : 1, "Television": 1, "Cookie": 12 }
     @classmethod
     def contact_amazon(self ):
          print(f"{Amazon.code}Your order is ready to deliver")
          
class BlueDart(Amazon):
     code= 110
     def contact_blueDart(self):
          print(f"Your {self.items} is on the way")
class User(BlueDart):
     code=111
     def product(self):
          print(super().code)
          print(f"Your order of {self.items} have been placed thank you!")
           

chandan = User()

 
chandan.contact_amazon()

print(BlueDart.code)
chandan.contact_blueDart()

print(User.code)
chandan.product()



