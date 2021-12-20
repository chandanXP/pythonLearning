def cheese_and_cracker(
     cheese_count, boxes_of_crackers):
     print("You have %d cheese!"%cheese_count)
     print("You have %d boxes of crackers!"%boxes_of_crackers)
     print("Man that's enough for a party")
     print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_cracker(20,30)

print("Or, we can use variable from our script:")
amount_of_cheese = 10
amount_of_cracker = 50
cheese_and_cracker(amount_of_cheese, amount_of_cracker)

print("We can even do math inside too:")
cheese_and_cracker(10+20, 12-3)

print("And we can combine the two, variable and math:")
cheese_and_cracker(amount_of_cheese*2,amount_of_cracker+3)
