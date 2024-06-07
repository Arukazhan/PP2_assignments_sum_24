#No assigning of a variable 
y = 'Am I human?'#python automatically assumes it is str
x = 7 #int


z = 7      # z's type is int
z = "damn" # z's type is changed to str here
print(z)
print(type(z)) 



#Casting
a = str(7)    
b = int(7)  
c = float(7)  


#variable name rules
#R1. letter or underscore
lol = 'laughing'
_lol = 'out'
'''
no number-start, can contain number(A-z, 0-9,_)
1_lol = 'loud'   
lol_1 = 'loud'   
'''

#R2. Case-sensitive
P = 'cool'
p = 404

lmao = 77
LmAo = 77 #basically, they are not the same


#R3. keywords
'''
and, if, break, etc
'''



'''
why is this wrong?
2myvar = "John"
my-var = "John"
my var = "John"
'''




#Multi Words 
"""
Camel case - myVariableName
Pascal case  - MyVariableName
Snake case - my_variable_name
"""



#easy Assigning
q, w, e = "Orange", "Banana", "Cherry"
r = t = y = "Orange"




#unpack
fruits = ["apple", "banana", "cherry"]
u, i, o = fruits
print(u, i, o)
print(u + i + o)





#local and global var
s = "awesome"

def myfunc1():
  s = "fantastic"
  print("Python is " + s)

myfunc1()

print("Python is " + s)

#keyword global
d = "awesome"

def myfunc2():
  global d
  d = "fantastic"

myfunc2()

print("Python is " + d)