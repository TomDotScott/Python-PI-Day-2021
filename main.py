def constructArray(fileName):
    # Read the file
    file = open(fileName, 'r')
    millionDigits = file.readline()
    # split into array of 5 digit numbers
    numbers = []
    for i in range(0, len(millionDigits), 5):
        num = ""
        for j in range(5):
            num += millionDigits[i + j]
        numbers.append(int(num))
    file.close()
    return numbers


print(constructArray('randomDigits.txt'))