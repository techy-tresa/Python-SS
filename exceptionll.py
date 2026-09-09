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

