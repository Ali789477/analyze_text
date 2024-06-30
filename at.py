text = input("Введите текст:")
text = text.lower()
punctuation = [".",",","?","!"]
for i in punctuation:
  text = text.replace(i , '')
BJ = text.split()
print("Кол-во значений",len(set(BJ)))
word_frequency = {}
for i in BJ:
  if i in word_frequency:
    word_frequency[i] += 1
  else:
    word_frequency[i] = 1
print(word_frequency)