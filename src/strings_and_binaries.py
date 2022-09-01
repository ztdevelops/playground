'''
    This file was created with the intention of better understanding
    how strings converted and eventually stored as binaries in memory.

    In a nutshell, each character in the string is first converted to its
    ASCII equivalent, which is a decimal value, then converted to binary.
    After which, to convert it back to a string, the process is reversed.
'''

def toBinary(a: str):
    bin_list = []
    for char in a:
        # Converts character to its respective ASCII code.
        # This is done by matching the character to the
        # ASCII table. The ASCII table can be seen below.
        # https://www.johndcook.com/blog/2022/05/28/how-to-memorize-the-ascii-table/
        ascii_code = ord(char)

        # Convert ASCII code to binary. This is done by
        # converting the base 10 ASCII code to base 2 binary.

        # Slicing the string [2:] removes the binary prefix 0b.
        bin_val = int(bin(ascii_code)[2:])

        bin_list.append(bin_val)
    
    return bin_list

def toString(bin_list: list):
    final_str = ""

    for bin_val in bin_list:
        decimal_val = 0
        for digit in str(bin_val):
            # Left to right approach. Whenever there
            # an additional bit added, multiply the
            # current decimals by 2, which is the same
            # as increasing the exponent value by 1.

            # Doing this gives us the ASCII code.
            decimal_val = decimal_val * 2 + int(digit)
        
        # chr() matches the ASCII code
        # against the table, returning
        # the unicode corresponding to
        # the ASCII code.
        final_str += chr(decimal_val)

    return final_str

str_to_convert = input("Give me a string to test: ")

bin = toBinary(str_to_convert)
returned_str = toString(bin)

if str_to_convert == returned_str:
    print("Conversion OK.")
else:
    print(f"Conversion failed, expected {str_to_convert} but received {returned_str}.")