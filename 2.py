f = open("input.txt", "r")
a = f.readlines()

validpasswordCount = 0
invalidpasswordCount = 0
counter = 0

for line in a:
    counter = 0
    letterMin = int(line.split(": ")[0].split(" ")[0].split("-")[0])
    letterMax = int(line.split(": ")[0].split(" ")[0].split("-")[1])
    letter = line.split(": ")[0].split(" ")[1]
    print(letterMin, letterMax)
    psw = line.split(": ")[1]
    for x in psw:
        if x == letter:
            counter += 1
    print(counter)
    if (counter >= letterMin) and (counter <= letterMax):
        validpasswordCount += 1
    else:
        invalidpasswordCount += 1

print(validpasswordCount)
print(invalidpasswordCount)
