# -*- coding: utf-8 -*-
import random


def word_picker(arg, val=100):
    word = ''
    P = random.randint(0, 100)
    if P <= val:
        word = arg[random.randint(0, len(arg) - 1)]
    else:
        word = None
    return word


def sentence_generator(syugo, jutsugo, mokutekigo, keiyoshi, fukushi, jodoshi):
    sohseki = ''
    if syugo is not None:
        sohseki += syugo[5][:-1] + u'[は/が]'
    if fukushi is not None:
        sohseki += fukushi[5][:-1]
    if keiyoshi is not None:
        sohseki += keiyoshi[5][:-1]
        sohseki += mokutekigo[5][:-1]
    if mokutekigo is not None:
        sohseki += mokutekigo[5][:-1] + u'[を/に]'
    sohseki += jutsugo[0]
    if u'連用' in jutsugo[4]:
        if jodoshi is not None:
            sohseki += jodoshi[5][:-1]
        else:
            sohseki += u'、'
    elif (syugo is None) and u'連体' in jutsugo[4]:
        sohseki += u'-'
    elif u'仮定' in jutsugo[4]:
        sohseki += u'ば'
    else:
        sohseki += u'。'
        sohseki += '\n'
    return sohseki


def sohseki(sub, tai, ju, ry, rt, aux):
    sohseki = ''
    while True:
        s, m, j, f, k, jo = '', '', '', '', '', ''
        s = word_picker(sub, 60)
        m = word_picker(tai)
        j = word_picker(ju)
        f = word_picker(ry, len(ry) // len(ju))
        k = word_picker(rt, len(rt) // len(ju))
        jo = word_picker(aux, len(aux) // len(ju))
        sohseki += sentence_generator(s, j, m, k, f, jo)
        if sohseki[-1:] == '\n':
            break

    return sohseki

while True:
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
    print(sohseki(subjective, tai, jutsu, renyo, rentai, jo))
    input()
