from enum import Enum
class CharType(Enum):
    LETTER = 1
    DIGIT = 2
    SYMBOL = 3

def checkCharType(c):
    if c.isalpha():
        return CharType.LETTER
    elif c.isdigit():
        return CharType.DIGIT
    else:
        return CharType.SYMBOL

# Rekursiv hjälpfuktion som tokenizar ord utan mellanslag
# Input: En sträng utan blanksteg
# Otput: En lista med strängar där varje sträng endast innehåller en typ av tecken
def tokenizeWord(word):
    tokenType = checkCharType(word[0])
    token = [""]

    if (len(word) > 1) and (tokenType == CharType.SYMBOL):
        return [word[0]] + tokenizeWord(word[1:])

    i = 0
    while i < len(word):
        if checkCharType(word[i]) == tokenType:
            token[0] += word[i].lower()
        else:
            return token + tokenizeWord(word[i:])
        i += 1
    return token

# print(tokenizeWord("Abc.DEF")) --> ['abc', '.', 'def']
# print(tokenizeWord("abc123def"))
# print(tokenizeWord("abcdef1"))
# print(tokenizeWord("abc...def1")) # --> ['abc', '.', '.', '.', 'def', '1']

# Input: En lista med text från docs
# Output: Samma lista som har "tokenizats" dvs delats upp i tokens
def tokenize(lines):
    tokens = []
    for line in lines:
        for word in line.split():
            tokens += tokenizeWord(word)
    return tokens


# with open("examples/article1.txt") as document:
#     print(tokenize(document.read().split("\n")))

# Input 1: En lista med ord som ska räknas
# Input 2: En lista med ointressanta ord som ska ignoreras
# Output: En dictionary där orden är nycklar och värdena är frekvensen av ordet
def countWords(words, stopwords):
    temp_dic = {}

    for word in words:
        if not word in stopwords:
            if not word in temp_dic: # Checka om vi har sett ordet innan, om inte lägg till i dictionary
                temp_dic.update({str(word): 1})
            else: # Annars om vi har sett ordet, inkrementera countern
                temp_dic[str(word)] += 1 

    return temp_dic


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

  if len(frequencies) == 0:
     return

  for i in range(n):
    try:
        print(word_list[i].ljust(20), str(frequencies[word_list[i]]).rjust(4))
    except Exception as e:     # word_list is empety or i is out of range for word_list. 
       print(e)
       return