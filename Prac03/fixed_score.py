def main():
    test_score = float(input("Enter score: "))
    test_result = get_result(test_score)
    print(test_result)


def get_result(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score > 90:
        result ="Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()