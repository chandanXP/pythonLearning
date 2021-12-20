tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

# while True:
#      for i in ["/","-", "|", "\\", "|"]:
#           print("%s\r" %i)

# val = "%r"
# data = 9+9
# print("%r"%"(100+1)")

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#escape sequence don't works on passing them in %r[%r prints the value as you have written in the file]
str = "Name:\tChandan"
print("%r"%str)


