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