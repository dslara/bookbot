from stats import get_book_word_count, character_count, sort_dic
from sys import argv, exit

if len(argv) != 2:
  print("Usage: python3 main.py <path_to_book>")
  exit(1)

def main():
  file = argv[1]
  text = get_book_text(file)
  num_words = get_book_word_count(text)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  dic = character_count(text)
  sort_dic(dic)

def get_book_text(pathfile):
  with open(pathfile) as f:
    return f.read()
  
main()