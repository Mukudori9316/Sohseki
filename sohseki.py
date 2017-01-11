import random


def word_picker(arg, val=100):
    word = ''
    P = random.randint(0, 100)
    if P <= val:
        word = arg[random.randint(0, len(arg) - 1)]
    else:
        word = None
    return word


def sohseki(syugo, jutsugo, mokutekigo, keiyoshi, fukushi, jodoshi):
    sohseki = ''
    if syugo is not None:
        sohseki += syugo[5][:-1] + u'は'
    if fukushi is not None:
        sohseki += fukushi[5][:-1]
    if keiyoshi is not None:
        sohseki += keiyoshi[5][:-1]
        sohseki += mokutekigo[5][:-1]
    if mokutekigo is not None:
        sohseki += mokutekigo[5][:-1] + u'を'
    sohseki += jutsugo[0]
    if u'連用' in jutsugo[4]:
        if jodoshi is not None:
            sohseki += jodoshi[5][:-1]
        else:
            sohseki += u'、'
    elif (syugo is None) and u'連体' in jutsugo[4]:
        sohseki += u'、'
    else:
        sohseki += u'。'
    return sohseki


wlist = []
subjective, jutsu, rentai, tai, renyo, jo = [], [], [], [], [], []
n, v, adj, adv, aux = u'名詞', u'動詞', u'形容詞', u'副詞', u'助動詞'
f = list(open('wlist.txt', 'r', encoding='utf-8'))
for word in f:
    wi = word.split(',')
    wi = tuple(wi)
    wlist.append(wi)

for w in wlist:
    if (w[1] == n and
       (w[2] == u'代名詞' or w[2] == u'固有名詞' or w[2] == u'一般')):
            subjective.append(w)
    elif w[1] == (v or adj):
        jutsu.append(w)
    elif w[1] == adj:
        rentai.append(w)
    elif w[1] == n and w[2] != u'非自立':
        tai.append(w)
    elif w[1] == adv:
        renyo.append(w)
    elif w[1] == aux:
        jo.append(w)
s1 = word_picker(subjective, 60)
m1 = word_picker(tai)
j1 = word_picker(jutsu)
f1 = word_picker(renyo, 80)
k1 = word_picker(rentai, 50)
jo1 = word_picker(jo, 40)

print(sohseki(s1, j1, m1, k1, f1, jo1))
print(s1, m1, j1)
