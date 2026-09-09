<<<<<<< HEAD
#collection: counter, namedtuple, OrderedDict, defaultdict, deque, ChainMap, UserDict, UserList, UserString
from collections import Counter
a= "abcdabcd"
my_counter = Counter(a)
print(my_counter) # Output: Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2}) gives in the form of dictionary 

print(my_counter.items()) # Output: dict_items([('a', 2), ('b', 2), ('c', 2), ('d', 2)]) gives in the form of list of tuples
print(my_counter.keys()) # Output: dict_keys(['a', 'b', 'c', 'd']) gives in the form of list of keys
print(my_counter.values()) # Output: dict_values([2, 2, 2, 2]) gives in the form of list of values  
print(my_counter.most_common(2)) # Output: [('a', 2), ('b', 2)] gives the most common elements and their counts
print(list(my_counter.elements())) # Output: ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'] gives the elements in the counter as a list
print(my_counter.elements()) # Output: <itertools.chain object at 0x7f8b8c8c8c8c> gives the elements in the counter as an iterator

from collections import namedtuple
Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt) # Output: Point(x=1, y=-4) gives the namedtuple object
print(pt.x, pt.y) # Output: 1 -4 gives the values of the namedtuple object

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict) # Output: OrderedDict([('a', 1), ('b', 2)]) gives the ordered dictionary object

from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print (d['c']) # Output: 0 gives the default value for the key 'c' which is not present in the dictionary   
print(d['a']) # Output: 1 gives the value for the key 'a' which is present in the dictionary    

from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d) # Output: deque([1, 2]) gives the deque object
d.appendleft(5)
print(d) # Output: deque([5, 1, 2]) gives the deque object after appending to the left
d.pop() 
print(d) # Output: deque([5, 1]) gives the deque object after popping from the right
d.popleft()
print(d) # Output: deque([1]) gives the deque object after popping from the left    
d.clear()
print(d) # Output: deque([]) gives the deque object after clearing all elements
d.extend([1, 2, 3])
print(d) # Output: deque([1, 2, 3]) gives the deque object after extending with a list  
d.extendleft([4, 5, 6])
print(d) # Output: deque([6, 5, 4, 1,   2, 3]) gives the deque object after extending to the left with a list   
d.rotate(1)
print(d) # Output: deque([3, 6, 5, 4, 1, 2]) gives the deque object after rotating to the right by 1    
d.rotate(-1)
print(d) # Output: deque([6, 5, 4, 1, 2, 3]) gives the deque object after rotating to the left by 1 

=======
#collection: counter, namedtuple, OrderedDict, defaultdict, deque, ChainMap, UserDict, UserList, UserString
from collections import Counter
a= "abcdabcd"
my_counter = Counter(a)
print(my_counter) # Output: Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2}) gives in the form of dictionary 

print(my_counter.items()) # Output: dict_items([('a', 2), ('b', 2), ('c', 2), ('d', 2)]) gives in the form of list of tuples
print(my_counter.keys()) # Output: dict_keys(['a', 'b', 'c', 'd']) gives in the form of list of keys
print(my_counter.values()) # Output: dict_values([2, 2, 2, 2]) gives in the form of list of values  
print(my_counter.most_common(2)) # Output: [('a', 2), ('b', 2)] gives the most common elements and their counts
print(list(my_counter.elements())) # Output: ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'] gives the elements in the counter as a list
print(my_counter.elements()) # Output: <itertools.chain object at 0x7f8b8c8c8c8c> gives the elements in the counter as an iterator

from collections import namedtuple
Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt) # Output: Point(x=1, y=-4) gives the namedtuple object
print(pt.x, pt.y) # Output: 1 -4 gives the values of the namedtuple object

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict) # Output: OrderedDict([('a', 1), ('b', 2)]) gives the ordered dictionary object

from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print (d['c']) # Output: 0 gives the default value for the key 'c' which is not present in the dictionary   
print(d['a']) # Output: 1 gives the value for the key 'a' which is present in the dictionary    

from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d) # Output: deque([1, 2]) gives the deque object
d.appendleft(5)
print(d) # Output: deque([5, 1, 2]) gives the deque object after appending to the left
d.pop() 
print(d) # Output: deque([5, 1]) gives the deque object after popping from the right
d.popleft()
print(d) # Output: deque([1]) gives the deque object after popping from the left    
d.clear()
print(d) # Output: deque([]) gives the deque object after clearing all elements
d.extend([1, 2, 3])
print(d) # Output: deque([1, 2, 3]) gives the deque object after extending with a list  
d.extendleft([4, 5, 6])
print(d) # Output: deque([6, 5, 4, 1,   2, 3]) gives the deque object after extending to the left with a list   
d.rotate(1)
print(d) # Output: deque([3, 6, 5, 4, 1, 2]) gives the deque object after rotating to the right by 1    
d.rotate(-1)
print(d) # Output: deque([6, 5, 4, 1, 2, 3]) gives the deque object after rotating to the left by 1 

>>>>>>> 19cf891a9cdd4f1b699ad7cac9a161d993ab7e9f
