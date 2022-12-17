# many modules are native to python, documented on docs.python.org
import random  # can say "as rand" or something to rename import
print(random.choice(['apple', 'banana', 'cherry']))

# could also do
# from random import choice
# print(choice(['apple', 'banana', 'cherry']))

# custom modules
# file1.py
# def fn():
# return 'do some stuff'

# file2.py
# import file1
# file1.fn #'do some stuff'

# external modules are posted on the python package index - pypi.python.org
# use pip to install external modules. as of python 3.4, it comes native
# to install package: python3 -m pip install NAME_OF_PACKAGE

# can run: autopep8 --in-place modules.py
# this cleans up file formatting

# __name__
# when run, every python file has a __name__ variable
# if the file is the main file being run, its value is __main__
def say_hi():
  print(f"My __name__ is {__name__}")
say_hi()

# python automatically executes code on import
# so if, say, you have a print() in an improt file, it runs the print on import
# to prevent this, can add to import file:
if __name__ == '__main__':
  #this code will only run
  #if the file is the main file
  print('__main__ file!')