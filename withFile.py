# reading
with open("sample.txt", 'r') as  f:
     a = f.read()
print(a)

#writing
with open("another.txt", 'w') as f:
     f.write("writing in another file")