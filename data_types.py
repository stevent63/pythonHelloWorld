print('Hello world') #comment

a = 2 #dont need anything else to initialize variable
print(a)

#use lowercase underscore variables in python
bool_var = True #needs to be capitalized

num = 5 #int
num2 = 5.0 #float

#can add num + num2, will become float
#cannot add a + num, wont force same type

#can add var in string with f-string
print(f"here is a num {a}")

num_int = int(num2) #convert float to int. does not round, it floors
num_str = str(num) #converts to string
num_float = float(num) #converts to float

name = 'steven'

if name == 'steven':
  print('steven')
elif name == 'ecem':
  print('ecem')
else:
  print('no name')

#logical operators the same except
## == instead of ===
## not, and, or instead of ! && !!

a1 = [1, 2]
b1 = [1, 2]
a1 == b1 #true
a1 is b1 #false, only truthy if points to same value in memory

#loop interable object
for item_var in a1:
  print(item_var)

for number in range(1,3): #actually [1,3)
  print('range' + str(number))

for letter in 'steven':
  print(letter)

bool_var = True
while (bool_var): #can also set with logical operators
  bool_var = False
  break #can use this in any loop to exit (obv not needed here)

#range(7) gives your 0-6
#range(1,8) gives 1-7
#range(1,10,2) gives odds from 1-10
#range(7,0,-1) gives integers from 7-1

#need to express the range in the loop or in list
list(range(10))

items = ['one', 'two']
len(items) #2
items[1] #two
items[-1] #two
'one' in items #True
items.append('three') #add to end of list
items.extend(['four', 'six']) #concat list
items.insert(4,'five') #insert second parameter at index of first parameter
print(items[4])
print(items[5])
#items.clear() ##removes all items from list
#items.pop(1) ##removes 'two
#items.pop() ##empty parameter removes last item from list
#items.remove('one') ##removes the first instance of 'one', throws ValueError if not found
#items.index('one') returns index of first index
#items.index('searchItem', 3) returns index of first index after index 3
#items.index('searchItem', 3, 10) returns index of first index starting at index 3 and before 10
#items.count('one') returns the number of times 'one' is found
#items.reverse() reverses existing list in place

words = ['Coding', 'is', 'fun']
' '.join(words) #starting string is inserted between all list elements. Seems to be inverse of JS syntax..

#slicing
items[1:] #['two', ..., 'six']
print(items[1:])
items[-1:] #['one', ..., 'five']
items[:2] #['one', 'two']
items[2:4] #['three', 'four']
items[1::2] #start at index 1 and step by 2
items[::2] #start at index 0 and step by 2
items[1::-1] #start at index 1 and reverse withs step 1
items[:1:-1] #start at last index and reverse withs step 1

#reverse string or list
string = 'racecar1'
string[::-1]

#insert list in part of list
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list1[1:3] = list2 #[1, 'a', 'b', 'c', 2, 3]

#swap values
names = ['steven', 'ecem']
names[0], names[1] = names[1], names[0]
print(names)

#list comprehension
nums = [1, 2, 3, 4]
new_nums = [x*10 for x in nums]
print(new_nums)
evens = [num for num in nums if num % 2 == 0]
print(evens)
double_evens = [num*2 for num in nums if num % 2 == 0]

with_vowels = 'This is so much fun'
without_vowels = ''.join(char for char in with_vowels if char not in 'aeiou')
print(without_vowels)

#nested lists generally the same as 2d+ array in JS
nested_list = [[1, 2], [3, 4]]
#nested list comprehension
[[print(val) for val in l] for l in nested_list]

board = [[num for num in range(1,4)] for val in range(1,4)]
board = [['X' if num % 2 != 0 else 'O' for num in range(1,4)] for val in range(1,4)]
print(board)

#dictionaries
coder = {
  'name': 'Steven',
  'owns_dog': False,
  'hours_experience': 1000,
  42: 'the answer'
}
#another way to create/cast a dict
another_coder = dict(name = 'joe')

#access single value
print(coder['name'])

#loop through keys
for value in coder.keys():
  # print(value)
  value

#loop through values
for value in coder.values():
  # print(value)
  value

#loop through key/value pairs
for key,value in coder.items():
  print(key, value)

#check for key in dict
'name' in coder #returns True
'phone' in coder #returns False
#ex
if 'name' in coder:
  print('the name of the coder is', coder['name'])

#check for value in dict
'Steven' in coder.values() #True

#coder.clear() #clears dictionary
coder2 = coder.copy() #creates new copy, unique object in memory

#for fromkeys, python will iterate over the first param no matter the data type
{}.fromkeys(['name', 'email'], 'unknown') #sets keys from first param with all values from second param

coder['name'] #'Steven'
coder.get('name') #'Steven'
# coder['age'] #KeyError
coder.get('age') #None

coder.pop('owns_dog') #removes key/value pair from dictionary
#coder.popitem() #removes random key/value pair from dictionary

first = dict(a=1)
second = dict(b=2)
second.update(first) #{'a': 1, 'b':2 }

#dictionary comprehension
numbers = dict(first=1, second=2, third=3)
squared_numbers = { key: value ** 2 for key,value in numbers.items()}

#making a dictionary with comprehension
new_dict = {num: num ** 2 for num in [1, 2, 3]}

#tuples
# -ordered collection or grouping of items
# -immutable
numbers = (1, 2, 3, 4)
3 in numbers #True

#tuples can be used as keys in a dictionary, for example gps coordinates for named place
# (cannot use list as keys)
locations = {
  (35.6895, 39.6917): 'Tokyo',
  (40.7128, 74.0060): 'New York',
}
locations[(35.6895, 39.6917)] #Tokyo

for location in locations:
  print(location, locations[location])

t = (1, 2, 3, 3, 3)
t.index(1) #0
# t.index(5) #ValueError
t.index(3) #2 - returns first matching index

#sets
# -like formal mathematical sets
# -do not have duplicate values
# -elements in sets aren't ordered
# -cannot access items in a set by index
# -useful if you need to keep track of a collection of elements
# -...but don't care about ordering, keys or values and duplicates

s1 = {1, 4, 5}
s2 = set({1, 2, 3})

s3 = {1, 2, 2} #{1, 2}
s3.add(2) #{1, 2}
s3.add(3) #{1, 2, 3}
s3.remove(3) #{1, 2}
# s3.remove(4) #ValueError
s3.clear() #set()

#s1[0] #TypeError
4 in s1 #True
8 in s1 #False

#set math
math_students = {'Steven', 'Frank'}
bio_students = {'Joe', 'Frank'}
math_students | bio_students #{'Steven', 'Joe', 'Frank'}
math_students & bio_students #{'Frank'}

#set comprehension
{x**2 for x in range(10)}
{0, 1, 64, 4, 36, 9, 16, 49, 81, 25} #set
{x:x**2 for x in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81} #dictionary