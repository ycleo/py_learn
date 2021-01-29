#Defining Functions
#Variable Scope
#Documentation
#Lambda Expressions
#Iterators and Generators


how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""
print(snake_string * how_many_snakes)

name = input("enter your name: ")
print("What's up {}!".format(name))

num = int(float(input("Enter an integer: ")))
print("hello" * num)



num = eval(input('calculate: '))
print(num)
print('\n')

#quiz 1
names = input("names separated by commas: ").title().split(sep=',')
assignments = input("assignments left separated by commas: ").split(sep=',')
grades = input("current grade separated by commas: ").split(sep=',')

x = zip(names, assignments, grades)


for name, assign, grade in x:
  final = int(grade) + int(assign)*2
  print("Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n".format(name, assign, grade, final))

  #quiz 2
  while True:
  try:
    x = int(input('number: '))
    break
  except ValueError:
    print('invalid number')
  except TypeError:
    print('Type error')
  except KeyboardInterrupt:
    print('\nNO Interrupt')
  finally:
    print("good work!")
print('\n')

def party_planner(cookies, people):
    leftovers = None
    num_each = None
    # TODO: Add a try-except block here to
    #       make sure no ZeroDivisionError occurs.
  
    try:
        num_each = cookies // people
        leftovers = cookies % people
       
    except Exception as e:
        print("people cannot be 0")
        print("(Reason: {})".format(e))
    
    return(num_each, leftovers)
        
# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)
          
            
    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")
