from Prac08.taxi import Taxi, SilverServiceTaxi

VALID_MENU_CHOICES = ['q', 'c', 'd']


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    menu(taxis)


def menu(taxi_list):
    menu_choice = ''
    taxi_choice = ''
    current_bill = 0
    while menu_choice != 'q':
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(">>> ")
        while menu_choice.lower() not in VALID_MENU_CHOICES:
            "Invalid menu choice"
            menu_choice = input(">>> ")
        if menu_choice == 'c':
            taxi_choice = choose_taxi(taxi_list)
        elif menu_choice == 'd':
            if taxi_choice == '':
                print("No taxi chosen")
            else:
                current_bill += drive_taxi(taxi_choice)
        print("Your bill to date is ${:.2f}".format(current_bill))
    print("Total trip cost is ${:.2f}".format(current_bill))
    print("Taxis are now:")
    for taxi in taxi_list:
        print("{} - {}".format(taxi_list.index(taxi), taxi))


def choose_taxi(taxi_list):
    print("Taxis available")
    for taxi in taxi_list:
        print("{} - {}".format(taxi_list.index(taxi), taxi))
    taxi_choice = taxi_list[int(input("Choose taxi: "))]
    return taxi_choice


def drive_taxi(taxi_choice):
    taxi_choice.start_fare()
    distance_to_drive = int(input("Drive how far? "))
    taxi_choice.drive(distance_to_drive)
    print("Yor limo trip cost you ${:.2f}".format(taxi_choice.get_fare()))
    return taxi_choice.get_fare()

main()
