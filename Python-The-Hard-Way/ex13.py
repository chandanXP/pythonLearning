from sys import argv

script, filename = argv

txt = open(filename)
print("Here is your file %r:"%filename)
print(txt.read())

print("Type the file again")
file_again  = input("> ") 

#opening the same file again
txt_again = open(file_again)
print(txt_again.read())