
file = open("input.txt", "r")
lines = file.readlines()
tot = 0

for line in lines:
    games = line.split(";")
    id = games[0][5]
    games[0] = games[0].split(":")[1]
    p = True

    for game in games:
        picks = game.split(",")
        for pick in picks:
            a = pick.split(" ")
            num = int(a[1])
            color = a[2]

            if (color == "green" and num > 13) or (color == "red" and num > 12) or (color == "blue" and num > 14):
                p = False

    if p:
        tot += int(id)

print(tot)


