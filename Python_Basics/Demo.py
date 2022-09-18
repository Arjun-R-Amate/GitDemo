# Q: Find out prime number program ?
# Ans = The given number is divisible by 1 or itself is known as prime number.
n = int(input("Enter a given number: "))
for item in range(2, n):
    if n % item == 0:
        print(n, "is not a prime number.")
        break
else:
    print(n, "is prime number.")