# higher order functions
# just like JS, can pass functions into other functions. nothing new there.

# decorators are functions
# they wrap other functions and enhance their behavior
# decorators are examples of higher order functions
# they have their own syntax, using @

def be_polite(fn):
  def wrapper():
    print('What a pleasure to meet you')
    fn()
    print('Have a great day')
  return wrapper

@be_polite
def greet():
  print('My name is Steven')

# the above three lines are the equivelent to
# greet = be_polite(greet)

# to accept multiple arguments, use *args and **kwargs
# in this case, the arguments passed to decorators are called signatures
def shout(fn):
  def wrapper(*args, **kwargs):
    return fn(*args, **kwargs).upper()
  return wrapper

@shout
def greet(name):
  return f"Hi, I'm {name}"

@shout
def order(main, side):
  return f"Hi, I'd like the {main} with a side of {side}"

print(greet('Steven'))
print(order('steak', 'potatos'))

# to preserve metadata of wrapped functions, can use this
from functools import wraps
def my_decorator(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    pass
  return wrapper

# example of useful wrapper function
from time import time
def speed_test(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    t0 = time()
    result = fn(*args, **kwargs)
    t1 = time()
    print(f'Time elapsed: {t1 - t0}')
    return result
  return wrapper

@speed_test
def sum_nums():
  return sum(x for x in range(100000000))

sum_nums()