from art import logo


# Creating a single function caesar() for both encode and decode
def caesar(direction_of_caesar, plain_text, shift_number):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction_of_caesar == "encode":
                new_position = position + shift_number
                while new_position > len(alphabet):
                    new_position -= len(alphabet)
            else:
                new_position = position - shift_number
                while new_position < 0:
                    new_position += len(alphabet)
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The {direction_of_caesar}d text is {cipher_text}")


print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
repeat = True
while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction_of_caesar=direction, plain_text=text, shift_number=shift)
    repeat = input("Would you like to continue the programa? yes or no\n").lower() == "yes"
