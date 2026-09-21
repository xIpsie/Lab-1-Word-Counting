import sys
# Hårdkodad limit på hur många loops en rekursiv func kan köras för annars cappar på den 999 försök. Quicksort, som används i sort(), kommer köra rekursivt 1 gång per unikt ord i en text. Dvs. 1000 unika ord i en text = 1000 rekursiva lager i sort(). 
sys.setrecursionlimit(10000)
import urllib.request
from wordfreq import *


# Input: Inputten anges i command prompten t.ex. "py topmost.py eng_stopwords.txt examples/article1.txt 20"
# Där topmost.py --> sys.argv[0], eng_stopwords.txt --> sys.argv[1], examples/article1.txt --> sys.argv[2], 20 --> sys.argv[3]

# Output: printTopMost() printar ut de n mest frekventa ord och deras statistik
def main():
  # Checkar om input-texten är en hemsida eller en .txt
  if sys.argv[2][:7] == "http://" or sys.argv[2][:8] == "https://":
    response = urllib.request.urlopen(sys.argv[2])  
    raw_text = response.read().decode("utf8")
  else:
    with open(sys.argv[2], encoding="utf-8") as document:
      raw_text = document.read()

  stopwords_file, n = sys.argv[1], int(sys.argv[3]) 
  text = tokenize(raw_text.split("\n"))
    
  with open(stopwords_file, encoding="utf-8") as document:
    frequencies = countWords(text, document.read())

  printTopMost(frequencies, n)



if __name__ == "__main__":
    main()