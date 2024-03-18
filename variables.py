# variables are nothing but the name of the allocated memory storage where the value can be stored.

x = 10
a = 'python'

print(x)
print(a)


# Type casting using variables

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0



# We can also get the type of the variable 

x = 5
y = "John"
print(type(x))
print(type(y))

# We can create the string using single or double quotes

x = "John"
# is the same as
x = 'John'

# Example of variables

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Assigning multiple values to the variable

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Assigning same values to multiple variable
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpacking the collection of the data to the variables

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

'''
Basically there are 2 types of variables in python. 
1. Local variable 
2. Global variable
Here are some examples
'''

# Local variables (it comes always whenever mentioned in program)

def run():
    x = 'hi'
    print(x)

run()

# Global variable (it comes when local variable is not present)

x = 'hello'

def run():
    # x = 'hi'
    print(x)

run()

