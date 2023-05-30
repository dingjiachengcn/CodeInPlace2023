import random

def main():
    random_value_seed = random.seed(1) #put it in first
    print(random_value_seed)
    # generate random number between min 1 and max 6
    dice_roll = random.randint(1, 6)
    print('dice value:', dice_roll)
    random_value_float = random.uniform(1, 3)
    print(random_value_float)


if __name__ == "__main__":
    main()

