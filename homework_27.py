# Exercise.1

import math

def sector_area(r, alpha_rad):
    alpha_deg = math.degrees(alpha_rad)
    area = (math.pi * r ** 2) * (alpha_deg / 360)
    print(f"Thw area: ՝ {area}")

sector_area(5, math.pi / 2)

# Exercise.2

def arabic_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100,  90,  50,  40,
        10,   9,   5,   4, 1
    ]
    syms = [
        "M",  "CM", "D", "CD",
        "C",  "XC", "L", "XL",
        "X",  "IX", "V", "IV", "I"
    ]
    roman = ""
    i = 0
    while num > 0:
        while num >= val[i]:
            roman += syms[i]
            num -= val[i]
        i += 1
    return roman

print(arabic_to_roman(15))
print(arabic_to_roman(72))
print(arabic_to_roman(9))

# Exercise.3

def filter_longest_words(words):
    max_len = max(len(word) for word in words)
    return [word for word in words if len(word) == max_len]

print(filter_longest_words(["aba", "aa", "z", "ad", "vcd", "aba"]))
print(filter_longest_words(["aba", "aa", "z", "advc", "vcd", "aba"]))