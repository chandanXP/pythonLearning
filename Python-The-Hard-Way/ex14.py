from sys import argv
script, filename = argv

print("We're going to erase %r."%filename)
print("If you don't want that, hit CTRL+C(^C).")
print("If you do want that, hit Enter." )

input("? ")

print("Opening the file...")
target = open(filename,'w')

print("Truncate the file. Goodbye!")
#Deleted the content of the file
target.truncate() 

print("Now I'm going to ask you for three line.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

#writing in the file 
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Finally we close it!")
#closing the file
target.close()
