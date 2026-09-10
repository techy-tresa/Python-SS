#lambda arguments: expression
from functools import reduce


add10 = lambda x : x +10
print(add10(5)) # Output: 15

mul= lambda x, y : x * y
print(mul(5, 6)) # Output: 30

point= [(1, 2), (15, 5), (9, 6), (12, 4)]
point_sort= sorted(point,)
print(point_sort) # Output: [(1, 2), (9, 6), (12, 4), (15, 5)] gives the sorted list of tuples based on the first element of each tuple 
point_sort= sorted(point, key=lambda x: x[1])
print(point_sort) # Output: [(1, 2), (12, 4), (15, 5), (9, 6)] gives the sorted list of tuples based on the second element of each tuple    
point_sort= sorted(point, key=lambda x: x[0]+x[1])
print(point_sort) # Output: [(1, 2), (12, 4), (15, 5), (9, 6)] gives the sorted list of tuples based on the sum of the elements of each tuple   

#map(function, sequence)
a= [1, 2, 3, 4, 5]
b= list(map(lambda x: x * 2, a))
print(b) # Output: [2, 4, 6, 8, 10] gives the list of elements after applying the function to each element of the sequence  

#filter(function, sequence)
a= [1, 2, 3, 4, 5]
c= list(filter(lambda x: x > 3, a))
print(c) # Output: [4, 5] gives the list of elements that satisfy the condition in the function
d= list(filter(lambda x: x % 2 == 0, a))
print(d) # Output: [2, 4] gives the list of elements that satisfy the condition in the function 

#reduce(function, sequence)
from functools import reduce
a= [1, 2, 3, 4, 5]
p_a= reduce(lambda x, y: x * y, a)
print(p_a) # Output: 120 gives the product of all elements in the sequence
p_b= reduce(lambda x, y: x + y, a)
print(p_b) # Output: 15 gives the sum of all elements in the sequence   