#raise
def colorize(text, color):
  colors = ('red', 'blue', 'green')
  if type(color) is not str:
    raise TypeError('color must be instance of str')
  if type(text) is not str:
    raise TypeError('text must be instance of str')
  if color not in colors:
    raise ValueError('color is invalid color')
  print(f"Printed {text} in {color}")
#colorize(34, 'red')
colorize('hello', 'red')

#try except
try:
  foobar #line that throws error
except:
  print('there was an error')
else: #this is optional
  print('in the else') #runs when except does not
finally:
  print('in the finally') #runs no matter what
print('post error')

#can have named errors in except
def divide(a,b):
  try:
    return a/b
  except ZeroDivisionError as err: #as err is optional
    print('dont divide by zero')
    print('error message:', err)

print(divide(1,0))

#for unhandled errors, use PDB package.