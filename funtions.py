#def name_of_funtion():
  #block of code

def say_happy_birthday():
  print('happy birthday')

say_happy_birthday()

def square_of_7():
  return 7**2

result = square_of_7()
print('result is', result)

def square(num):
  return num * num

print('square', square(8))

def add(a, b):
  return a + b

print('add', add(1, 2))
print('add with keywork arguments', add(b=2, a=1))

def exponent(num, power=2): #power defaults to square
  return num ** power

print(exponent(3)) #9

#functions have their own scope
#variables defined in functions cannot be accessed outside functions
#global variables can only be accessed inside functions when specifically referenced, ex:
total = 0
def incremental():
  global total #this line is necessary otherwise an error is thrown
  total += 1
  return total

def outer():
  count = 0
  def inner():
    nonlocal count #this line is necessary otherwise an error is thrown
    count += 1
    return count
  return inner()

#all python functions can be formally documented with """[documentation"""
def say_hello():
  """A simple function that returns the string hello"""
  return "hello"

print('say_hello documentation:', say_hello.__doc__)

# *args makes this and following arguments part of a tuple args
# args can be anything, just needs the * in front
def sum_all_nums(*args):
  total = 0
  for num in args:
    total += num
  return total

print('sum_all_nums:', sum_all_nums(1, 2, 3, 4, 5))

# **kwargs - key word args, stores rest of arguments as a dictionary
def fav_colors(**kwargs):
  print(kwargs)

fav_colors(steven='green', joe='blue')

# ordering parameters
# 1. parameters
# 2. *args
# default parameters
# **kwargs
def display_info(a, b, *args, first_name='Steven', **kwargs):
  return [a, b, args, first_name, kwargs]

print(display_info(1, 2, 3, last_name='Talafous', job='Salesperson'))
# a - 1
# b - 2
# args - (3,) ##tuple
# first_name - Steven
# kwargs - {'last_name': 'Talafous, 'job': 'Salesperson'}

#tuple unpacking (similar to spread operator in js)
def sum_all_values(*args):
  total = 0
  for num in args:
    total += num
  print(total)

nums = (1, 2, 3, 4, 5)
sum_all_values(*nums) #unpack with *[tuple]

#dictionary unpacking
def display_names(first, second):
  print(f"{first} says hello to {second}")

names = {'first': 'Steven', 'second': 'Joe'}
display_names(**names) #unpack with **[dictionary]