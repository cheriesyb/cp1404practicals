output_file = open("numbers.txt", 'r')
number_1 = int(output_file.readline())
number_2 = int(output_file.readline())
print(number_1 + number_2)
output_file.close()


# extended activity

output_file = open("numbers.txt", 'r')
total = 0
for line in output_file:
    number = int(line)
    total += number
print(total)
output_file.close()
