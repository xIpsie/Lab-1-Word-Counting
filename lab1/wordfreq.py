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

# Input: En lista med text från docs
# Output: Samma lista som har "tokenizats" dvs delats upp i tokens
def tokenize(lines):
    tokens = []
    for line in lines:
        for word in line.split():
            start = 0
            end = 0
            while start < len(word):
                tokenType = checkCharType(word[start])
                token = ""
                while (end < len(word)) and checkCharType(word[end]) == tokenType:
                    token += word[end].lower()
                    end += 1

                
                tokens.append(token)
                start = end
    return tokens

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


# Sorts the words in frequencies using sorted() function, then prints the n first words in frequencies along with thier frequency. 
#
# Parameter: 
# frequencies: A dictionary with words and their frequencies. 
# n: Number of words the function should print. 
#
# Return: void
def printTopMost(frequencies, n):
  for i in sorted(frequencies.items(), key=lambda x: -x[1])[:n]:
     print(i[0].ljust(20), str(i[1]).rjust(4))