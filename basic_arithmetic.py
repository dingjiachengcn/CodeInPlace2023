def basic_arithmetic():
    x = int('34') + 17.0
    y = 19 + int(float('5.0'))
    print(x)
    print(y)

    a = 3.625
    b = int(a)
    print(float(b))

    c = 15
    c += 6  # same as x = x + 6     (x = 21)
    c -= 10  # same as x = x - 10    (x = 11)
    c *= 8  # same as x = x * 8     (x = 88)
    c /= 4  # same as x = x / 4
    print(c)

if __name__ == '__main__':
    basic_arithmetic()