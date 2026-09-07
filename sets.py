<<<<<<< HEAD
myset={[1,2,3],4,5, 4, 5, 10, 12 } #set with integer values
print(myset) # Output: {1, 2, 3, 4, 5, 10, 12}, printing the set

hw= set("Hello World") #set with string values
print(hw) # Output: {' ', 'd', 'e', 'H', 'l', 'o', 'r', 'W'}, printing the set, gives unique characters in the string

myset.add(15) #adding the value 15 to the set
print(myset) # Output: {1, 2, 3, 4, 5, 10, 12, 15}, printing the updated set    
myset.remove(4) #removing the value 4 from the set
print(myset) # Output: {1, 2, 3, 5, 10, 12, 15}, printing the updated set       
myset.discard(5) #removing the value 5 from the set
print(myset) # Output: {1, 2, 3, 10, 12, 15}, printing the updated set  
myset.pop() #removing a random value from the set
print(myset) # Output: {2, 3, 10, 12, 15}, printing the updated set, the value removed is random and may vary each time the code is run 
myset.clear() #removing all the values from the set
print(myset) # Output: set(), printing the updated set, which is now empty  

for i in myset: #iterating through the values of the set
    print(i) # Output: 2, 3, 10, 12, 15, printing the values of the set     

if 10 in myset: #checking if the value 10 is present in the set
    print("Yes, 10 is present in the set") # Output: Yes, 10 is present in the set      
else:
    print("No, 10 is not present in the set")   

odd ={1, 3, 5, 7, 9} #set with odd numbers
even ={2, 4, 6, 8, 10} #set with even numbers
prime ={2, 3, 5, 7} #set with prime numbers

u = odd.union(even) #union of odd and even sets
print(u) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, printing the union of odd and even sets
i = odd.intersection(prime) #intersection of odd and prime sets     
print(i) # Output: {3, 5, 7}, printing the intersection of odd and prime sets   

diff = odd.difference(prime) #difference of odd and prime sets
print(diff) # Output: {1, 9}, printing the difference of odd and prime sets 

diff2= prime.symmetric_difference(odd) #symmetric difference of prime and odd sets
print(diff2) # Output: {1, 2, 9}, printing the symmetric difference of prime and odd sets, which is the set of elements that are in either of the sets but not in their intersection    

odd.update(even) #updating the odd set with the values of the even set
print(odd) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, printing the updated odd set  

odd.intersection_update(prime) #updating the odd set with the intersection of odd and prime sets
print(odd) # Output: {3, 5, 7}, printing the updated odd set, which now contains only the values that are present in both the odd and prime sets    

odd.difference_update(prime) #updating the odd set with the difference of odd and prime sets
print(odd) # Output: {1, 9}, printing the updated odd set,  which now contains only the values that are present in the odd set but not in the prime set 

odd.symmetric_difference_update(prime) #updating the odd set with the symmetric difference of odd and prime sets
print(odd) # Output: {1, 2, 9}, printing the updated    odd set, which now contains only the values that are in either of the sets but not in their intersection    

setA= {1, 2, 3, 4, 5} 
setB= {1, 2, 3}

print(setA.issubset(setB)) # Output: False, checking if setA is a subset of setB
print(setB.issubset(setA)) # Output: True, checking if setB is a subset of setA 
print(setA.issuperset(setB)) # Output: True, checking if setA is a superset of setB 
print(setB.issuperset(setA)) # Output: False, checking if setB is a superset of setA    
print(setA.isdisjoint(setB)) # Output: False, checking if setA and setB have no elements in common  

a= frozenset([1, 2, 3, 4, 5]) #creating a frozenset with integer values
print(a) # Output: frozenset({1, 2, 3, 4, 5}), printing the frozenset
a.add(6)
print(a) #frozenset object does not support item assignment, so this will raise an AttributeError   

'''union, intersection etc can work with frozensets but no add, remove etc.'''
=======
myset={[1,2,3],4,5, 4, 5, 10, 12 } #set with integer values
print(myset) # Output: {1, 2, 3, 4, 5, 10, 12}, printing the set

hw= set("Hello World") #set with string values
print(hw) # Output: {' ', 'd', 'e', 'H', 'l', 'o', 'r', 'W'}, printing the set, gives unique characters in the string

myset.add(15) #adding the value 15 to the set
print(myset) # Output: {1, 2, 3, 4, 5, 10, 12, 15}, printing the updated set    
myset.remove(4) #removing the value 4 from the set
print(myset) # Output: {1, 2, 3, 5, 10, 12, 15}, printing the updated set       
myset.discard(5) #removing the value 5 from the set
print(myset) # Output: {1, 2, 3, 10, 12, 15}, printing the updated set  
myset.pop() #removing a random value from the set
print(myset) # Output: {2, 3, 10, 12, 15}, printing the updated set, the value removed is random and may vary each time the code is run 
myset.clear() #removing all the values from the set
print(myset) # Output: set(), printing the updated set, which is now empty  

for i in myset: #iterating through the values of the set
    print(i) # Output: 2, 3, 10, 12, 15, printing the values of the set     

if 10 in myset: #checking if the value 10 is present in the set
    print("Yes, 10 is present in the set") # Output: Yes, 10 is present in the set      
else:
    print("No, 10 is not present in the set")   

odd ={1, 3, 5, 7, 9} #set with odd numbers
even ={2, 4, 6, 8, 10} #set with even numbers
prime ={2, 3, 5, 7} #set with prime numbers

u = odd.union(even) #union of odd and even sets
print(u) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, printing the union of odd and even sets
i = odd.intersection(prime) #intersection of odd and prime sets     
print(i) # Output: {3, 5, 7}, printing the intersection of odd and prime sets   

diff = odd.difference(prime) #difference of odd and prime sets
print(diff) # Output: {1, 9}, printing the difference of odd and prime sets 

diff2= prime.symmetric_difference(odd) #symmetric difference of prime and odd sets
print(diff2) # Output: {1, 2, 9}, printing the symmetric difference of prime and odd sets, which is the set of elements that are in either of the sets but not in their intersection    

odd.update(even) #updating the odd set with the values of the even set
print(odd) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, printing the updated odd set  

odd.intersection_update(prime) #updating the odd set with the intersection of odd and prime sets
print(odd) # Output: {3, 5, 7}, printing the updated odd set, which now contains only the values that are present in both the odd and prime sets    

odd.difference_update(prime) #updating the odd set with the difference of odd and prime sets
print(odd) # Output: {1, 9}, printing the updated odd set,  which now contains only the values that are present in the odd set but not in the prime set 

odd.symmetric_difference_update(prime) #updating the odd set with the symmetric difference of odd and prime sets
print(odd) # Output: {1, 2, 9}, printing the updated    odd set, which now contains only the values that are in either of the sets but not in their intersection    

setA= {1, 2, 3, 4, 5} 
setB= {1, 2, 3}

print(setA.issubset(setB)) # Output: False, checking if setA is a subset of setB
print(setB.issubset(setA)) # Output: True, checking if setB is a subset of setA 
print(setA.issuperset(setB)) # Output: True, checking if setA is a superset of setB 
print(setB.issuperset(setA)) # Output: False, checking if setB is a superset of setA    
print(setA.isdisjoint(setB)) # Output: False, checking if setA and setB have no elements in common  

a= frozenset([1, 2, 3, 4, 5]) #creating a frozenset with integer values
print(a) # Output: frozenset({1, 2, 3, 4, 5}), printing the frozenset
a.add(6)
print(a) #frozenset object does not support item assignment, so this will raise an AttributeError   

'''union, intersection etc can work with frozensets but no add, remove etc.'''
>>>>>>> ddece29d48cfaa508d442a69fc93d798dd484c2c
