import csv
import math


def string_scoring(string_in):
    with open('./Files/scrabble_scores.csv', 'r') as f:
        reader = csv.reader(f)
        scrabble_scores = list(reader)
    letter_score = 0
    for c in string_in:
        point = 0
        for sub_ss in scrabble_scores:
            if sub_ss[0] == c:
                point = float(sub_ss[1])
            elif 32 < ord(c) < 97:
                point = -40
            elif ord(c) == 32:
                point = 20
        letter_score += point
    decode_string_split = string_in.lower().split()
    stoplist_in = open('./Files/stopword_list.txt', 'rt').read().splitlines()
    meaningful_words = [w for w in decode_string_split if w in stoplist_in]
    score_words = len(decode_string_split) / len(string_in)
    #score_words = (len(meaningful_words) +1 )*len(decode_string_split)
    score =  score_words * (letter_score/len(string_in))
    score = max(score, 0)
    return (score)


print(string_scoring('u rl+jpr $e\x10 v1b-!6 - 0q/~+ j '))
print(string_scoring('}puke\\so a vj-2w do by hqdo\\n3'))
print(string_scoring('cooking mc s like a pound of bac'))
print(string_scoring('absolutely correct english boobs'))
print(string_scoring("w  {@iim%ed eetsagoa!t` {l' ui"))
print(string_scoring('u+)ex nsqhe/]puse7nr;rw;ouqeas'))
print(string_scoring('yth ebwt cadcpzjs g2fdf \x11x}oab'))
print(string_scoring('ieeacdm gi y fcao k ze_dn el hkied'))
print(string_scoring('cooking mc s like a pound of bacon'))
print(string_scoring('e ee e e e e e e e e e e e e e e e'))

