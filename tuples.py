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


