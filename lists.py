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