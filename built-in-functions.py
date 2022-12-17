# lambdas
# similar to anonymous functions in js
# single line

square = lambda num: num * num
add = lambda a,b: a+b
print(add(1, 2))

# map
nums = [2, 4, 6, 8, 10]
doubles = map(lambda x: x*2, nums) #outputs map obj
list(doubles) #now in original data structure

people = ["Steven", "Joe", "James"]
peeps = map(lambda name: name.upper(), people)
list(peeps)

#filter
nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums)) 

people = ["Steven", "Joe", "James"]
j_names = filter(lambda n: n[0]=='j', people)
list(j_names)

#can nest filter in map or vice versa
#list comprehension is more commonly used instead of the above functions

# any / all functions based on whether values are truthy or not
values = [True, False]
any(values) #True
all(values) #False

#generator expressions
#tldr - only use instead of list when output is not used again
#much less memory space
#same as list comprehension but without []

nums = [2, 4, 0]
nums.sort() #sorts original list
nums = [2, 4, 0]
sorted(nums) #outputs sorted list but does not alter original
sorted(nums, reverse=True) #decending order
#can also accept tuple

max(3, 67, 99) #99
min(3, 67, 99) #3
max('c', 'd', 'a') # 'd'

people = ["Steven", "Joe", "James"]
min(people, key=lambda n:len(n)) #Joe

reversed('hello') #outputs reversed iterator object
#usually for lists will just use .reverse()

abs(-1) #1
sum([1, 2, 3]) #6
sum([1, 2, 3], 10) #16
round(1.7) #2
round(1.72, 2) #1.7

#zip
first_zip = zip([1, 2, 3], [4, 5, 6])
#first_zip returns an iterator of tuples
list(first_zip) #[(1, 4), (2, 5), (3, 6)]
dict(first_zip) #{1: 4, 2: 5, 3: 6}