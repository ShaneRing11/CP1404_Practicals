from Prac08.taxi import Taxi
from Prac08.taxi import UnreliableCar
from Prac08.taxi import SilverServiceTaxi

def main():
    """
    prius1 = Taxi("Prius 1", 100)
    prius1.drive(40)
    print("{}, current fair is ${:.2f}".format(prius1, prius1.get_fare()))
    prius1.start_fare()
    prius1.drive(100)
    print("{}, current fair is ${:.2f}".format(prius1, prius1.get_fare()))

    ford = UnreliableCar("Ford", 100, 50)
    for i in range(10):
        ford.drive(10)
        print(ford)
    """

    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.drive(10)
    print(hummer)
    print(hummer.get_fare())

main()

