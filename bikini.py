# This is my scratch pad/test script
import os
import sys
import math
sys.path.append(os.path.join(os.getcwd() + '\Set1'))

def hex_to_string(hexIn):
    try:
        string = str(bytes.fromhex(hexIn), 'utf-8')
    except:
        string = ' '
    return string
def equal_hexXor(str1, str2):
    a = bytes.fromhex(str1)
    b = bytes.fromhex(str2)
    aXORb = int.from_bytes(a, byteorder='big') ^ int.from_bytes(b, byteorder='big')
    return "%x" % aXORb
def hexXor(str1, str2):
    a_len = org_a_len = len(str1)
    b_len = org_b_len =len(str2)
    if a_len % 2 > 0:
        str1 = str1 + '0'
        a_len = len(str1)
    if b_len % 2 > 0:
        str2 = str2 + '0'
        b_len = len(str2)
    if a_len < b_len:
        str2_cut = str2[0:a_len]
        aXOR_out = equal_hexXor(str1, str2_cut)
        aXOR_out = aXOR_out[0: org_a_len]
    elif a_len > b_len:
        str1_cut = str1[0:b_len]
        aXOR_out = equal_hexXor(str1_cut, str2)
        aXOR_out = aXOR_out[0: org_b_len]
    else:
        aXOR_out = equal_hexXor(str1, str2)
    return aXOR_out
def single_byte_decode(encodeIn):
    best_string = best_guess = ""
    top_score = score = 0
    for i in range(97, 122):  # 122
        string_out = ""
        for letter1, letter2 in zip(encodeIn[0::2], encodeIn[1::2]):
            i_hex = hex(i)[2:]
            xorRes = hexXor(i_hex, letter1 + letter2)
            xorResChr = hex_to_string(xorRes)
            string_out += xorResChr
        score_char = sum(c.isalpha() for c in string_out)
        decode_string_split = string_out.lower().split()
        stoplist_in = open(os.path.join(os.getcwd() + "\Files" + "\stopword_list.txt"), 'rt').read().splitlines()
        meaningful_words = [w for w in decode_string_split if w in stoplist_in]
        score_words = len(meaningful_words)
        score = score_char * math.exp(score_words)
        if score > top_score:
            top_score = score
            best_guess = i
            best_string = string_out
    return (chr(best_guess), best_string.lower())

def single_byte_decode_file(fileIN):
    with open(os.path.join(os.getcwd() + "\Files" + "\stopword_list.txt"), 'rt') as b:
        stoplist_in = b.read().splitlines()
    with open(os.path.join(os.getcwd() + "\Files\\" + fileIN), "r") as f:
        first_pass = top_rows = []
        i = 0
        for line in f:
            i += 1
            byte_decode = (i,) + single_byte_decode(line)
            first_pass.extend(byte_decode)
        decoded_string_pos = top_score = 0
        best_guess = decoded_string_out = ''
        for line_number, decode_letter,  decode_string in zip(first_pass[0::3], first_pass[1::3], first_pass[2::3]):
            score_char = sum(c.isalpha() for c in decode_string)
            decode_string_split = decode_string.lower().split()
            meaningful_words = [w for w in decode_string_split if w in stoplist_in]
            score_words = len(meaningful_words)
            score = score_char * math.exp(score_words)
            if score > top_score:
                top_score = score
                best_guess = decode_letter
                decoded_string_pos = line_number
                decoded_string_out = decode_string
                #top_rows.extend(decoded_string_pos)
        print(decoded_string_pos, best_guess, decoded_string_out)
        return(first_pass)


best_decode = single_byte_decode_file("encripted_text.txt")











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

print(hex_to_string(input_hex))


