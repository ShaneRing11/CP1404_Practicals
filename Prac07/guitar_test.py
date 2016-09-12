from Prac07.guitar import Guitar

def main():
    new_guitar = Guitar("New guitar", 2015, 559)
    old_guitar = Guitar("Old guitar", 1942, 10792)
    guitars = [new_guitar, old_guitar]

    for guitar in guitars:
        print(guitar)
        print(guitar.is_vintage(guitar.year))

main()