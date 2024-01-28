alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        # # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
        while new_position > len(alphabet):
            new_position -= len(alphabet)
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


# Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(encrypted_text, shift_number):
    decrypted_text = ""
    # Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by
    #  the shift amount and print the decrypted text.
    # e.g.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"
    for letter in encrypted_text:
        old_position = alphabet.index(letter)
        new_position = old_position - shift_number
        while new_position < 0:
            new_position += len(alphabet)
        new_letter = alphabet[new_position]
        decrypted_text += new_letter
    print(f"Decrypted text is {decrypted_text}")


# Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
#  Then call the correct function based on that 'drection' variable.
#  You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(encrypted_text=text, shift_number=shift)


