def IsPrime(number):
    if number <= 1:
        return False

    for d in range(2, int(number**0.5) + 1):
        if number % d == 0:
            return False

    return True


for i in range(20):
    if IsPrime(i + 1):
        print(i, end=" ")
