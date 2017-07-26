import base64

def convert_hex_to_base64(hex_in):
    return base64.encodebytes(bytes.fromhex(hex_in))


input_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
output_str = convert_hex_to_base64(input_str)

print(output_str) #SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

