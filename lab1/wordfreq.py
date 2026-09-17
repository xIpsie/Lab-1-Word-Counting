# Input: En lista med text från docs
# Output: Samma lista som har "tokenizats" dvs delats upp i tokens
def tokenize(lines):
    pass
    # with open('examples/article1.txt', 'r', encoding='utf-8') as f:
    #     content = f.read()
    #     print(content)


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