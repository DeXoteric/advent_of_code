import hashlib


def day_04_p1():
    secret_key = "iwrupvqb"
    number = 1
    while True:
        input_str = secret_key + str(number)
        hash_str = hashlib.md5(input_str.encode()).hexdigest()
        if hash_str[:5] == "00000":
            return number
        number += 1


print(day_04_p1())
