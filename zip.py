#zip
#zip returns an iterator that combines multiple iterables into one sequence of tuples. 
#Each tuple contains the elements in that position from all the iterables.
alphabets = ['a', 'b', 'c']
numbers = [1, 2, 3]
print(zip(alphabets, numbers))
print(list(zip(alphabets, numbers)))
#Like we did for range() we need to convert it to a list 
#or iterate through it with a loop to see the elements.

#unpack "tuples"
for alpha, num in zip(alphabets, numbers):
  print(alpha, num) 
# Print() note --> 
# https://extenshu.com/2017/09/24/python%E5%88%9D%E5%AD%B8%E9%87%8D%E9%BB%9E-04-%E8%81%8A%E8%81%8Aprint/

#unzip a list into tuples --> use asterisk *
some_list = [('A', 1, .1), ('B', 2, True), ('C', 3, False)]
letters, nums, items = zip(*some_list)
print(letters)
print(nums)
print(items)
print(letters, nums, items)

#enumerate
#enumerate is a function that returns an iterator of tuples 
#containing "indices" and "values" of a list.
letters = ['a', 'b', 'c', 'd', 'e']
print(enumerate(letters)) #same, need to use "list" to express
print(list(enumerate(letters)))
for i, letter in enumerate(letters):
    print(i, letter)

