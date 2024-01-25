def bin_to_dec(bin_str):
    return int(bin_str, 2)

def dec_to_bin(dec_num):
    return bin(dec_num)[2:]

def hex_to_dec(hex_str):
    return int(hex_str, 16)

def dec_to_hex(dec_num):
    return hex(dec_num)[2:]

def bin_to_hex(bin_str):
    dec_num = bin_to_dec(bin_str)
    return dec_to_hex(dec_num)

def hex_to_bin(hex_str):
    dec_num = hex_to_dec(hex_str)
    return dec_to_bin(dec_num)

def main():
    while True:
        print("\n1. Binär zu Dezimal")
        print("2. Dezimal zu Binär")
        print("3. Hexadezimal zu Dezimal")
        print("4. Dezimal zu Hexadezimal")
        print("5. Binär zu Hexadezimal")
        print("6. Hexadezimal zu Binär")
        print("7. Beenden")

        choice = input("Bitte wählen Sie eine Option (1-7): ")

        if choice == '1':
            bin_str = input("Geben Sie die Binärzahl ein: ")
            print("Dezimal: {}".format(bin_to_dec(bin_str)))

        elif choice == '2':
            dec_num = int(input("Geben Sie die Dezimalzahl ein: "))
            print("Binär: {}".format(dec_to_bin(dec_num)))

        elif choice == '3':
            hex_str = input("Geben Sie die Hexadezimalzahl ein: ")
            print("Dezimal: {}".format(hex_to_dec(hex_str)))

        elif choice == '4':
            dec_num = int(input("Geben Sie die Dezimalzahl ein: "))
            print("Hexadezimal: {}".format(dec_to_hex(dec_num)))

        elif choice == '5':
            bin_str = input("Geben Sie die Binärzahl ein: ")
            print("Hexadezimal: {}".format(bin_to_hex(bin_str)))

        elif choice == '6':
            hex_str = input("Geben Sie die Hexadezimalzahl ein: ")
            print("Binär: {}".format(hex_to_bin(hex_str)))

        elif choice == '7':
            break

        else:
            print("Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und 7.")

if __name__ == "__main__":
    main()
