
file = open('input.txt', 'r')
entries = file.readlines()
total = 0
digits = []

d = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

for e in entries:
    alpha_digit = ""
    for char in e:
        if char.isnumeric():
            digits.append(char)
        else:
            alpha_digit += char
        
        for key in list(d.keys()):
            if key in alpha_digit:
                digits.append(d[key])
                alpha_digit = ""
                break

    total += int(digits[0] + digits[-1])
    digits.clear()


print(total)
