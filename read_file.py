f = open('another_file.txt', 'w')
f.write('Hello World!')
f.close()

f = open('another_file.txt', 'a')
f.write(" How's going? I miss you so much.\nYou've changed so much.")
f.close()

f = open('another_file.txt')
file_data = f.read()
f.close()

print(file_data)

with open('another_file.txt') as char:
  print(char.read(3))
  print(char.read(8))
  print(char.read())


sep_lines = []
with open('another_file.txt') as f:
  for line in f:
    sep_lines.append(line)
print(sep_lines)

sep_lines = []
with open('another_file.txt') as f:
  for line in f:
    sep_lines.append(line.strip())
print(sep_lines)