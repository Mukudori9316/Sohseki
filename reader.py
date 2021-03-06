# coding: utf-8
from janome.tokenizer import Tokenizer

txt = ''
words = ''
with open('kokoro.txt', 'r', encoding='utf-8') as f:
    kokoro = list(f)

kokoro = kokoro[22:-14]

for n, i in enumerate(kokoro):
    if i != '\n':
        txt += i[:-1]
t = Tokenizer()
tokens = t.tokenize(txt)


for token in tokens:
    n1 = token.surface
    n2 = token.part_of_speech.split(',')[0]
    n3 = token.part_of_speech.split(',')[1]
    n4 = token.part_of_speech.split(',')[2]
    n5 = token.infl_form
    n6 = token.base_form
    if n2 != u'記号' and n3 != u'数':
        words += (n1 + ',' + n2 + ',' + n3 + ',' +
                  n4 + ',' + n5 + ',' + n6 + '\n')
f.close()
f = open('wlist.txt', 'w', encoding='utf-8')
f.write(words)
f.close()

txt = ''
words = ''
with open('wagahaiwa_nekodearu.txt', 'r', encoding='utf-8') as f:
    wagahaiwa_nekodearu = list(f)

wagahaiwa_nekodearu = wagahaiwa_nekodearu[22:-14]

for n, i in enumerate(wagahaiwa_nekodearu):
    if i != '\n':
        txt += i[:-1]
t = Tokenizer()
tokens = t.tokenize(txt)


for token in tokens:
    n1 = token.surface
    n2 = token.part_of_speech.split(',')[0]
    n3 = token.part_of_speech.split(',')[1]
    n4 = token.part_of_speech.split(',')[2]
    n5 = token.infl_form
    n6 = token.base_form
    if n2 != u'記号' and n3 != u'数':
        words += (n1 + ',' + n2 + ',' + n3 + ',' +
                  n4 + ',' + n5 + ',' + n6 + '\n')
f.close()
f = open('wlist.txt', 'a', encoding='utf-8')
f.write(words)
f.close()
