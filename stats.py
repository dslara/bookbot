def get_book_word_count(text: str):
  return len(text.split())

def character_count(text: str):
  resum = {}
  for c in text:
    character = c.lower()
    if character in resum:
      resum[character] = resum[character] + 1
    else:
      resum[character] = 1
  return resum

def sort_on(items):
  return items["num"]

def sort_dic(dic):
  list = []
  for item in dic:
    list.append({ "char": item, "num": dic[item] })
  list.sort(reverse=True, key=sort_on)
  for item in list:
    if item["char"].isalpha():
      print(f"{item["char"]}: {item["num"]}")
