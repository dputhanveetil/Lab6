# divya puthanveetil

# added by Paul Chojecki
from decode import *


def encode(password):
    pass_list = list(password)
    encoded = []

    for item in pass_list:
        encoded.append(str((int(item) + 3) % 10))

    encoded_str = ''.join(encoded)

    return int(encoded_str)


if __name__ == "__main__":
    menu = "Menu\n-------------\n1. Encode\n2. Decode\n3. Quit"

    while True:
        print(menu)
        print("\nPlease enter an option: ", end='')
        choice = int(input())

        if choice == 1:
            print("Print please enter your password to encode: ", end='')
            ogpassword = input()
            print("Your password has been stored!")
            print()
            encoded = encode(ogpassword)

        elif choice == 2:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded} ")
            print()

        elif choice == 3:
            break

        else:
            pass
