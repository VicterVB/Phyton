roman_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def roman_calculator(roman_numeral):
    result = 0
    prev_value = 0

    for symbol in reversed(roman_numeral):
        value = roman_numerals[symbol]

        if value < prev_value:
            result -= value
        else:
            result += value

        prev_value = value

    return result

# Voorbeelden
print(roman_calculator("VIII"))      # Output: 8
print(roman_calculator("IIX"))       # Output: 8
print(roman_calculator("IL"))        # Output: 49
print(roman_calculator("XXXXVIIII")) # Output: 49
print(roman_calculator("XLV"))       # Output: 45
print(roman_calculator("VL"))        # Output: 45
