#data structure
# 1. List (ordered, mutable)
# 2. Tuple (ordered) --> Like immutable list
# 3. Set (mutable) --> unordered collection of "unique" objects
# 4. Dictionary (mutable, but keys are immutable)

#list
months = ['jan','feb','march','april']
months[3] = 'sfjlkj'
print(months)
print('april' in months)

#equality vs. identity
print('\n')
a = [1, 2, 3, 4, 5]
b = a     #point to the same list in memory
c = a[:]  #copy --> create and a new list 
d = [1, 2, 3, 4, 5]
# a and c point to two different objects
# they aren't identical objects.
print(a == b)
print(a is b)
print(a == c)
print(a is c)
print(a == d)
print(a is d)

b[1] = 'Hi'
print('\n',a,b)
print(b[0:4:2]) #List slicing

#List methods: https://www.w3schools.com/python/python_ref_list.asp
#adding --> append/insert/extend
print('\n')
basket = [1, 2, 3, 4, 5]
new_list = basket.append(100) # "append" changes the list 'in place' --> do not return result 
print(new_list)
print(basket)
basket.insert(3, 3.5)
print(basket)
#removing --> pop/remove/clear
print('\n', basket.pop()) # "pop" changes the list and returns the item
basket.pop(0)
print(basket)
basket.pop(2)
print(basket)
print(basket.remove(5)) # "remove" changes the list 'in place' --> do not return result
print(basket)
print(basket.clear()) # "clear" changes the list 'in place' --> do not return result
print(basket)
#sort(method) v.s. sorted(function)
print('\n')
box = ['b', 'n', 'a', 'd', 'x', 'e']
print(sorted(box)) #sorted function created a new list
print(box)
print(box.sort()) # "sort" method changes the list 'in place' --> do not return result
print(box)
#reverse
box = ['b', 'n', 'a', 'd', 'x', 'e']
box.sort()
print(box.reverse())
print(box)
print(box[::-1]) #List slicing creates a new list
print(box)

#List unpacking
print('\n')
a, b, *c, d = range(1, 10) #creates a list 1 to 9
print(a, b, c, d)

#tuple
print('\n')
my_tuple = (1, 2, 3, 4, 5, 5, 5)
print(my_tuple[2:3])
print(my_tuple[1:4])
print(my_tuple.count(5)) # How many times '5' show up
print(my_tuple.index(5))
a, b, c, *others = (1, 2, 3, 4, 5, 5, 5)
print(a)
print(others) #will form a list

#set
print('\n')
list1 = [1,2,3,4,5,5,5]
set1 = set(list1)
print(set1)
print(len(set1))
set2 = {4,5,6,7}
print(set1.union(set2))#creat a new set --> print(set1 | set2)
print(set1.intersection(set2)) #creat a new set --> print(set1 & set2)
print(set1.isdisjoint(set2))
print(set1.difference(set2)) #create a new set
set1.discard(1)
print(set1)
set1.difference_update(set2)
print(set1)


#Dictionary: a group of unordered key-value pairs
#a data type that stores mappings of unique keys to values. 
print('\n')
elements = {
              'H2': 1, 
              'H2': "Hydrogen",  #key must be unique --> otherwise it will be overwrite
              'He': 2, 
              True: [6, 28748], 
              26: 'age', 
              (0.8, 3, 'sf'): "tuple"
}
print(elements['He'], elements[True])
print(elements[26], elements[(0.8, 3, 'sf')])
# keys need to be immutable data type --> hashable key
# so 'List' and 'set' cannot be a key
elements['Li'] = [3, 5.667] #Add new key to dict
elements['He'] = 4656 # keys are immutable, but values are mutable!
print(elements)

#Dictionary methods
# print(elements['Ne']). 會直接error//用get比較好
print(elements.get('Li'))
print(elements.get('Ne'))
print(elements.get('Mg', 20)) #if "Mg" doesn't exit, return 20
print('He' in elements)

#Methods applications for loop
print('\n')
user = {
  'name': 'Leo',
  'age': 25,
  'can_swim': True
} 
for item in user: # will only print keys == user.keys()
  print(item)
for item in user.items():
  print(item)
for item in user.values():
  print(item)
for key, value in user.items():
  print(key, value)

#identity operator
print('\n')
n = elements.get('hellooooooo')
print(n is None)
print(n is not None)
print("He" in elements) # or print("He" in elements.keys())
print("Hydrogen" in elements) #false
print("Hydrogen" in elements.values())

print('\n')
print(elements.items())
print(elements.pop((0.8, 3, 'sf')))
print(elements)
print(elements.popitem()) #randomly remove an item 
print(elements.update({26: 'Allen'}))
print(elements.update({27: 'Hunter'}))
print(elements)
elements.clear()
print(elements)

print('\n')
user = dict([(1,'one')])
print(user)


