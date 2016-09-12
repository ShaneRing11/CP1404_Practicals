from Prac07.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = "Placeholder"
    count = 0
    while name.isspace() == False:
        count += 1
        name = input("Name: ")
        year = int(input("Year: "))
        cost = int(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
    for guitar in guitars:
        print(guitar)

main()
