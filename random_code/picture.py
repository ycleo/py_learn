
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


for p_list in picture:
  i = 0
  image = ''
  while i < len(p_list):
    if p_list[i] == 0:
      image += " "
      i += 1
    else:
      image += "*"
      i += 1
  print(image)
