def encode(input_text):
    ascii_number = ord('A')
    input_binary_digits = _get_binary_digits(ascii_number)
    scrambled_binary_digits = _scramble_digits(input_binary_digits)
    output_decimal_value = _get_decimal_value(sc)

    return ascii_number

def _get_decimal_digits(number):
    return _get_digits(number, 10)

def _get_binary_digits(number):
    return _get_digits(number, 2)

def _get_digits(number, base):
    digits = []

    while True:
        curr_digit = number % base 
        digits.insert(0, curr_digit)
        number = number - curr_digit

        if number == 0:
            break

        number = number // base 
        
    return digits

def _scramble_digits(digits):
    scrambled = []

    for col in range(8):
        for row in range(4):
            scrambled.append(get_arr_value(digits, row, col))
        
    return scrambled        

def get_arr_value(arr, row, col):
    index = row * 8 
    return arr[index+ col]

def _get_decimal_value(binary_digits):
    decimal_value = 0

    for i in range(len(binary_digits)):
        binary_index = len(binary_digits) - i - 1
        binary_digit = binary_digits[binary_index]

        decimal_value += binary_digit * 2 ** i
    
    return decimal_value