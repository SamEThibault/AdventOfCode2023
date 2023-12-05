
file = open('input.txt', 'r')
entries = file.readlines()
total = 0
digits = []

for e in entries:
    for char in e:
        if char.isnumeric():
            digits.append(char)
    total += int(digits[0] + digits[-1])
    digits.clear()

print(total)
