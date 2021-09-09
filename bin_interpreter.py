#############################
#          IMPORTS          #
#############################

import re

##############################
#          FUNCTION          #
##############################


def bin(binary):
    pos = 0
    result = 0
    plus = 1
    while not_bin(binary) == 1:
        binary = input("Your text isn't binary, please enter binary code\n")
    while len(binary) != pos:
        if int(binary[pos]) == 1:
            result += plus
        plus *= 2
        pos += 1
    return result


def not_bin(text):
    if re.search(r"[^01]", text):
        return 1
    else:
        return 0
#########################
#          RUN          #
#########################


def Run():
    while True:
        code = input("Please enter binary code.\n")
        print(bin(code))
