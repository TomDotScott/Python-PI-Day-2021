def construct_array(fileName):
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


def greatest_common_denominator(a, b):
    if b > a:
        b, a = a, b
    remainder = a % b
    if remainder == 0:
        return b
    else:
        return greatest_common_denominator(b, remainder)


print(greatest_common_denominator(252, 105))
