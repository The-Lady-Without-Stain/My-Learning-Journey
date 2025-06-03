#Defining our functions for prime, armstrong and palindrome
def prime(num):
    if num <= 1:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True

def armstrong(num):
    a_digits = [int(b) for b in str(num)]
    n = len(a_digits)
    return sum(b ** n for b in a_digits) == num

def palindrome(num):
    return str(num) == str(num)[::-1]


#Checking a number to see if it is prime, armstrong, palindrome or a combination.
while True:
    user_input = input("Please enter a positive number: ")

    try:
        num = int(user_input)
        if num < 0:
            raise ValueError("Negative numbers are not allowed.")

        results = []

        if prime(num):
            results.append("prime")
        if armstrong(num):
            results.append("Armstrong")
        if palindrome(num):
            results.append("palindrome")

        if results:
            print(f"{num} is a {', '.join(results)} number.")
        else:
            print("Number is not a prime, an armstrong, or a palindrome")
        break

    except ValueError:
        print("Invalid input. Please, kindly enter a valid positive number.")
