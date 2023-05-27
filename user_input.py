def user_input():
    print('hello there')
    user_status = input('how are you? ')
    print('you said: ' + user_status)

    x = input('enter a value:')
    print(x)
    print(float(x) / 2)

if __name__ == "__main__":
    user_input()