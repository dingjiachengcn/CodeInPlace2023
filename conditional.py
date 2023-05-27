def conditional():
    name = "Michael"
    age = 21
    born_in_december = True
    lucky_number = 6

    if name != "Karel":
        print("Hi, I don't think we've met before!")
    if age == 21 or not(born_in_december):
        print("Do you remember...")
    if lucky_number > 5 and name == "Michael" and not(age == 30) and born_in_december:
        print("Hey! I've been looking all over for you!")

if __name__ == '__main__':
    conditional()