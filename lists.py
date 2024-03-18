thislist = ["apple", "banana", "cherry"]
print(thislist)

# Checkigng length and type of the list
def list_items(list):
    print(len(list))
    print(type(list))

list_items(thislist)

# We can also use the list constructor 
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# list indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Modification in list elements

def change(nlist, value, new):
    nlist = list(nlist)
    nlist[value] = new
    print(nlist)

change(thislist, 0, 'orange')

# Modification in  range of list elements

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert function in list

def list_insert(nlist, posi, value):
    nlist = list(nlist)
    nlist.insert(posi, value)
    print(nlist)


list_insert(thislist,2, "pineapple")

# Adding new elements in list

thislist = ["apple", "banana", "cherry"]

def add_list(nlist):
    nlist = list(nlist)
    nlist.append("orange")
    print(nlist)

add_list(thislist)
# Extending the list

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
def extend_list(nlist):
    nlist = list(nlist)
    nlist.extend(tropical)
    print(nlist)

extend_list(thislist)


# Removing elements in list

thislist = ["apple", "banana", "cherry"]
def remove_list(nlist):
    nlist = list(nlist)
    nlist.remove("banana")
    print(nlist)

remove_list(thislist)

# for removing second element in the list

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Removing first element from the list
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Removing whole list

thislist = ["apple", "banana", "cherry"]
del thislist


# Clearing the list

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) 


# Looping in list

# for loop

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#   while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#   single hand loop
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# syntax newlist = [expression for item in iterable if condition == True]

# sorting list

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# decending sort

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# reversing the list

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# list copy function
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Joins in list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

'''
Python list methods
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

