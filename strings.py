str = "I am a Programmer"
print(str) # Output: I am a Programmer
str2 = """used for multi-line strings"""
print(str2)

char = str[2]
print(char) # Output: a
#strings are ordered, immutable, and allow duplicate characters. Strings are also iterable, which means you can loop through the characters in a string.

substring = str[5:10]
print(substring) # Output: a Prog

greeting = "good morning"
name = "tresa"
sen= greeting + " " + name
print(sen) # Output: good morning tresa

for i in greeting:
    print (i)

if "good" in greeting:
    print("yes, 'good' is present in the greeting string") # Output: yes, 'good' is present in the greeting string  
else:
    print("no, 'good' is not present in the greeting string")   

sen= sen.strip() # removes leading and trailing whitespace
print(sen) # Output: good morning tresa
print(sen.upper()) # Output: GOOD MORNING TRESA
print(sen.lower()) # Output: good morning tresa
print(sen.startswith("good")) # Output: True
print(sen.endswith("tresa")) # Output: True 
print(sen.replace("tresa", "john")) # Output: good morning john 
print(sen.split()) # Output: ['good', 'morning', 'tresa']    #forms a list
new_sen = " ".join(sen.split())
print(new_sen) # Output: good morning tresa
print(sen.find("afternoon")) # Output: -1 (not found)
print(sen.count("o")) # Output: 3 (number of occurrences of 'o' in the string)
ss= 's'*6
print(ss) # Output: ssssss
sa= ss + 'a'*3
print(sa) # Output: sssssssaaa

var="tap tap"
qwe= "the variable is %s" % var
print(qwe) # Output: the variable is tap tap
#for numbers we use %d for integers and %f for floating point numbers.
qwe= "the variable is {} and the number is {}".format(var, 5)
print(qwe) # Output: the variable is tap tap and the number is 5    
