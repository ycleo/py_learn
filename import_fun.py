def mean(num_list):
  return sum(num_list) / len(num_list)

def add_five(num_list):
  return [n + 5 for n in num_list]

#1st method to avoid the excutable statement 
if __name__ == '__main__':
  print('Testing mean function')
  list_ex = [34, 44, 23, 46, 12, 24]
  correct_mean = 30.5
  assert mean(list_ex) == correct_mean

  print('Testing add_five function')
  correct_list = [39, 49, 28, 51, 17, 29]
  assert add_five(list_ex) == correct_list

  print('All tests passed!')

#2nd method 
def main():
  print('Another way!')

if __name__ == '__main__':
  main()