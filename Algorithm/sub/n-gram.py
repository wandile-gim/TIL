from functools import reduce
from os import sep


text = 'hello'
# for i in range(len(text)-1):
#     print(text[i], text[i+1])

# two_gram = zip(text, text[1:])
# for i in two_gram:
#     print(i[0], i[1], sep='')

# for i in range(len(text)-2):
#     print(text[i], text[i+1], text[i+2], sep='')

# print(list(zip(*['hello', 'ello', 'llo'])))

# print(list(zip(*[text[i:] for i in range(3)])))
# # text = 'show me the money'
# # words = text.split()
# # print(list(zip(words, words[1:])))
# word = 'level'

# print(word == ''.join(reversed(word)))

# ho = True
# for i in range(len(word)//2):
#     if word[i] != word[-1-i]:
#         ho = False
#         break
# print(ho)


a = [5, 7, 8, 12, 2, 4, 0, 3, 9]
print([i for i in a if i > 5 and i < 10])
print(list(filter(lambda x: x > 5 and x < 10, a)))
a = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x+y, a))
