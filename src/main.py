import sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if len(sys.argv) < 2:
    raise ValueError("Must pass in a file name and a key.")

with open(f'../input/{sys.argv[1]}', 'r') as input_file:
    unencrypted_message = input_file.read()

encrypted_message = []
for letter in unencrypted_message:
    if letter.upper() not in LETTERS:
        encrypted_message.append(letter)
        continue

    encrypted_letter = LETTERS[(LETTERS.index(letter.upper()) + int(sys.argv[2])) % len(LETTERS)]
    encrypted_letter = encrypted_letter.lower() if letter.islower() else encrypted_letter

    encrypted_message.append(encrypted_letter)

print(''.join(encrypted_message))