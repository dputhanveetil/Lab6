# divya puthanveetil

def encode(password):
    pass_list = list(password)
    encoded = []

    for item in pass_list:
        encoded.append(int(item) + 3)

    return encoded


def decode():
    pass


if __name__ == "__main__":
    menu = "Menu\n-------------\n1. Encode\n2. Decode\n3. Quit"

    while True:
        print(menu)
        print("\nPlease enter an option: ")
        choice = int(input())

        if choice == 1:
            print("Print please enter your password to encode: ")
            ogpassword = input()
            print("Your password has been stored!")
            encoded = encode(ogpassword)

        elif choice == 2:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded} ")

        elif choice == 3:
            break

        else:
            pass
