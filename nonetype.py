import random


def mystery_int():
    """
    return 2 or None with equal
    probability (0.5)
    """
    if random.random() > 0.5:
        return 2


def main():
    """
    set x equal to mystery_int
    check if x is an integer
    if so, print the square of x
    """

    x = mystery_int()
    print(x)

    if x is not None:
        print(x * x)


if __name__ == "__main__":
    main()