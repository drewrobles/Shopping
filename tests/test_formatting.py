import unittest

from formatting import encode, _get_ascii_digits, _get_binary_digits, _scramble_digits, _get_decimal_value


class IntegrationTests(unittest.TestCase):
    '''
    Tests from "More examples" section of problem spec
    '''

    def test_single_character(self):
        input_text = 'A'
        
        expected = 16777217
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_full_bundle(self):
        input_text = 'FRED'
        
        expected = 251792692 
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_non_alphanumerics(self):
        input_text = ' :^)'

        expected = 79094888
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_four_lowercase(self):
        input_text = 'foo'

        expected = 124807030
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_space_lowercase(self):
        input_text = ' foo'

        expected = 250662636
        actual = encode(input_text)
        
        self.assertEqual(expected, actual)

    def test_four_lowercase(self):
        input_text = 'foot'

        expected = 267939702
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_four_uppercase(self):
        input_text = 'BIRD'

        expected = 251930706
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_four_periods(self):
        input_text = '....'

        expected = 15794160
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_four_carets(self):
        input_text = '^^^^'

        expected = 252706800
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_capitalized_word(self):
        input_text = 'Woot'

        expected = 266956663
        actual = encode(input_text)

        self.assertEqual(expected, actual)

    def test_two_lowercase(self):
        input_text = 'no'

        expected = 53490482
        actual = encode(input_text)

        self.assertEqual(expected, actual)

class BaseTestCases:

    class BaseTest(unittest.TestCase):
        '''
        Classes that inherit from BaseTest require the following variables:

        - raw_characters
        - ascii_digits
        - input_binary
        - output_binary

        to be defined in test setUp function as class variables.
        '''

        def test_get_ascii_digits(self):
            '''First step is to convert raw characters to ascii digits'''

            actual = self.ascii_digits
            expected = _get_ascii_digits(self.raw_characters)

            self.assertEqual(actual, expected)

        def test_get_binary_digits(self):
            '''Second step is to convert ascii digits into binary'''

            actual = self.input_binary
            expected = _get_binary_digits(self.ascii_digits)

            self.assertEqual(actual, expected)

        def test_scramble_digits(self):
            '''Third step is to scramble binary digits''' 
            
            actual = self.output_binary
            expected = _scramble_digits(self.input_binary)

            self.assertEqual(actual, expected)

        def test_get_decimal_value(self):
            '''Fourth step is convert binary digits into decimal'''

            actual = self.output_decimal
            expected = _get_decimal_value(self.output_binary)

            self.assertEqual(actual, expected)

        def test_encode(self):
            '''Public function does all the steps in one'''

            actual = self.output_decimal
            expected = encode(self.raw_characters)

            self.assertEqual(actual, expected)


class TestSingleCharacter(BaseTestCases.BaseTest):
    '''
    Tests from "Examples" section of problem spec
    '''
    
    def setUp(self):
        self.raw_characters = 'A'

        self.ascii_digits = [65]

        self.input_binary = [
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 1, 0, 0, 0, 0, 0, 1 
        ]
        
        self.output_binary = [
            0, 0, 0, 0, 0, 0, 0, 1, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 1 
        ]

        self.output_decimal = 16777217 

class TestFullBundle(BaseTestCases.BaseTest):

    def setUp(self):
        self.raw_characters = 'FRED'

        self.ascii_digits = [70, 82, 69, 68]

        self.input_binary = [
            0, 1, 0, 0, 0, 1, 0, 0, 
            0, 1, 0, 0, 0, 1, 0, 1, 
            0, 1, 0, 1, 0, 0, 1, 0, 
            0, 1, 0, 0, 0, 1, 1, 0, 
        ]

        self.output_binary = [
            0, 0, 0, 0, 1, 1, 1, 1, 
            0, 0, 0, 0, 0, 0, 1, 0, 
            0, 0, 0, 0, 1, 1, 0, 1, 
            0, 0, 1, 1, 0, 1, 0, 0, 
        ]

        self.output_decimal = 251792692

class TestNonAlphanumerics(BaseTestCases.BaseTest):
    
    def setUp(self):
        self.raw_characters = ' :^)'

        self.ascii_digits = [32, 58, 94, 41]

        self.input_binary = [
            0, 0, 1, 0, 1, 0, 0, 1,
            0, 1, 0, 1, 1, 1, 1, 0,
            0, 0, 1, 1, 1, 0, 1, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
        ]

        self.output_binary = [
            0, 0, 0, 0, 0, 1, 0, 0,
            1, 0, 1, 1, 0, 1, 1, 0,
            1, 1, 1, 0, 0, 1, 0, 0,
            0, 1, 1, 0, 1, 0, 0, 0,
        ]

        self.output_decimal = 79094888


if __name__ == '__main__':
    unittest.main()