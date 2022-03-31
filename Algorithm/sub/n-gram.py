from os import sep


text = 'hello'
# for i in range(len(text)-1):
#     print(text[i], text[i+1])

# two_gram = zip(text, text[1:])
# for i in two_gram:
#     print(i[0], i[1], sep='')

# for i in range(len(text)-2):
#     print(text[i], text[i+1], text[i+2], sep='')

print(list(zip(*['hello', 'ello', 'llo'])))
# text = 'show me the money'
# words = text.split()
# print(list(zip(words, words[1:])))
