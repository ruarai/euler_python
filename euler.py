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

def is_prime(n):
    if(n <= 1):
        return False
    i = 2
    while i*i <= n:
        if(n % i == 0):
            return False
        i+= 1
    return True

def problem_7():
    numPrimes = 1
    num = 1
    while numPrimes<=10001:
        num += 1
        if is_prime(num):
            numPrimes += 1#so many 1's in this function
    print(num)

problem_8_input = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

def problem_8():
    numStr = problem_8_input.replace('\n','')
    print(numStr)

    largestProduct = 0

    for i in range(0,len(numStr) - 13):
        p = 1
        for j in range(i,i + 13):
            p*=int(numStr[j])
        if p > largestProduct:
            largestProduct = p

    print(largestProduct)

def problem_9():
    for x in range(1, 1000):
        for y in range(1, 1000):
            for z in range(1, 1000):
                if x*x+y*y==z*z and x + y + z == 1000:
                    print(x*y*z)
                    return

def sieve(n):
    table = [1]*n
    table[0] = 0
    table[1] = 0

    for u in range(2, n):
        for v in range(2, n):
            if u * v < n:
                table[u*v] = 0

    primes = []
    for i in range(n):
        if table[i] == 1:
            primes.append(i)
    return primes

def problem_10():
    print(sum(sieve(10)))
    print(sum(sieve(2*1000*1000)))

problem_10()
