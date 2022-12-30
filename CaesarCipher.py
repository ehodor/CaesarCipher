# Created by Emma Hodor on 12/30/2022

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

while True:
    coding = input('Would you like to "encode" or "decode" a message?\n').lower()
    if coding == "encode" or coding == "decode":
        break
    else:
        print('Sorry, input is invalid. Please type either "encode" or "decode".\n')

message = input(f'What message would you like to {coding}?\n').lower()
shift = int(input('By how much would you like to shift?\n')) % 26


def encrypt(message1, shift1):
    new_message = ""
    for i in range(len(message1)):
        if message1[i] not in alphabet:
            new_message += message1[i]
        else:
            asc = ord(message1[i]) + shift1
            if asc > 122:
                loop = asc - 122
                asc = 97 + loop
            new_message += chr(asc)
    print(f"Here's your encoded message: {new_message}")


def decrypt(message1, shift1):
    new_message = ""
    for i in range(len(message1)):
        if message1[i] not in alphabet:
            new_message += message1[i]
        else:
            asc = ord(message1[i]) - shift1
            if asc < 97:
                loop = 97 - asc
                asc = 122 - loop
            new_message += chr(asc)
    print(f"Here's your decoded message: {new_message}")


if coding == "encode":
    encrypt(message, shift)
elif coding == "decode":
    decrypt(message, shift)
