def sum_of_squares(n):
    result = 0
    for i in range(1, n + 1):
        result += i ** 2
    return result

n = int(input("Enter a positive integer: "))
if n > 0:
    result = sum_of_squares(n)
    print(f"The sum of squares for the first {n} positive numbers is {result}")
else:
    print("Please enter a positive integer.")
