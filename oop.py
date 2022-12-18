#define a class
class User:
  active_users = 0
  def __init__(self, first): #automatically run when an instance is made
    # ^^self always needs to be the first argument
    self.name = first #self is similar to this in JS
    User.active_users += 1
    print(f'A new user {self.name} has been made.')
  def __repr__(self):
    return f'{self.name}'
  def logout(self):
    User.active_users -= 1
  def initial(self):
    return f'{self.name[0]}'
  @classmethod # @thing is called a decorator
  def display_active_users(cls):
    return f'There are currently {cls.active_users} active users'
  @classmethod
  def from_string(cls, first):
    return cls(first)

#create an instance of the class
user1 = User('Steven')
print(user1) #runs user1.__repr__
print(user1.initial())

user2 = User('Joe')
print(User.active_users)
user2.logout()
print(User.active_users)
print(User.display_active_users())

user3 = User.from_string('James')
print(User.display_active_users())

# dunder methods like __init__ as just for native python methods
# don't use them unless you're intentionally overwriting one
# for example, can overwrite __len__ to make len(instance) give the age of an instance of a User class

# "_function" object method name is a convention for a method intended for
# only internal use to that object's other methods

# "__function" will be translated to "._Class__function" when accessed externally
# purpose is to tie it to this particular class so not confused when inherited to child class

#inheritence
class Animal:
  cool = True

  def __init__(self, age):
    self.age = age

  def make_sound(self, sound):
    print(f'this animal says {sound}')
  
class Cat(Animal):
  def __init__(self, age, breed):
    super().__init__(age)
    self.breed = breed

cat = Cat(5, 'tiger')
print(cat.age)
print(cat.breed)
cat.make_sound('meow')

#property handling
class Human:
  def __init__(self, age):
    if age >= 0:
      self._age = age
    else:
      self._age = 0
  @property
  def age(self): #age is name refered to on [instance].age
    return self._age
  
  @age.setter
  def age(self, value):
    if value >= 0:
      self._age = value
    else:
      raise ValueError('age cannot be negative')

steven = Human(30)
print(steven.age)

#multiple inheritance is possible but not used often. can look up if needed..