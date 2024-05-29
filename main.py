
input_string = input("Enter int numbers: ")


numbers = list(map(int, input_string.split()))

# Filtr
positive_numbers = [num for num in numbers if num > 0]

if positive_numbers:
    print("Positive elements in an array:", positive_numbers)
else:
    print("Array doesn`t have positive elements.")
