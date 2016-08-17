lower = 10
upper = 100
print("Enter a number ({}-{}):".format(lower, upper))

for i in range(lower, upper):
    print("{:<3} {}".format(i, chr(i)))