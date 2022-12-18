# can only interate on an 'iterator object'
# to get that object..
name = 'Steven'
it = iter(name)

# can now iterate on 'it'
for char in it:
  print(char)

# above loop actually just calls next(it) until it hits a StopIteration error

# can define the iterator of any Class with __iter__

# generator functions are like 'return', except with 'yield' you can yield multiple times
# return returns a value, generators return a generator
def count_up_to(max):
  count = 1
  while count <= max:
    yield count
    count += 1

gen = count_up_to(5)
# can call next(gen) for each element
for num in gen:
  print(num)

# can convert list(gen) if you need to access any element more than once

#basically, generators are much much more memory efficient

# generator expressions use () instead of []
# an equivelent to count_up_to:
g = (num for num in range(1, 10))
for num in g:
  print(num)
# generator expressions are faster than list comprehensions