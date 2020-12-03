f = open("input.txt", "r")
a = f.readlines()

validpasswordCount = 0
invalidpasswordCount = 0


for line in a:
    counter = 0
    firstPosition = int(line.split(": ")[0].split(" ")[0].split("-")[0]) - 1
    secondPosition = int(line.split(": ")[0].split(" ")[0].split("-")[1]) - 1
    letter = line.split(": ")[0].split(" ")[1]
    psw = line.split(": ")[1]
    print(firstPosition, secondPosition)
    print(psw)
    print(letter)
    if (psw[firstPosition] == letter and psw[secondPosition] != letter) or (psw[firstPosition] != letter and psw[secondPosition] == letter):
        print("yes")
        validpasswordCount += 1
    else:
        invalidpasswordCount += 1

print(validpasswordCount)
print(invalidpasswordCount)
