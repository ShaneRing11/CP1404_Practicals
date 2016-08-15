number_file = open("numbers.txt", "r")
num_one = int(number_file.readline())
num_two = int(number_file.readline())
added = num_one + num_two
print(added)
number_file.close()