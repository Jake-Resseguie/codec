# Jacob Resseguie

encoded_password = ""


def encode():
    password = input("Please enter your password to encode: ")
    encode = ""
    for i in range(0, len(password)):
        encode += str((int(password[i]) + 3) % 10)
    print("Your password has been encoded and stored!")
    return encode


def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_password += str(abs(int(digit) - 3) % 10)
    print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        menu_option = int(input("Please enter an option: "))
        global encoded_password

        if menu_option == 1:
            encoded_password = encode()
        elif menu_option == 2:
            decode(encoded_password)
        elif menu_option == 3:
            exit()


if __name__ == "__main__":
    main()
