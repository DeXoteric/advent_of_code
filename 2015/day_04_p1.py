import hashlib


def find_hash_with_zeros():
    secret_key = "iwrupvqb"
    number = 1
    while True:
        input_str = secret_key + str(number)
        hash_str = hashlib.md5(input_str.encode()).hexdigest()
        if hash_str[:5] == "00000":
            return number
        number += 1


print(find_hash_with_zeros())
