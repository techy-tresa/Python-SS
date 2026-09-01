mylist= ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(mylist) # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']

mylist2= list() #empty list
print(mylist2)

item= mylist[1] #indexing
print(item) # Output: banana

'''item= mylist[7]
print(item) # Output: IndexError: list index out of range'''

item2= mylist[-1] #negative indexing
print(item2) # Output: elderberry

for i in mylist:
    print(i) # Output: apple banana cherry date elderberry

if "date" in mylist:
    print("Yes") # Output: Yes, 'date' is in the fruits list
else:
    print("No")

len(mylist) # Output: 5, the length of the list

mylist.append("fig") # Adding an item to the end of the list
print(mylist) # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

mylist.insert(2, "grape") # Inserting an item at a specific index
print(mylist) # Output: ['apple', 'banana', 'grape', 'cherry', 'date', 'elderberry', 'fig']

mylist.pop(4) # Removing an item by index
print(mylist) # Output: ['apple', 'banana', 'grape', 'cherry', 'elderberry', 'fig']

mylist.remove("banana") # Removing an item by value
print(mylist) # Output: ['apple', 'grape', 'cherry', 'elderberry', 'fig']

mylist.sort() # Sorting the list in ascending order
print(mylist) # Output: ['apple', 'cherry', 'elderberry', ' fig', 'grape']

new_list= mylist.copy() # Creating a copy of the list
new_list.reverse() # Reversing the copied list
print(new_list) # Output: ['grape', ' fig', 'elderberry', 'cherry', 'apple']  

a= [0] *5 
print(a) # Output: [0, 0, 0, 0, 0]

b= [1, 2, 3, 4, 5]
c= a + b # Concatenating two lists
print(c) # Output: [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]

d= c[4:9]
print(d) # Output: [0, 1, 2, 3, 4]

e= d[::2]
print(e) # Output: [0, 2, 4], slicing with a step of 2

f= d[::-1]
print(f) # Output: [4, 3, 2, 1, 0]

num = f()
num.append(-1,-2,-3) # Adding multiple items to the list
print(num) # Output: [4, 3, 2, 1, 0, -1, -2, -3]

print(f) # Output: [4, 3, 2, 1, 0]

digits= [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares=[ i**2 for i in digits] # List comprehension to create a list of squares
print(squares) # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]
