def is_prime(n):
    if n < 2:
        print("Not Prime")
        return

    i = 2

    while i * i <= n:
        if n % i == 0:
            print("Not Prime")
            return
        i += 1

    print("Prime")

n = int(input("ENTER NUMBER: "))
is_prime(n)
