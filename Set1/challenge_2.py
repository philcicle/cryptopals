import binascii
import sys


def hexXor(str1, str2):
    a = binascii.unhexlify(str1.encode())
    b = binascii.unhexlify(str2.encode())
    if len(str1) == len(str2):
        aXORb = int.from_bytes(a, sys.byteorder) ^ int.from_bytes(b, sys.byteorder)
        aXORb_hex = binascii.hexlify(aXORb.to_bytes(len(a), sys.byteorder))
    else:
        print("Unequal length Hex input")
        aXORb_hex = "0x0000"

    return aXORb_hex


input_str = "1c0111001f010100061a024b53535009181c"
second_str = "686974207468652062756c6c277320657965"

print(hexXor(input_str, second_str))

