def main():
    num_picks = int(input("How many quick Picks? "))
    for i in range(num_picks):
        get_picks()


def get_picks():
    import random
    picks = []
    for i in range(6):
        pick = random.randrange(1, 46)
        while pick in picks:
            pick = random.randrange(1, 46)
        picks.append(pick)
    picks = sorted(picks)
    for pick in picks[:-1]:
        print("{:>2} ".format(pick), end="")
    print(picks[-1])
main()