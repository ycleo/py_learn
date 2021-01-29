# Ternary Operator (conditional "expression") :
# an shortcut operation that evaluates to something based on the condition being true or false
# expression --> evaluates to a value
is_friend = True
can_message = "message allowed" if is_friend else 'not allowed to message'
print(can_message) 

#logical operator practice
is_magician = False
is_expert = True

if is_magician and is_expert:
  print("You're a master magicain!")
elif is_magician:
  print("At least you are getting there.")
else: 
  print('You need magic power.')

comment = "You're a master magicain!" if is_magician and is_expert else 'Keep going!'
print(comment)

