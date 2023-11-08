#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
           'C': 100, 'D': 500, 'M': 1000}
    s = roman_string
    if s is None or not isinstance(s, str):
        return 0

    for i in range(len(s)):
        if i + 1 < len(s) and rom[s[i]] < rom[s[i + 1]]:
            result -= rom[s[i]]
        else:
            result += rom[s[i]]

    return result
