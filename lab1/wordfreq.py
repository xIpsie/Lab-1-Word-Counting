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