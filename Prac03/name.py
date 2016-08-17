def main():
    valid_name = get_name()
    print_name(valid_name)


def print_name(name):
    for char in range(len(name)):
        if char % 2 > 0:
            print(name[char])


def get_name():
    name = input("Enter name: ")
    while len(name) < 1:
        print("You must enter a name!")
        name = input("Enter name: ")
    return name

main()