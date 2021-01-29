#Control Flow

#Conditional Statements
#Boolean Expressions
#For and While Loops
#Break and Continue
#Zip and Enumerate
#List Comprehensions

#for loops are ideal when the number of iterations is known or finite.
#while loops are ideal when the iterations need to continue until a condition is met.

# For loop
for _ in range(3, 11, 2):
  print(_)
for _ in range(2):
  print(list(range(9))) # a quick to create integers list

print('\n')
# wrong demonstration
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")
    print(name)

print(names)
print('\n')
#During each iteration, the name variable is set to a string taken from the list. 
#Then the assignment statement creates a new string (name.lower().replace(" ", "_")) 
#and changes the name variable to that string. 
#It doesn't modify the contents of the names list at all. 
#To modify the list you must operate on the list itself, using range

# 1. create a new list --> use append
usernames = []
for name in names:
    usernames.append(name.lower().replace(' ', '_'))

print(usernames)

# 2. modify the origional list --> use range
for index in range(len(names)):
    names[index] = names[index].lower().replace(' ', '_')

print(names)
print('\n')
# HTML application
items = ['first string', 'second string']
html_str = "<ul>\n"  

for item in items:
  html_str += '<li>{}</li>\n'.format(item)
html_str += '<ul>'
print(html_str)

#Quiz 1
print(list(range(0,-5)))
#Quiz 2
colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = []

for color in colors:
  lower_colors.append(color.lower())
print(lower_colors)

print('\n')
#dictionary application
#method 1
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)
#method 2
word_counter_2 = {}
for word in book_title:
  word_counter_2[word] = word_counter_2.get(word, 0) + 1
print(word_counter_2)

#items() application --> iterate through both keys and values
result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
for item, number in basket_items.items():
  if item in fruits:
    result +=  number
print(result)

print('\n')
#while loop
#nearest square
limit = 40
root = 0
while (root+1)**2 < limit:
  root += 1
nearest_square = root**2
print(nearest_square)

#Quiz: add up the odd numbers in the list, but only up to the first 5 odd numbers together. 
#If there are more than 5 odd numbers, you should stop at the fifth. 
#If there are fewer than 5 odd numbers, add all of the odd numbers.
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

#method 1 --> use for loop (less efficiency)
odd_sum = 0
count = 0
for num in num_list:
    if num % 2 == 1 and count < 5:
        count += 1
        odd_sum += num
print(odd_sum)

#method 2 --> use while loop (no need to go through the whole list)
odd_sum = 0
count = 0
i = 0
lenth = len(num_list)
while (count < 5) and (i < lenth):
  if num_list[i] % 2 == 1:
    count += 1
    odd_sum += num_list[i]
  i += 1
print ("The numbers of odd numbers added are: {}".format(count))
print ("The sum of the odd numbers added is: {}".format(odd_sum))

print('\n')
# Break and Continue
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
#method1 --> use break (wrong)
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("breaking loop now!")
        break
    else:
        print("adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("Final Weight: {}".format(weight))
print("Final Items: {} \n".format(items))

#method2 --> use continue
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
  print('current weight:{}'.format(weight))
  if (cargo_weight + weight) >= 100:
    print('skip')
    continue
  else:
    print('adding {} ({})'.format(cargo_name, cargo_weight))
    items.append(cargo_name)
    weight += cargo_weight
print("final weight = {}".format(weight))
print("final items = {}".format(items))

#Quiz
print('\n')
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System"]
news_ticker = ''

for sentence in headlines:
  news_ticker += sentence + ' '
  if len(news_ticker) >= 18:
    news_ticker = news_ticker[:18]
    break
print(news_ticker)

print('\n')
#List Comprehension
#We can create lists quickly and concisely with list comprehensions
cities = ['new york city', 'los angeles', 'taipei city', 'mountain view']
#original way
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())
print(capitalized_cities)
#use list comprehension
cap_cities = [city.title() for city in cities]
print(cap_cities)

squares = [x**2 for x in range(9) if x % 2 == 0]
#If like to add "else" 
#you have to move the conditionals to the beginning of the listcomp, right after the expression, 
squares2 = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares, squares2)
print('\n')


winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'], 1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'], 1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'], 1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'], 1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'], 1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'], 1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'], 1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'], 1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'], 1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'], 1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'], 1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'], 1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'], 1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'], 1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'], 1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'], 1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'], 1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}

### Question: Please provide a list with the name(s) of the director(s) with 
### the most Oscar wins. The list can hold the names of multiple directors,
### since there can be more than 1 director tied with the most Oscar wins.
wincount = {}
for year, namelist in winners.items():
  for winner in namelist:
    wincount[winner] = wincount.get(winner, 0) + 1

most_win_director = []
highest_win_time = max(wincount.values())
most_win_director = [winner for winner, count in wincount.items() if count == highest_win_time]
print(most_win_director)

