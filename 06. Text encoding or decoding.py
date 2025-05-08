alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# COMBINE CODE FOR ENCODING AND DECODING THE INPUT MESSAGE
def caesar(start_text, shift_amount, cipher_direction):
    global new_position
    end_text = " "
    for letter in start_text:
        if letter in alphabet:
            if cipher_direction == "encode":
                position = alphabet.index(letter)
                new_position = position + shift_amount
            elif cipher_direction == "decode":
                position = alphabet.index(letter)
                new_position = position - shift_amount
            else:
                print("invalid input".capitalize())

            end_text += alphabet[new_position]
        else:
            end_text += letter

    if cipher_direction == "encode":
        print(f"The encoded message is \"{end_text} \"")
    elif cipher_direction == "decode":
        print(f"The decoded message is \"{end_text} \"")
    else:
        print("invalid input".capitalize())


play_again = True
while play_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    texts = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=texts, shift_amount=shift, cipher_direction=direction)

    play_again = input('Type "yes" to go again. Otherwise type "no":\n').lower()
    if play_again == "yes":
        play_again = True
    else:
        play_again = False
        print("Good Bye! Ranger.")

# TUTOR'S COMBINED FUNCTION
# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = " "
#     for letter in start_text:
#         position = alphabet.index(letter)
#         if cipher_direction == "decode":
#             shift_amount *= -1
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
#     print(f"The {cipher_direction}d text is {end_text} ")
#
#
# caesar(start_text=texts, shift_amount=shift, cipher_direction=direction)

# SINGLE CODES FOR ENCODING AND DECODING THE INPUT MESSAGE
# def encrypt(plain_text, shift_amount):
#     cipher_text = " "
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encode message is {cipher_text}")
#
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = " "
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")
