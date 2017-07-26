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

def hex_to_string(hexIn):
    try:
        string = str(bytes.fromhex(hexIn), 'utf-8')
    except:
        string = ' '
    return string

encode_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
best_string = best_guess = ""
top_score = score = 0
for i in range(97, 122): # 122
    string_out = ""
    for letter1, letter2 in zip(encode_hex[0::2], encode_hex[1::2]):
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



