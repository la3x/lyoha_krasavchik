import random

def gen_password(length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ''
    for i in range(length):
        password = password + random.choice(elements)
    return password


def monetka():
    coin = random.randint(0, 2)
    if coin == 0:
        return "Орёл"
    else:
        return "Решка"