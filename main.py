# remove whitespace from the file
file = open("randomDigits.txt", 'r')
lines = file.readlines()
lines = [line.replace(' ', '') for line in lines]
lines = [line.replace('\n', '') for line in lines]
file.close()
file = open("randomDigits.txt", 'w')
file.writelines(lines)