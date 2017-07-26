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


