# f= open('sample.txt', 'r')
f= open('sample.txt', 'w' ) #be default mode is 'r'
# data = f.read()
# data = f.read(20) #reads first 20 character in file
# data = f.read()
# data = f.readline() #reads \n 'new line character also'
f.write("\nadding new content in file")
f.write("\nformat")

f.close()