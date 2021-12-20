my_name = 'Chandan'
my_age = 23
my_height = 70 #inches
my_weight = 52 
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'browm'
my_grade = 8.2
my_num = 9.82341671

print("Let's talk about %s" %my_name)
print("He's %d inches tall." %my_height)
print("He's %d pounds heavy." %my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair."%(my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee"%my_teeth)
 
# this line is tricky, try ot get it exactly right
print("If I add %d, %d, and %d I get %d."%(my_age, my_height, my_weight, my_age + my_height + my_weight))
print("My grades are: %f" %my_grade)
print("My number is : %3f" %my_num)
print("round(my_num):",round(my_num,2))