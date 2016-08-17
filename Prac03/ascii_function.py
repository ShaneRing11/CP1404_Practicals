def main():
    LOWER = 10
    UPPER = 50
    valid_num = get_number(LOWER, UPPER)
    print("{:<3} {}".format(valid_num, chr(valid_num)))


def get_number(lower, upper):
    valid_input = False
    while not valid_input:
        try:
            number = int(input("Enter a number ({}-{}): ".format(lower, upper)))
            while number < lower or number > upper:
                print("Please enter a valid number!")
                number = int(input("Enter a number ({}-{}): ".format(lower, upper)))
            valid_input = True
        except ValueError:
            print("Invalid (must be integer)")
    return number

main()
