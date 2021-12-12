import argparse
import pprint

pp = pprint.PrettyPrinter(indent=4)

# initialize matrix 26x26, with zero
matrix = [[0 for x in range(26)] for y in range(26)] 

# A have value 65 on ascii table (65 + 0)
# B value is 65 + 1 = 66
# ...
# Z is 65 + 25 = 90
# decimal_value_of_A = 65
decimal_value_of_A = ord('A')


# This function generates the
def generateKey(string, key):

    if len(string) == len(key):
        return(key.upper())
    elif len(string) < len(key):
        return key[0:len(string)].upper()
    else:
        key_list = list(key)
        len_key = len(key_list)
        missing_padding = len(string) - len_key
        for i in range(missing_padding):

            # % is modulo. the div reminding
            index = i % len_key
            next_letter = key_list[index]
            key_list.append(next_letter)
    key_with_padding = "".join(key_list)
    return(key_with_padding.upper())


def encodeText(original_text, key):

    encoded_text_list = list()

    # 1. get first letter of the key (first_letter_key)
    # 2. get (row) for that letter (the alphabet)
    # 3. get first letter from original_text (first_letter_text)
    # 4. for the previous row, get column for that letter (j)
    # 5. the encoded letter will be [i][j]
    # 6. repeat for remaining letters (original_text)

    #1
    len_key = len(key)
    for c in range(len_key):
        first_letter_key = key[c]

        decimal_first_letter_key = ord(first_letter_key)
        row = decimal_first_letter_key - decimal_value_of_A

        first_letter_text = original_text[c]
        decimal_first_letter_text = ord(first_letter_text)

        column = decimal_first_letter_text - decimal_value_of_A

        encoded_letter = matrix[row][column]
        encoded_text_list.append(encoded_letter)

    return ''.join(encoded_text_list)



def decodeText(encoded_text, key):

    decoded_text_list = list()

    len_key = len(key)
    for c in range(len_key):
        first_letter_key = key[c]

        decimal_first_letter_key = ord(first_letter_key)
        row = decimal_first_letter_key - decimal_value_of_A

        first_letter_text = encoded_text[c]
        decimal_first_letter_text = ord(first_letter_text)

        first_letter_text_index = decimal_first_letter_text - decimal_value_of_A - row
 
        if first_letter_text_index < 0:
            first_letter_text_index = first_letter_text_index + 26

        decoded_letter_value = first_letter_text_index + decimal_value_of_A
        decoded_letter = chr(decoded_letter_value)
        decoded_text_list.append(decoded_letter)

    return ''.join(decoded_text_list)



def main():

    # the alphabet have 26 letters
    # a...wxyz
    # build the matrix, used to encode
    for i in range(26):
        for j in range(26):

            next_relative_index_from_A = (i + j) % 26
            letter_value = decimal_value_of_A + next_relative_index_from_A
            letter = chr(letter_value)
            matrix[i][j] = letter


    #
    # Parse command line
    #
    # To encode:
    # $> python c3-2.py --encode <PLAIN TEXT> --key <KEY TEXT>
    # To decode:
    # $> python c3-2.py --decode <ENC TEXT> --key <KEY TEXT>    
    #
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", required = True, help="specify key. must be only letters")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--encode", help="specify text to encode. must be only letters")
    group.add_argument("--decode", help="specify text to decode. must be only letters")

    args = parser.parse_args()
    pp.pprint(args)

    key_str = str(args.key)
    if not key_str.isalpha():
        print("Invalid key. It only accepts letters. Exit.")
        exit(1)

    keyword = key_str.upper()

    if args.encode:
        string = str(args.encode)
    else:
        string = str(args.decode)


    if not string.isalpha():
        print("Invalid text to encode|decode. It only accepts letters. Exit.")
        exit(1)        
    string = string.upper()

    key = generateKey(string, keyword)
    print("Key: " + key)

    if args.encode:
        string = args.encode
        encoded_text = encodeText(string, key)
        print("Encoded text: " + encoded_text)
    else:
        string = args.decode
        decoded_text = decodeText(string, key)
        print("Decoded text: " + decoded_text)


if __name__ == "__main__":
    main()
