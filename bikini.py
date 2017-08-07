import csv
import math
import string


def string_scoring(string_in):
    with open('./Files/scrabble_scores.csv', 'r') as f:
        reader = csv.reader(f)
        scrabble_scores = list(reader)
    letter_score = 0
    rejected = False
    for c in string_in:
        point = 0
        if c.isalpha():
            for sub_ss in scrabble_scores:
                if sub_ss[0] == c:
                    point = float(sub_ss[1])
        letter_score += point
    letter_count = sum(c.isalpha() for c in string_in)
    space_count = sum(c.isspace() for c in string_in)
    number_count = sum(c.isnumeric() for c in string_in)
    unprintable_count = (len(repr(string_in))-2) - len(string_in)
    symbol_count = sum(c.isprintable() for c in string_in) - (letter_count+space_count+number_count)
    if number_count>1 or unprintable_count>0 or symbol_count>1:
        rejected = True
    expected_letter_score = letter_count*3
    expected_space_count = len(string_in)/5
    chi_square_letter = math.pow(letter_score - expected_letter_score, 2) / expected_letter_score
    chi_square_space = math.pow(space_count - expected_space_count, 2) / expected_space_count
    if rejected:
        score = 1000
    else:
        score = (chi_square_letter + chi_square_space)*(math.exp(symbol_count)+math.exp(unprintable_count))
    return (score)



print(string_scoring('yth ebwt cadcpzjs g2fdf \x11x}oab'))
print(string_scoring('ieeacdm gi y fcao k ze_dn el hkied'))
print(string_scoring('kfz wpef2qsvqbhxa u tvt  jo]sp'))
print(string_scoring('absolutely correct english words'))
print(string_scoring('cooking mc s like a pound of bacon'))



print(string_scoring('u rl+jpr $e\x10 v1b-!6 - 0q/~+ j '))
print(string_scoring('}puke\\so a vj-2w do by hqdo\\n3'))
print(string_scoring("w  {@iim%ed eetsagoa!t` {l' ui"))
print(string_scoring('u+)ex nsqhe/]puse7nr;rw;ouqeas'))
print(string_scoring('e ee e e e e e e e e e e e e e e e'))

stoplist_in = open('./Files/stopword_list.txt', 'rt').read().splitlines()
meaningful_words = [w for w in decode_string_split if w in stoplist_in]




##### handy functions #####
input_str = "the kid don't play"


def string_to_hex(strIn):
    hex_total = ''
    for i in input_str:
        hex_i = hex(ord(i))[2:]
        hex_total += hex_i
    return hex_total


print(string_to_hex(input_str))

input_hex = '746865206b696420646f6e277420706c6179'


def hex_to_string(hexIn):
    try:
        string = str(bytes.fromhex(hexIn), 'utf-8')
    except:
        string = ' '
    return string


print(hex_to_string('7a'))