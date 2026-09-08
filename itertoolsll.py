#itertools: product, permutations, combinations, accumulate, groupby, islice, chain, compress, dropwhile, filterfalse, starmap, tee
from itertools import product 
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod)) # Output: [(1, 3), (1, 4), (2, 3), (2, 4)] gives the Cartesian product of the two lists   
prod = product(a, b, repeat=2)
print(list(prod)) # Output: [(1, 3, 1, 3), (1, 3, 1, 4), (1, 3, 2, 3), (1, 3, 2, 4), (1, 4, 1, 3), (1, 4, 1, 4), (1, 4, 2, 3), (1, 4, 2, 4), (2, 3, 1, 3), (2, 3, 1, 4), (2, 3, 2, 3), (2, 3, 2, 4), (2, 4, 1, 3), (2, 4, 1, 4), (2, 4, 2, 3), (2, 4, 2, 4)] gives the Cartesian product of the two lists with repeat=2

from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(list(perm)) # Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] gives all possible permutations of the list
perm = permutations(a, 2)   
print(list(perm)) # Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)] gives all possible permutations of the list with length 2  

from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb)) # Output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)] gives all possible combinations of the list with length 2  
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr)) # Output: [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)] gives all possible combinations with replacement of the list with length 2  

from itertools import accumulate
import operator
a = [1, 2,5, 3, 4]
acc = accumulate(a)
print(list(acc)) # Output: [1, 3, 6, 10] gives the accumulated sums of the list 
acc = accumulate(a, operator.mul)
print(list(acc)) # Output: [1, 2, 6, 24] gives the accumulated products of the list 
acc= accumulate(a, func= max)
print(list(acc)) # Output: [1, 2, 5, 5, 5] gives the accumulated maximums of the list   

from itertools import groupby
def smaller_than_3(x):
    return x < 3
a= [1, 2, 3, 4]
group= groupby(a, key=smaller_than_3)
for key, value in group:
    print(key, list(value)) # Output: True [1, 2] False [3, 4] gives the grouped elements of the list based on the key function 

group= groupby(a, key=lambda x: x < 3)
for key, value in group:
    print(key, list(value)) # Output: True [1, 2] False [3, 4] gives the grouped elements of the list based on the key function 

person= [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
group= groupby(person, key=lambda x: x['age'])
for key, value in group:
    print(key, list(value)) # Output: 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}] 27 [{'name': 'Lisa', 'age': 27}] 28 [{'name': 'Claire', 'age': 28}] gives the grouped elements of the list based on the key function  

from itertools import count, cycle, repeat
for i in count(10):
    if i > 20:
        break
    else:
        print(i) # Output: 10 11 12 13 14 15 16 17 18 19 20 gives the count of numbers starting from 10 to 20

a = [1, 2, 3]
for i in cycle(a):
    if i > 15:
        break
    else:
        print(i) # Output: 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 gives the cycle of the list until the condition is met

for i in repeat(1, 5):
    print(i) # Output: 1 1 1 1 1 gives the repeated value of 1 for 5 times  
 
