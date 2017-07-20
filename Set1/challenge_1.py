import binascii
import base64


def convert_hex_to_base64(str_in):
    decoded = binascii.unhexlify(str_in.encode())
    ecoded_base64 = base64.b64encode(decoded)
    return ecoded_base64


input_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
output_str = convert_hex_to_base64(input_str)

print(output_str)



