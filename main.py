import random
from datetime import datetime

alphabet = ['a', 'b', 'c' ,'d' ,'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ["!", "@", "#", "#", "$", "%", "^", "&", "*", "(", ")", "_",
           "[", "{", "]", "}", ";", ":", "'", ",", "<", ".", ">", "/",
           "?", "\\", "|", "`"]

def generate_password(length):
    pw = str()

    for pw_char in range(int(length)):
        # Randomize type of character to add
        type_int = random.randint(0, 2)

        # Add a letter
        if type_int == 0:
            bool_int = random.randint(0, 1)
            rnd_alpha = random.randint(0, len(alphabet) - 1)

            if bool_int == 0:
                pw += alphabet[rnd_alpha].lower()
            elif bool_int == 1:
                pw += alphabet[rnd_alpha].upper()

        # Add a number
        elif type_int == 1:
            rnd_num = random.randint(0, len(numbers) - 1)
            pw += numbers[rnd_num]

        # Add a symbol
        else:
            rnd_sym = random.randint(0, len(symbols) - 1)
            pw += symbols[rnd_sym]

    # Clean-up
    if len(pw) > length:
        for char in range(len(pw) - length):
            pw -= pw[0]

    elif len(pw) < length:
        for char in range(length - len(pw)):
            pw += symbols[random.randint(0, len(symbols) - 1)]

    return pw

def main():
    # pw_len = input("Password Length\n>>> ")
    # password = generate_password(int(pw_len))
    # print(f"Generated password: {password}")
    for password in range(20):
        pw = generate_password(20)
        print(pw)


if __name__ == "__main__":
    main()
