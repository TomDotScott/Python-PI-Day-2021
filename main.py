# Read the file
file = open("randomDigits.txt", 'r')
millionDigits = file.readline()
# split into array of 5 digit numbers
numbers = []
for i in range(0, len(millionDigits), 5):
    num = ""
    for j in range(5):
        num += millionDigits[i + j]
    numbers.append(int(num))

print(numbers)