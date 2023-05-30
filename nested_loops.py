def nested_loops():

    # for i in range(5):
    #     for j in range(5):
    #         print("hello world!")

    number = 64
    while (number >=1 ):
        print("ok!")
        for i in range(3):
            print(i + 1)
        number /= 2

if __name__ == "__main__":
    nested_loops()
