import os
import csv
import math
from challenge_2 import hexXor

def hex_to_string(hexIn):
    try:
        string = str(bytes.fromhex(hexIn), 'utf-8')
    except:
        string = ' '
    return string

def string_scoring(string_in):
    with open('../Files/scrabble_scores.csv', 'r') as f:
        reader = csv.reader(f)
        scrabble_scores = list(reader)
    letter_score = 0
    for c in string_in:
        point = 0
        for sub_ss in scrabble_scores:
            if sub_ss[0] == c:
                point = float(sub_ss[1])
            elif 32 < ord(c) < 97:
                point = -10
            elif ord(c) == 32:
                point = 15
        letter_score += point
    score = letter_score
    return (score)

def single_byte_decode(encodeIn):
    best_string = best_guess = ""
    top_score = -10000
    for i in range(97, 122):  # 122
        string_out = ""
        for letter1, letter2 in zip(encodeIn[0::2], encodeIn[1::2]):
            i_hex = hex(i)[2:]
            xorRes = hexXor(i_hex, letter1 + letter2)
            xorResChr = hex_to_string(xorRes)
            string_out += xorResChr
        score = string_scoring(string_out.lower())
        if score > top_score:
            top_score = score
            best_guess = i
            best_string = string_out
    return (chr(best_guess), best_string.lower())


encode_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    # encode_hex = '2cee2b355233292b595d1c69592f483b54584f7154fd4928560752e333a1'
print(single_byte_decode(encode_hex))