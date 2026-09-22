import sys
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

  sys.setrecursionlimit(len(frequencies))   # change recusion limit to the number of unique words in text ahead of sort()
  printTopMost(frequencies, n)



if __name__ == "__main__":
    main()