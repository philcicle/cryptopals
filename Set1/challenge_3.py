from challenge_2 import hexXor

def hex_to_string(hexIn):
    try:
        string = str(bytes.fromhex(hexIn), 'utf-8')
    except:
        string = ' '
    return string

def single_byte_decode(encodeIn):
    best_string = best_guess = ""
    top_score = score = 0
    for i in range(97, 122): # 122
        string_out = ""
        for letter1, letter2 in zip(encodeIn[0::2], encodeIn[1::2]):
            i_hex = hex(i)[2:]
            xorRes = hexXor(i_hex, letter1 + letter2)
            xorResChr = hex_to_string(xorRes)
            string_out += xorResChr
        score = sum(c.isalpha() for c in string_out)
        if score > top_score:
            top_score = score
            best_guess = i
            best_string = string_out
    print(chr(best_guess), best_string)


encode_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

single_byte_decode(encode_hex)