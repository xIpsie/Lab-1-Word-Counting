# Input 1: Dictionary som sorteras baserat värdet. Störst till minst.
# Return: Sorterad dictionary. 
def sort(dict):
  if len(dict) <= 1:
    return dict
  else:
    partNum, partItem, part1, part2 = dict[next(iter(dict))], next(iter(dict)), {}, {}
    dict.pop(next(iter(dict)))

    for e in dict:
      if dict[e] > partNum:
        part1[e] = dict[e]
      else:
        part2[e] = dict[e]

    part1[partItem] = partNum
    return sort(part1) | (sort(part2))


# Input 1: En dictionary med ord och dess frekvenser
# Input 2: Hur många av de vanligaste orden som ska printas
def printTopMost(frequencies, n):
    frequencies = sort(frequencies)
    word_list = list(frequencies) 

    for i in range(n):
      print(word_list[i].ljust(10), frequencies[word_list[i]])