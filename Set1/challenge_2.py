
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

input_str = "1c0111001f010100061a024b53535009181c"
second_str = "686974207468652062756c6c277320657965"

print(hexXor(input_str, second_str)) # '746865206b696420646f6e277420706c6179'








