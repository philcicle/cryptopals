from challenge_3 import single_byte_decode




with open("../Files/encripted_text.txt", "r") as f:
    i = 0
    for line in f:
        i += 1
        if i == 2:
            break
        print(line)
        print(i, single_byte_decode(line))
        score = sum(c.isalpha() for c in string_out)

