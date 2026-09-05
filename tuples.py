mytuples = ("Tresa", 28, "Engineer",) #paranthesis is optional 
print(mytuples)

tup= tuple(["Tresa", 28, "Engineer"]) #list converted to tuples
print(tup)

print(mytuples[0]) # Output: Tresa, indexing

print(len(mytuples)) # Output: 3, length of tuple

#tup[0]= "John" # Output: TypeError: 'tuple' object does not support item assignment, tuples are immutable

for i in tup:
    print(i) # Output: Tresa 28 Engineer, iterating through the tuple

if "Engineer" in mytuples:
    print("Yes") # Output: Yes, 'Engineer' is in the tuple
else:
    print("No")


print(len(tup)) # Output: 3, length of the tuple
print(tup.count("Tresa")) # Output: 1, count of 'Tresa' in the tuple
print(tup.index("28")) # Output: 1, index of '28' in the tuple
print(tup.index("Nayak")) # Output: ValueError: tuple.index(x): x not in tuple, 'Nayak' is not in the tuple

my_list= list(tup) #tuple converted to list
print(my_list) # Output: ['Tresa', 28, 'Engineer'], tuple converted to list
my_please= tuple(my_list) #list converted to tuple
print(my_please) # Output: ('Tresa', 28, 'Engineer'), list converted to tuple

a= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:6] #slicing the tuple   
print(b) # Output: (3, 4, 5, 6), slicing the tuple
b= a[::-1] #slicing with a step of 1
print(b) # Output: (10, 9, 8, 7, 6), slicing with a step of 1

n= (1, 2, 3, 4, 5, 6, 7, 8, 9)
i1, *i2, i3= n #unpacking the tuple
print(i1) # Output: 1, first element of the tuple   
print(i2) # Output: [2, 3, 4, 5, 6, 7, 8], middle elements of the tuple
print(i3) # Output: 9, last element of the tuple

'''A list has larger memory overhead than a tuple. Tuples are more memory efficient than lists, especially for large collections of data. 
This is because tuples are immutable and have a fixed size, 
while lists can grow and shrink dynamically, which requires additional memory management.'''

'''working with tuples is faster than working with lists. Since tuples are immutable, they can be optimized by the Python interpreter for performance.'''
