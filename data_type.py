#data type
# 1. integer
# 2. floater
# 3. string --> immutable
# 4. boolean

#built-in functions:
#https://docs.python.org/3/library/functions.html

print(type(5.))
print(3 + 2.76)
print(int(342.35853))
print(.1 + .1 + .1 == .3)
age = 14
teen = not (age > 12 and age <20)
print(teen)
print(10//3)

#math function 
print("\n")
print(round(3.8))
print(abs(-68))
print(bin(6))
print(int('0b101', 2)) #base is binary, tansfer to int or decimal

#variable
print('\n')
print('''variable regulation:

1. Must start with lowercase or underscore

2. Can be letters, numbers, underscores (NO space)

3. Case sensitive

4. Don't overwrite keywords''')

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

#constants --> nice habbit: all CAPITALS
print('\n')
PI = 3.14
PYTHON = 'great'
print(len(PYTHON))

#string basic concept
print('\n')
object_length_1 = len("Leo_is_clever_and_handsome")
object_length_2 = len('I am good')
print(object_length_1)
print(object_length_2)
print(object_length_1/object_length_2)

long_string = '''
wow ~ you can really dace ~
wow ~ I can too!
'''
print(long_string)

#escape sequence
print('\n')
print('I think you\'re \'the guy.\'')
print("\tI think you're 'the guy.'\nI love you.")

#sting concatenation
print('\n')
first = 'Hello'
second = 'world!'
print(first + ' ' + second)
print(first*5)

#string method: 
#https://www.w3schools.com/python/python_ref_string.asp
print('\n')
yo = 'to be or not to be'
print(yo.replace('be', 'do'))
#method creates a new string, and computer removes it from memory after print().
print(yo.replace('be', 'do', 1))
print(yo) #watch out!!! string is immutable

print('\n')
new_str = 'You are so beautiful and sexy.\n #lover'
print(new_str, '\n')
print(new_str.split())
print(new_str.split(' ', 2))  #用space來做split,單引號或雙引號皆可
print(new_str.split("."))     #用period來做split
print(new_str.split("#")) 
print(new_str.split(None, 4)) #None預設為space,後面接maxsplit

print('\n')
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

myTuple = ("John", "Peter", "Vicky")
"#".join(myTuple) 
print(myTuple)
# "join" method creates a new item (an iterable)
# --> do not change the original tuple
print("-".join(myTuple))

myList = ["John", "Peter", "Vicky"]
"#".join(myList) 
print(myList)
# "join" method creates a new item (an iterable) 
# --> do not change the original list
print("#".join(myList))

space = ' '
print(space.join(myList))

#formatted string
print('\n')
name = 'Joe'
age = 33
print(f"Hi {name}. You are {age} years old.")
print('Hi {1}. You are {0} years old.'.format(name, age))
print('Hi {new_name}. You are {new_age} years old.'.format(new_name = 'Hulk', new_age = 60))

#string index
#str[start:stop:stepover]
gr = "hello_world"
     #0123456789

print(gr[1:9:2])
print(gr[:-1:3])
print(gr[::-1]) #reverse of the string
print('rld' in gr, 'lo' not in gr)

#boolean
print('\n')
print(bool(1), bool(0))
print(bool('False'))

#type conversion
print('\n')
born = input("What year were you born?")
print(type(born))
age = 2020 - int(born)
print(f"Your age is {age}.") 

#practice: password checker
username = input('username:')
password = input('password:')
password_length = len(password)
hidden_password = "*" * password_length

print(f'{username}, your password {hidden_password} is {password_length} letters long.') 
