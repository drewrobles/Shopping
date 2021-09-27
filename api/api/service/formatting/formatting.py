def decode(arr):
    return ''.join([decode_16_bits(number) for number in arr])

def decode_16_bits(number):
    # Convert decimal to binary
    digits = decimal_to_binary(number)


    # Unscramble binary digits
    digits = unscramble_binary_digits(digits)

    # Convert binary into ascii digits
    digits = [_get_decimal_value(digits[i*8:i*8+8]) for i in range(4)]

    # Convert ascii digits into raw character
    return ''.join([chr(number) for number in reversed(digits)]).strip(chr(0))    

def is_valid_chunk(digits, chunk_num):
    for i in range(chunk_num * 8, chunk_num*8+8):
    # for i in range(digits[chunk_num * 8: chunk_num*8+8]):
        if digits[i] != 0:
            return True
    return False

def stringify_digits(arr):
    digits = [str(curr) for curr in arr]
    val = ''
    for i in range(len(digits)):
        if i % 8 == 0 and i != 0:
            val += ' '
        val += digits[i]

    return val

def decimal_to_binary(num):
    arr = []
    decimal_to_binary_helper(num, arr)
    _zero_pad(arr, 32)

    return arr


def decimal_to_binary_helper(num, arr):
    if num >= 1:
        decimal_to_binary_helper(num // 2, arr)
        arr.append(num % 2)

def unscramble_binary_digits(digits):
    unscrambled = [-1] * 32

    for i in range(len(digits)):
        unscrambled[i] = digits[i // 8 + (i % 8) * 4]

    return unscrambled    

def set_arr_value(arr, row, col, value):
    arr[row * 8 + col] = value


def encode(input_text):
    chunks = []

    for i in range(0, len(input_text), 4):
        curr_chunk = input_text[i:min(i+4, len(input_text))]
        encoded_chunk = encode_16_bits(curr_chunk)
        chunks.append(encoded_chunk)

    return chunks

def encode_16_bits(input_text):
    '''Encodes input text in Weird Text Format (8-bit)'''

    # Convert raw characters into ascii digits
    input_ascii_digits = _get_ascii_digits(input_text)

    # Convert ascii digits into binary
    input_binary_digits = _get_binary_digits(input_ascii_digits)

    # Scramble binary digits
    scrambled_binary_digits = _scramble_digits(input_binary_digits)

    # Convert binary digits into decimal
    output_decimal_value = _get_decimal_value(scrambled_binary_digits)

    return output_decimal_value 

def _get_ascii_digits(input_text):
    '''Returns an array of integers representing ascii values'''

    return [ord(char) for char in input_text]

def _get_binary_digits(ascii_digits):
    '''Convert array of ascii digits to binary digits'''

    binary_digits = []

    for curr_ascii_digit in ascii_digits:
        # Convert integer into array of binary digits
        curr_binary_chunk = _get_digits(curr_ascii_digit, 2)

        # Add binary digits chunk to left of binary array
        binary_digits = curr_binary_chunk + binary_digits

    # Left pad array so that it is of length 32
    _zero_pad(binary_digits, 32)

    return binary_digits

def _get_digits(number, base):
    '''Returns the digits of an integer in provided base'''

    digits = []

    while True:
        # Get digit in ones place
        curr_digit = number % base 

        # Insert ones digit into left of array 
        digits.insert(0, curr_digit)

        # Make digit in ones place a zero 
        number = number - curr_digit

        # No more digits to add if number is zero
        if number == 0:
            break

        # Right shift number to get rid of ones place
        number = number // base 

    # Left pad array so that it is of length 8
    _zero_pad(digits, 8)

    return digits

def _zero_pad(digits, length):
    '''Left pad array with zeros to reach total length'''

    for i in range(len(digits), length):
        digits.insert(0, 0)

def _unscramble_digits(digits):
    '''Unscramble digits by iterating along columns of virtual 2D array'''

    unscrambled = [-1] * 32

    index = 0

    for col in range(8):
        for row in range(4):
            # Get current value to put back
            arr_value = arr_value[index]

            set_arr_value(uncrambled, row, col, arr_value)

    return uncrambled

def set_arr_value(arr, row, col, value):
    arr[row * 8 + col] = value

def _scramble_digits(digits):
    '''Scramble digits by iterating along columns of virtual 2D array'''

    scrambled = []

    for col in range(8):
        for row in range(4):
            # Get array value at virtual row and column
            arr_value = get_arr_value(digits, row, col) 

            # Add array value to scrambled digits array
            scrambled.append(arr_value)
        
    return scrambled        

def get_arr_value(arr, row, col):
    '''Get value in array at current row and column of virtual 2D array'''

    return arr[row * 8 + col]

def _get_decimal_value(binary_digits):
    '''Convert binary digits into decimal'''

    decimal_value = 0

    for i in range(len(binary_digits)):
        # Iterate binary digits starting at least significant digit
        binary_index = len(binary_digits) - i - 1
        binary_digit = binary_digits[binary_index]

        # Add computed value of binary digit to decimal value
        decimal_value += binary_digit * 2 ** i
    
    return decimal_value
