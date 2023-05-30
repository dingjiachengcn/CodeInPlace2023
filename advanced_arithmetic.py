import math
import random

def main():
    x = 36 / 2
    y = 36 // 10
    z = 36.0 // 10
    a = -5 // 2
    b = 39 % 17
    c = 12 % 4
    d = 18 % 19
    e = - (19 - 7) # the 1st is minus, the 2nd is negation
    f = 23 - -4    # the 1st is negation, the 2nd is minus
    g = --8

    h = random.randint(0, 5)       # must be a non-negative number
    i = random.randint(1, 5)       # must be a positive number
    ans1 = math.exp(math.sqrt(h) * math.pi)
    ans1 += math.log(i)

    print(x)
    print(y)
    print(z)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)

    print(ans1)

if __name__ == '__main__':
    main()