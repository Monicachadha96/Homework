#capitalize() will print a string and make the first letter of the first word a capital
a = 'hello'
print(a.capitalize())
# output will be Hello

#casefold() converts strings to case folded strings for caseless matching
b = 'HELLO'
print(b.casefold())
# output will be HELLO

#center() will center align the string, you csn use a specified character to do this, although a space is default
c = 'hello'
print(c.center(20,'-'))
# output will be -------hello--------

#count() will count the number of times an element appears in a list
d = [1,2,1,2,1]
print(d.count(2))
# output will be 2

#endswith() will check if a string ends with the specified suffix and return True or False depending on if it matches, True if it matches
e = 'hello'
print(e.endswith('lo'))
# output will be True

#find() will find where the first occurence of a specified element is, if it cannot find it in a string it will return -1
f = 'hello'
print(f.find('z'))
# output will be -1

#format() formats specified values and will them put them inside a string's placeholder
g = "The price is {:,}"
print(g.format(1000))
# output will be: The price is 1,000

#index() returns the index of where an element is in the string
h = 'hello'
print(h.index('e'))
# output will be: 1

#isalnum() will check if all the characters in the text are alphanumeric and will return True if that is the case otherwise will return False
i = "Hello1"
print(i.isalnum())
# output will be: True

#isalpha() will check if all the characters in the text are letters and will return True if that is the case otherwise will return False
i = "Hello1"
print(i.isalpha())
# output will be: False

#isdigit() will check if all the characters in the text are digits and will return True if that is the case otherwise will return False
i = "Hello1"
print(i.isdigit())
# output will be: False

#islower() will check if all the characters in the text are in lower case and will return True if that is the case otherwise will return False
j = "hello"
print(j.islower())
# output will be: True

#isnumeric() will check if all the characters in the text are numeric characters (this includes more than just digits such as decimals) and will return True if that is the case otherwise will return Falsee
l = '½'
print(l.isnumeric())
# output will be: True

#isspace() will check if all the characters in the text are whitespaces and will return True if that is the case otherwise will return False
m = " a "
print(m.isspace())
# output will be: False

#istitle() will check if all the characters in the text start with a capital will return True if that is the case otherwise will return False
n = "Hello All"
print(n.istitle())
# output will be: True

#isupper() will check if all the characters in the string as uppercase and if that is the case otherwise will return False
n = "Hello All"
print(n.istitle())
# output will be: False

# Joins all items in a type into a string, and you can choose a seperator
o =  ("a","b","c")
print(" ".join(o))
# output will be: a b c

# Lower() will change the string into all lowercase
p = "HEllo"
print(p.lower())
# output will be: hello

# lstrip() starts from the left hand side and will remove all the characters of the character you specify until it reaches a different character
q = "....a.."
print(q.lstrip('.'))
# output will be: a..

# replace() will replace a specified value with a different value, if the value appears more than once you can choose for how many occurrences it should be replaced for
q = "....a.."
print(q.replace('.','-',4))
# output will be: ----a..

# rsplit() will split a string into a list, you have to specify what the seperator is
r = "a.b.c"
print(r.rsplit("."))
# output will be:['a', 'b', 'c']

# rstrip() starts from the right hand side and will remove all the characters of the character you specify until it reaches a different character
q = "....a.."
print(q.rstrip('.'))
# output will be: ....a

# split() will split a string into a list, where each word in the string is now an item in the list
s = "hello world"
print(s.split())
# output will be: ['hello', 'world']

# splitlines() will split a string into a list, where each line in the string is now an item in the list
s = "hello\nworld"
print(s.splitlines())
# output will be: ['hello', 'world']

# startswith() will check if a string ends with the specified prefix and return True or False depending on if it matches, True if it matches
e = 'hello'
print(e.startswith('lo'))
# # output will be False

# strip() looks at both the right and left hand sides and will remove all the characters of the character you specify until it reaches a different character
q = "....a.."
print(q.strip('.'))
# output will be: a

# swapcase() will make all the upper case letters, lower case and then all the lower case letters upper case
t = "HeLLo"
print(t.swapcase())
# output will be: hEllO

# Title() will make the first letter in each word in the string upper case
u = "hello world"
print(u.title())
# output will be: Hello World

# Upper() will return the string and make all the characters upper case
u = "hello world"
print(u.upper())
# output will be: HELLO WORLD

# 3. List methods
# append() will add an item to the end of a list
list = ['a','b','c']
list.append('d')
print(list)
# output will be: ['a', 'b', 'c', 'd']

# clear() will empty a list, so therefore no value is returned
list = ['a','b','c']
list.clear()
print(list)
# output will be: []

# copy() will empty a list, so therefore no value is returned
list = ['a','b','c']
newlist = list.copy()
print(newlist)
# output will be: ['a', 'b', 'c']

# count() method returns the number of times the specified element appears in the list.
list = ['a','b','c']
count = list.count('a')
print(count)
# output will be: 1

# extend() method adds all the elements of an interable (list, tuple etc) to the end of the list
list = ['a','b','c']
extension = ['d','e','f']
list.extend(extension)
print(list)
# output will be: ['a', 'b', 'c', 'd', 'e', 'f']

# index() returns the index of a specified element in a list
list = ['a','b','c']
index = list.index('c')
print(index)
# output will be: 2

# insert() will insert an element into a list at a specified index
list = ['a','b','c']
list.insert(3,'d')
print(list)
# output will be: ['a', 'b', 'c', 'd']

# pop() will remove an element at the given index
list.pop(3)
print(list)
# output will be:['a', 'b', 'c']

# remove() will remove the first matching element, of the element passed through remove()
list.remove('a')
print(list)
# output will be: ['b', 'c']

# reverse() will reverses the elements in the list
list.reverse()
print(list)
# output will be: ['c', 'b']

# sort() will sort the list, the default is ascending but you can specify how to sort with a key=
list.sort()
print(list)
# output will be: ['b', 'c']

# reverse() will reverses the elements in the list
list.reverse()
print(list)
# output will be: ['c', 'b']

#4. Tuple methods
#count() will count the number of times a given element is in a tuple
x = (1,2,1,2,1)
print(x.count(1))
# output will be: 3

#index() will return the index of a specified element in the typle
x = (1,2,1,2,1,3)
print(x.index(3))
# output will be: 5

#5. Dictionary methods
#clear() will remove all the items from a dictionary
y = {1:"hello",2:"world"}
print(y)
y.clear()
print(y)
# output when cleared will be {}

#copy() will remove all the items from a dictionary
y = {1:"hello",2:"world"}
ynew = y.copy()
print(ynew)
# output when cleared will be {1: 'hello', 2: 'world'}

#fromkeys() will create a new dictonary from a given sequence of elements, there is an option of a value with can be set to each element of the dictionary
keys = {'apple','pear','orange'}
value = 'fruit'
newdict = dict.fromkeys(keys,value)
print(newdict)
# output when cleared will be {'pear': 'fruit', 'apple': 'fruit', 'orange': 'fruit'}

#keys() returns a view object of all the keys in a dictionary as a list
print(newdict.keys())
# output when cleared will be: (['orange', 'pear', 'apple'])

#pop() will remove and then return an element from a dictionary which has the key given
print(newdict.pop('pear'))
print(newdict)
# output when cleared will be: fruit and the new dictionary will be: {'orange': 'fruit', 'apple': 'fruit'}

#popitem() removes the item that was last inserted into the dictionary
print(y.popitem())
# (2, 'world')

#setdefault() will return the value of the item with the specified key, if they key doesn't exist it will insert it into the dictionary
y = {1:"hello",2:"world"}
y.setdefault(3,'!')
print(y)
# output for the dictionary will now be: {1: 'hello', 2: 'world', '3': '!'} and the set default couldn't find the key 3 so inserted it in

#update() will add an element to the dictionary if the key is not in the dictionary, if the key is in the dictionary it will update it
ynew = {3:'.'}
y.update(ynew)
print(y)
# output for the dictionary is now {1: 'hello', 2: 'world', 3: '.'}

#values() will give a view object that displays a list of all the values in a dictionary
print(y.values())
# output will be: dict_values(['hello', 'world', '.'])

#6. Set methods
#add() will add an element to a set if the element isn't in the set already
set = {'a','b','c'}
set.add('d')
print(set)
# output will be: {'a', 'b', 'c', 'd'}

#clear() method removes all the items from a dictionary
set.clear()
print(set)
# output will be: set() as the set is empty

#copy() method will copy the dictionary
set = {'a','b','c'}
newset = set.copy()
print(newset)
# output will be:{'a', 'b', 'c'}

#difference() method will return the different of new sets
set = {'a','b','d'}
print(set.difference(newset))
# output will be: {'d'}

#intersection() method will return the items that exist within two sets
print(set.intersection(newset))
# output will be: {'b', 'a'}

#issubset() method will return True if all the elements of one set is in the other.
print(set.issubset(newset))
# output will be: False. Here we are checking if set is a subset of the newset

#issuperset() method will return True if a set has every element of another set that is passed through
print(set.issuperset(newset))
# output will be: False. Here we are checking if set is a superset of newset, i.e set has a,b and d which it doesn't

#pop() method will remove a random item in a set.
print(newset.pop())
# output will be dependent on which element it chooses to remove but will either be a, b or c and then the set will be left with only two of a, b or c

#remove() method will remove a specified element in a set
set.remove('a')
print(set)
# output will be {'b', 'd'}

#symmetric_difference() will return the symmetric difference of two sets, this means elements that are not present in both sets
set = {'a','b','c'}
newset = {'c','d','e'}
print(newset.symmetric_difference(set))
# output will be {'a', 'd', 'b', 'e'} (as 'c' features in both sets)

#union() returns the elements that feature in both sets specified, but will duplicate if they appear more than twice across both sets
print(newset.union(set))
# output will be {'c', 'e', 'b', 'd', 'a'} (so 'c' won't appear twice as duplicates are excluded)

#update() will update the set with items from other iterables (e.g another set, a list)
a = [1,2,3]
set.update(a)
print(set)
# output will be {1, 'a', 2, 3, 'c', 'b'}

#7.File methods
# read() will return the number of bytes from a given file, by default it will read the whole file, however you can specify how many bytes
#print(examplefile.read())
# output will be what is in the file

# readline() will read the first line of the file
#sat the first line of an example txt file is Hello world
#print(examplefile.readline())
# output will be Hello world

# readlines() will read all the lines in a list, where each line is an item in the list for example if the first two lines were
#Hello
#World
#print(examplefile.readlines())
# output will be ['Hello','World']

# write()allows you to add some text to either, depending on how you opened the file this will be at the end if you specify "a" when you used open()or specifying "w" will remove all the orginal context when opened and what you are writing will be the first line of the file
#print(examplefile("\nHello World")) will start a new line and write Hello World


# writelines() will add a list of texts to a file, the same 'a' or 'w' applies depending on how you opened the file
