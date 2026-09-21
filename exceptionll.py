#Errors and exceptions
a = 10 print(a) # error: invalid syntax because there is no new line after 10   
a= 10 print(a)) # error: invalid syntax because there is an extra closing parenthesis
a= 20 +"2" # error: unsupported operand type(s) for +: 'int' and 'str' because we are trying to add an integer and a string
import mmm # error: No module named 'mmm' because we are trying to import a module that does not exist  
a=4
b= c #error: c not defined 
f = open('easyfile.txt') #error: no such file found 

a=[1,2,3]
print(a.index(6)) #error: index not found 

my_dict= {'name':"bb"}
my_dict['age'] #error

#Errors and exceptions
a = 10 print(a) # error: invalid syntax because there is no new line after 10   
a= 10 print(a)) # error: invalid syntax because there is an extra closing parenthesis
a= 20 +"2" # error: unsupported operand type(s) for +: 'int' and 'str' because we are trying to add an integer and a string
import mmm # error: No module named 'mmm' because we are trying to import a module that does not exist  
a=4
b= c #error: c not defined 
f = open('easyfile.txt') #error: no such file found 

a=[1,2,3]
print(a.index(6)) #error: index not found 

my_dict= {'name':"bb"}
my_dict['age'] #error: age key not in dictionary 

x = -5
if x <0:
    raise Exception('x should be positive')

#OR 
x = -7
assert (x>=0), 'x is not positive'

try:
    a = 5/0 
except Exception as e:
    print(e)


try: 
    b = 5/1
    c= b + "10"
except ZeroDivisionError as e:
    print(e) 
except TypeError as e:
    print(e)
else:
    print("it is fine")
finally:
    print("cleanin up..") #output: division by zero     cleaning up...

class ValueTooHighError(Exception):
    pass #use to define own class

class ValueTooSmallError(Exception):
    def _init_(self, message, value ):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x<10:
            raise ValueTooSmallError("value too small")
try:    
    test_value(200) 
except ValueTooHighError as e:
    print(e) #Output: value is too high
except ValueTooSmallError as e:
    print(e.message, e.value) #Output: value is too high 200