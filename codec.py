# Jacob Resseguie
def encode(menu_option):
    if menu_option == 1:
        password = input("Please enter your password to encode: ")
        encode = ""
        for i in range(0,len(password)):
            encode += str(int(password[i])+3)
    print("Your password has been encoded and stored!")
    return encode

def main():

    print("Manu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")
    menu_option = int(input("Please enter an option: "))
    encode(menu_option)



if __name__ == "__main__":
    main()