# Choose if it is Encrypt or Decrypt
# takes a plain text input for the message
# takes a plain text input for the KEY


characters = list('abcdefghijklmnopqrstuvwxyz')
input_message = ""
input_key = ""
final_indeces = []
resultArr = []
result = ''

temp_array_indeces_message = []
temp_array_indeces_key = []

characters = list('abcdefghijklmnopqrstuvwxyz')
input_message = ""
input_key = ""
final_indeces = []
resultArr = []
result = ''

temp_array_indeces_message = []
temp_array_indeces_key = []

# this function is for preserving the original casing and non-alphabet characters
def preserve_case_and_nonalpha(original, transformed_letters):
    result = []
    index = 0
    for char in original:
        if char.isalpha():
            if char.isupper():
                result.append(transformed_letters[index].upper())
            else:
                result.append(transformed_letters[index])
            index += 1
        else:
            result.append(char)
    return ''.join(result)

#Process the input
def input_process():
    global input_message, input_key, temp_array_indeces_message, temp_array_indeces_key, characters
    input_message = input("Enter the Message: ")
    input_key = input("Enter the Key: ")

    # filter alphabetic characters for ciphering
    temp_message = [char.lower() for char in input_message if char.isalpha()]
    temp_key = list(input_key.lower())

    temp_array_indeces_message = [characters.index(char) for char in temp_message]
    temp_array_indeces_key = [characters.index(char) for char in temp_key]

#encrypt
def vigenereAlgo_encrypt():
    global temp_array_indeces_message, temp_array_indeces_key, final_indeces, result, characters, resultArr
    final_indeces = []
    resultArr = []

    # repeat key to match message length
    temp_array_indeces_key_full = (temp_array_indeces_key * ((len(temp_array_indeces_message) // len(temp_array_indeces_key)) + 1))[:len(temp_array_indeces_message)]

    print(f"\nMessage: {input_message}")
    print(f"Key: {input_key}\n")
    print(f"Message → {temp_array_indeces_message}")
    print(f"Key     → {temp_array_indeces_key_full}")
    print(f"Applying the formula.....")

    for i in range(len(temp_array_indeces_message)):
        m = temp_array_indeces_message[i]
        k = temp_array_indeces_key_full[i]
        c = (m + k) % 26
        final_indeces.append(c)
        resultArr.append(characters[c])
        print(f"({m} + {k}) % 26 = {(m + k)} % 26 = {c} → {characters[c].upper()}")

    result = preserve_case_and_nonalpha(input_message, resultArr)
    print(f"Ciphertext: {result}\n")

#decrypt
def vigenereAlgo_decrypt():
    global temp_array_indeces_message, temp_array_indeces_key, final_indeces, result, characters, resultArr
    final_indeces = []
    resultArr = []

    # Repeat key to match message length
    temp_array_indeces_key_full = (temp_array_indeces_key * ((len(temp_array_indeces_message) // len(temp_array_indeces_key)) + 1))[:len(temp_array_indeces_message)]

    print(f"\nCiphertext: {input_message}")
    print(f"Key: {input_key}\n")
    print(f"Ciphertext → {temp_array_indeces_message}")
    print(f"Key        → {temp_array_indeces_key_full}")
    print(f"Applying the formula.....")

    for i in range(len(temp_array_indeces_message)):
        c = temp_array_indeces_message[i]
        k = temp_array_indeces_key_full[i]
        p = (c - k) % 26
        final_indeces.append(p)
        resultArr.append(characters[p])
        print(f"({c} - {k}) % 26 = {(c - k)} % 26 = {p} → {characters[p].upper()}")

    result = preserve_case_and_nonalpha(input_message, resultArr)
    print(f"Plaintext: {result}\n")


#take thea
def option():
    choice = input("[0]Encrypt\n[1]Decrypt\n[2]Exit\nWhat do you like to do?: ")
    if choice == '0':
        print('\n--------Encryption--------\n')
        input_process()
        vigenereAlgo_encrypt()
    if choice == '1':
        print('\n--------Decryption--------\n')
        input_process()
        vigenereAlgo_decrypt()
    if choice == '2':
        print('Exiting\n')
        return

def main():
    option()



main()

# vigenereAlgo_encrypt()
# refer to the temp arrays

# Encryption Example (mod 26):
# Plaintext: HELLO
# Key: VIGEN
# Convert letters to numerical values (A=0, B=1, ..., Z=25):
# •	HELLO → (7, 4, 11, 11, 14)
# •	VIGEN → (21, 8, 6, 4, 13)
# Apply the Vigenère formula: (Plaintext + Key) mod 26
# •	(7 + 21) mod 26 = 28 mod 26 = 2 → C
# •	(4 + 8) mod 26 = 12 mod 26 = M
# •	(11 + 6) mod 26 = 17 mod 26 = R
# •	(11 + 4) mod 26 = 15 mod 26 = P
# •	(14 + 13) mod 26 = 27 mod 26 = B
# Ciphertext: CMRPB

# Decryption Example (mod 26):
# Ciphertext: QVPFA
# Key: CIPHER
# Convert letters to numerical values:
# •	QVPFA → (16, 21, 15, 5, 0)
# •	CIPHER → (2, 8, 15, 7, 4)
# Apply the Vigenère formula: (Ciphertext - Key) mod 26
# •	(16 - 2) mod 26 = 14 mod 26 = O
# •	(21 - 8) mod 26 = 13 mod 26 = N
# •	(15 - 15) mod 26 = 0 mod 26 = A
# •	(5 - 7) mod 26 = -2 mod 26 = Y
# •	(0 - 4) mod 26 = -4 mod 26 = W
# Plaintext: ONAYW
