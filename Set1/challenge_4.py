import os
from challenge_3 import single_byte_decode
from challenge_3 import string_scoring


def single_byte_decode_file(fileIN):
    with open('../Files/' + fileIN, "r") as f:
        first_pass = []
        i = 0
        for line in f:
            i += 1
            byte_decode = (i,) + single_byte_decode(line)
            first_pass.extend(byte_decode)
        decoded_string_pos = 0
        top_score = 10000
        best_guess = decoded_string_out = ''
        for line_number, decode_letter,  decode_string, decode_score in zip(first_pass[0::4], first_pass[1::4],
                                                                            first_pass[2::4], first_pass[3::4]):
            score = decode_score
            if score <= top_score:
                top_score = score
                best_guess = decode_letter
                decoded_string_pos = line_number
                decoded_string_out = decode_string
        return (decoded_string_pos, best_guess, decoded_string_out, top_score)


best_decode = single_byte_decode_file("encripted_text.txt")
print(best_decode)

