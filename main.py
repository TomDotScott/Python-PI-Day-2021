import math


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

    if b == 0:
        b = 1

    remainder = a % b

    if remainder == 0:
        return b
    else:
        return greatest_common_denominator(b, remainder)


numbersArray = construct_array('randomDigits.txt')
# Count through the array in pairs
totalNumbers = 0
coPrimeCount = 0
for i in range(0, len(numbersArray), 2):
    a = numbersArray[i]
    b = numbersArray[i + 1]
    gcd = greatest_common_denominator(a, b)
    # print(str(a) + ", " + str(b) + " = " + str(gcd))
    # If the gcd is 1, they are 'Co-Prime'
    if gcd == 1:
        coPrimeCount += 1

    totalNumbers += 1

# Find the ratio of co-primes to prime
ratio = coPrimeCount / totalNumbers
# P(CoPrime) = 6 / PI^2
# PI = root(6 / P(Co))
piEstimate = math.sqrt(6 / ratio)

# Work out % accuracy
print("PI = " + str(math.pi) +
      "\nEstimate = " + str(piEstimate) +
      "\n% accuracy = " + str(piEstimate / math.pi * 100) + " %"
      )
