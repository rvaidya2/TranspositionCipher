import sys
import re

def validate_key(key, key_length):
    if len(key) != key_length:
        print("Error: <keylength> must match the length of <key>")
        sys.exit(1)
    for digit in range(1, key_length + 1):
        if str(digit) not in key:
            print("Error: <key> must include all digits from 1 to <keylength> with each digit occurring exactly once")
            sys.exit(1)

def validate_text(text):
    pattern = r'^[a-z0-9]+$'
    match = re.search(pattern, text)
    if (match == None):
        print("Error: <inputfile> must contain only lowercase letters (a-z) or digits (0-9)")
        sys.exit(1)

def encrypt(text, key):
    num_columns = len(key)
    num_rows = len(text) // num_columns + (1 if len(text) % num_columns != 0 else 0)
    matrix = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]
    
    
    for i, char in enumerate(text):
        row = i // num_columns
        col = i % num_columns
        matrix[row][col] = char

    ciphertext = ''
    for col in key:
        col_index = int(col) - 1
        for row in matrix:
            ciphertext += row[col_index]
    ciphertext = ciphertext.replace(' ', 'z')


    return ciphertext


def decrypt(ciphertext, key):
    num_columns = len(key)
    num_rows = len(ciphertext) // num_columns
    matrix = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]

    index = 0
    for col in key:
        col_index = int(col) - 1
        for row in range(num_rows):
            matrix[row][col_index] = ciphertext[index]
            index += 1

    plaintext = ''
    for row in matrix:
        plaintext += ''.join(row)
    

    return plaintext


def main():
    if len(sys.argv) != 6:
        print("Usage: python3 trans.py <keylength> <key> <inputfile> <outputfile> <enc/dec>")
        sys.exit(1)

    key_length = int(sys.argv[1])
    key = sys.argv[2]
    input_file = sys.argv[3]
    output_file = sys.argv[4]
    mode = sys.argv[5]

    validate_key(key, key_length)

    with open(input_file, 'r') as file:
        text = file.read()

    validate_text(text)

    if mode == 'enc':
        ciphertext = encrypt(text, key)
        with open(output_file, 'w') as file:
            file.write(ciphertext)
        print("Ciphertext in", output_file)
    elif mode == 'dec':
        plaintext = decrypt(text, key)
        with open(output_file, 'w') as file:
            file.write(plaintext)
        print("Plaintext in", output_file)
    else:
        print("Invalid. Use 'enc' for encryption or 'dec' for decryption.")

if __name__ == "__main__":
    main()
