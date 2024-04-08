def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

n = input('Insert a number.')
n = int(n)
print(f'{n} factorial is: {factorial(n)}')