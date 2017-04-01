def problem_1():
    s = 0
    for i in range(1, 1001):
        if i % 5 == 0 or i % 3 == 0:
            s+=i
    print(s)

def problem_2():
    a, b = 2, 1
    s = 0
    while a < 4 * 1000 * 1000:
        if a % 2 == 0:
            s+=a
        a, b = a + b, a
    print(s)

def sieve(n):
    primes = [1]*n

    for u in range(2, n):
        for v in range(2, n):
            if u * v < n:
                primes[u*v] = 0
                print(u*v);

def palindrome(str):
    for i in range(len(str)/2):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

def problem_4():
    l = 0

    for x in range(1, 1000):
        for y in range(1, 1000):
            if palindrome(str(x*y)) and x*y > l:
                print(x*y)
                l = x * y

def problem_5():
    n = 20
    while True:
        divisible = True
        for i in range(2, 20):
            if n % i != 0:
                divisible = False
                break
        if divisible:
            print(n)
            break

        n+= 20

def problem_6():
    linSum = 0
    squareSum = 0
    for i in range(1, 101):
        linSum+=i
        squareSum+=i*i

    print(linSum*linSum-squareSum)

problem_6()
