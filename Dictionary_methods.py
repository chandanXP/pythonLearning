myDict = {
     "fast": "In a quick manner",
     "chandan": "A coder",
     "marks": [1,2,3],
     "anotherDict": {'Cad3n': 'player', 'score': 'platinum III'},
     32: 45
     #'keys': 'values'
}
#NOTE: Dictionary is unordered
#methods
print(type(myDict))
print(myDict.keys())# prints the keys of the dictionary
print(type(myDict.keys())) #type of a dictionary
print(list(myDict.keys())) #typecasting of a dictionary
print(myDict.values())  #values
print(myDict.items()) # all contents of a dictionary 

update ={
     'laguage': "English",
     'country': "Cananda",
     'fast': 'af'
}

myDict.update(update) #to update myDict
#print(myDict.get("chandan")) #will return 'None' if values not found, to avoid key error we use this method
#print(myDict["chandan"]) #will return error if the value not found
print(myDict)


