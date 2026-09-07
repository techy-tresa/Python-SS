<<<<<<< HEAD
mydict = {"name": "Tresa", "age": 20, "occupation": "Engineer", "city": "New Delhi", "country": "India"} #dictionary with key-value pairs
print(mydict) # Output: {'name': 'Tresa', 'age': 20, 'occupation': 'Engineer', 'city': 'New Delhi', 'country': 'India'}, printing the dictionary

mydict2= dict(name="Shankar", age=21, occupation="Merhant Navy", city="Kolkata", country="India") #dictionary with key-value pairs
print(mydict2) # Output: {'name': 'Shankar', 'age': 21, 'occupation': 'Merhant Navy', 'city': 'Kolkata', 'country': 'India'}, printing the dictionary

values= mydict["name"]#getting the values of the dictionary
print(values) # Output: Tresa, printing the value associated with the key "name"

mydict["email"]= "tresa@gmail.com" #updating the value of the key "email"
print(mydict) # Output: {'name': 'Tresa', 'age': 20, 'occupation': 'Engineer', 'city': 'New Delhi', 'country': 'India', 'email': 'tresa@gmail.com'}, printing the updated dictionary

del mydict["email"] #deleting the key-value pair with the key "email"
print(mydict) # Output: {'name': 'Tresa', 'age': 20, 'occupation': 'Engineer', 'city': 'New Delhi', 'country': 'India'}, printing the updated dictionary
mydict.pop("age") #removing the key-value pair with the key "age"
print(mydict) # Output: {'name': 'Tresa', 'occupation': 'Engineer', 'city': 'New Delhi', 'country': 'India'}, printing the updated dictionary
mydict.popitem() #removing the last inserted key-value pair
print(mydict) # Output: {'name': 'Tresa', 'occupation': 'Engineer', 'city': 'New Delhi'}, printing the updated dictionary


if "name" in mydict: #checking if the key "name" is present in the dictionary
    print("Yes, 'name' is present in the dictionary") # Output: Yes, 'name' is present in the dictionary    
else:
    print("No, 'name' is not present in the dictionary")

try:
    print(mydict["Name"]) #trying to access the value of the key "Name" which is not present in the dictionary
except KeyError:
    print("Key not found")

for key in mydict: #iterating through the keys of the dictionary
    print(key) # Output: name, occupation, city, printing the keys of the dictionary        

for key, value in mydict.items(): #iterating through the key-value pairs of the dictionary
    print(key, value) # Output: name Tresa, occupation Engineer, city New Delhi 

mydict_cpy= mydict #creating a copy of the dictionary
mydict_cpy["hobby"]= "Reading" #updating the value of the key "hobby" in the copied dictionary
print(mydict_cpy) # Output: {'name': 'Tresa', 'occupation': 'Engineer', 'city': 'New Delhi', 'hobby': 'Reading'}, printing the copied dictionary
print(mydict) # Output: {'name': 'Tresa', 'occupation': 'Engineer', 'city': 'New Delhi', 'hobby': 'Reading'}, printing the original dictionary, showing that it has also been updated

'''dict function and copy() does not change the original dictionary, but creating a copy of the dictionary using assignment operator (=) does change the original dictionary.'''

mydict.update(mydict2) #updating the original dictionary with the key-value pairs of the copied dictionary
print(mydict) # Output: {'name': 'Shankar', 'occupation': 'Merhant Navy', 'city': 'Kolkata', 'country': 'India'}, printing the updated dictionary

square= {2: 4, 4: 16, 6: 36, 8: 64, 10: 100} #dictionary with key-value pairs
print(square) # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}, printing the dictionary   

value = square[6] #getting the value of the key 6
print(value) # Output: 36, printing the value associated with the key 6 

tuple= (12,14)
etc= {tuple: 26} #dictionary with tuple as key and integer as value
print(etc) # Output: {(12, 14): 26}, printing the dictionary
=======
mydict = {"name": "Tresa", "age": 20, "occupation": "Engineer", "city": "New Delhi", "country": "India"} #dictionary with key-value pairs
print(mydict) # Output: {'name': 'Tresa', 'age': 20, 'occupation': 'Engineer', 'city': 'New Delhi', 'country': 'India'}, printing the dictionary

mydict2= dict(name="Shankar", age=21, occupation="Merhant Navy", city="Kolkata", country="India") #dictionary with key-value pairs
print(mydict2) # Output: {'name': 'Shankar', 'age': 21, 'occupation': 'Merhant Navy', 'city': 'Kolkata', 'country': 'India'}, printing the dictionary

values= mydict["name"]#getting the values of the dictionary
print(values) # Output: Tresa, printing the value associated with the key "name"

mydict["email"]= "tresa@gmail.com" #updating the value of the key "email"
print(mydict) # Output: {'name': 'Tresa', 'age': 20, 'occupation': 'Engineer', 'city': 'New Delhi', 'country': 'India', 'email': 'tresa@gmail.com'}, printing the updated dictionary

del mydict["email"] #deleting the key-value pair with the key "email"
print(mydict) # Output: {'name': 'Tresa', 'age': 20, 'occupation': 'Engineer', 'city': 'New Delhi', 'country': 'India'}, printing the updated dictionary
mydict.pop("age") #removing the key-value pair with the key "age"
print(mydict) # Output: {'name': 'Tresa', 'occupation': 'Engineer', 'city': 'New Delhi', 'country': 'India'}, printing the updated dictionary
mydict.popitem() #removing the last inserted key-value pair
print(mydict) # Output: {'name': 'Tresa', 'occupation': 'Engineer', 'city': 'New Delhi'}, printing the updated dictionary


if "name" in mydict: #checking if the key "name" is present in the dictionary
    print("Yes, 'name' is present in the dictionary") # Output: Yes, 'name' is present in the dictionary    
else:
    print("No, 'name' is not present in the dictionary")

try:
    print(mydict["Name"]) #trying to access the value of the key "Name" which is not present in the dictionary
except KeyError:
    print("Key not found")

for key in mydict: #iterating through the keys of the dictionary
    print(key) # Output: name, occupation, city, printing the keys of the dictionary        

for key, value in mydict.items(): #iterating through the key-value pairs of the dictionary
    print(key, value) # Output: name Tresa, occupation Engineer, city New Delhi 

mydict_cpy= mydict #creating a copy of the dictionary
mydict_cpy["hobby"]= "Reading" #updating the value of the key "hobby" in the copied dictionary
print(mydict_cpy) # Output: {'name': 'Tresa', 'occupation': 'Engineer', 'city': 'New Delhi', 'hobby': 'Reading'}, printing the copied dictionary
print(mydict) # Output: {'name': 'Tresa', 'occupation': 'Engineer', 'city': 'New Delhi', 'hobby': 'Reading'}, printing the original dictionary, showing that it has also been updated

'''dict function and copy() does not change the original dictionary, but creating a copy of the dictionary using assignment operator (=) does change the original dictionary.'''

mydict.update(mydict2) #updating the original dictionary with the key-value pairs of the copied dictionary
print(mydict) # Output: {'name': 'Shankar', 'occupation': 'Merhant Navy', 'city': 'Kolkata', 'country': 'India'}, printing the updated dictionary

square= {2: 4, 4: 16, 6: 36, 8: 64, 10: 100} #dictionary with key-value pairs
print(square) # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}, printing the dictionary   

value = square[6] #getting the value of the key 6
print(value) # Output: 36, printing the value associated with the key 6 

tuple= (12,14)
etc= {tuple: 26} #dictionary with tuple as key and integer as value
print(etc) # Output: {(12, 14): 26}, printing the dictionary
>>>>>>> ddece29d48cfaa508d442a69fc93d798dd484c2c
