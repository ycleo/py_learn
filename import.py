import import_fun as fu

scores = [88, 92, 79, 93, 85]

mean = fu.mean(scores)
curved = fu.add_five(scores)

mean_c = fu.mean(curved)

print('Scores:', scores)
print('original mean:', mean, 'new mean:', mean_c)

print(__name__)
print(fu.__name__)