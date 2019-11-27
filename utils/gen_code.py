import random
import string


def gen_code():
    a = random.sample(string.digits, 6)
    code = "".join(a)
    # print(code)
    return code


# for i in range(4):
#     print(gen_code())

