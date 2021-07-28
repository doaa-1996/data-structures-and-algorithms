def left_join(map_a, map_b):
  
  output = []

  for word in map_a:
    if map_b.__contains__(word):
       antonym = map_b.get(word)
       synonym = map_a[word]
       output.append([word, synonym, antonym])
  
  print(output)
  return output

if __name__ == "__main__":
    lst1 = ['fond', 'wrath', 'diligent', 'outfit', 'guide']
    lst2 = ['enamored', 'anger', 'employed', 'garb', 'usher']
    lst3 = ['fond', 'wrath', 'diligent', 'guide', 'flow']
    lst4 = ['averse', 'delight', 'idle', 'follow','jam']

   
    map_a = dict(zip(lst1, lst2))

    map_b = dict(zip(lst3, lst4))
    # print(map_a)
    # print(map_b)
    left_join(map_a, map_b)
