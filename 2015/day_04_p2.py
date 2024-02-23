import hashlib


def day_04_p2():
    secret_key = "iwrupvqb"
    number = 1
    while True:
        input_str = secret_key + str(number)
        hash_str = hashlib.md5(input_str.encode()).hexdigest()
        if hash_str[:6] == "000000":
            return number
        number += 1


print(day_04_p2())
