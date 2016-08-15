try:
 numerator = int(input("Enter the numerator: "))
 denominator = int(input("Enter the denominator: "))
 fraction = numerator / denominator
except ValueError:  # Prints an error if the input is not an integer
 print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:  # Prints error when denominator is 0
 print("Cannot divide by zero!")
print("Finished.")