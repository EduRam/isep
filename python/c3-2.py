
# initialize matrix 26x26, with zero
matrix = [[0 for x in range(26)] for y in range(26)] 

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


def encodeText(string, key):
    cipher_text = []
    return


def main():

    # A have value 65 on ascii table (65 + 0)
    # B value is 65 + 1 = 66
    # ...
    # Z is 65 + 25 = 90
    decimal_value_of_A = ord('A')

    # the alphabet have 26 letters
    # a...wxyz

    for i in range(26):
        for j in range(26):

            next_index_from_A = (i + j) % 26
            letter_value = decimal_value_of_A + next_index_from_A
            letter = chr(letter_value)
            matrix[i][j] = letter


    string = "aBcDeF"
    keyword = "aBc"
    key = generateKey(string, keyword)
    print(key)

    encoded = encodeText(string, key)
    print(encoded)

    # print matrix
    #print("\n".join('|'.join(row) for row in matrix))


if __name__ == "__main__":
    main()
