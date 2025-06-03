def fibonacci_sequence(f):
    a, b = 0, 1
    f_sequence = []

    for n in range(f):
        f_sequence.append(a)
        a, b = b, a + b

    return f_sequence


try:
    my_fibonacci = int(input ("Enter the number of fibonacci sequences you want: "))
    if my_fibonacci <= 0:
        raise ValueError ("You cannot enter zero or a negative number.")
    print(fibonacci_sequence(my_fibonacci))

except ValueError as e:
    if str(e).startswith("You"):
        print(e)

    else:
        print("Invalid input. Please, kindly enter a valid positive number.")




