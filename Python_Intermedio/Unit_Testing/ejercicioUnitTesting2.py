import unittest, sys, os

from Python_Basics.Functions.ejercicioFunciones3 import sum_list
from Python_Basics.Functions.ejercicioFunciones4 import reverse_string
from Python_Basics.Functions.ejercicioFunciones5 import contarLetras
from Python_Basics.Functions.ejercicioFunciones6 import order_words
from Python_Basics.Functions.ejercicioFunciones7 import return_prime_number


#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class TestSumList(unittest.TestCase):
    def test_sum_list_with_positive_numbers(self):
        expected = 41
        result = sum_list([4,6,2,29])
        self.assertEqual(result, expected)

    def test_sum_list_with_sum_wrong(self):
        expected = 49
        result = sum_list([4,6,2,29])
        self.assertNotEqual(result, expected)

    def test_sum_with_empty_list(self):
        expected = "La lista está vacía"
        result = sum_list([])
        self.assertEqual(result, expected)

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        expected = 'orutra'
        result = reverse_string('arturo')
        self.assertEqual(result, expected)

    def test_reverse_string_incorrect(self):
        expected = 'arturo'
        result = reverse_string('jose')
        self.assertNotEqual(result, expected)

    def test_reverse_string_has_character(self):
        self.assertIn('r', reverse_string('Lyfter'))

class TestContarLetras(unittest.TestCase):
    def test_contar_letras_correct(self):
        expected = 'There is 3 uppercase letters and 13 lowercase letters.'
        result = contarLetras('I love Nacion Sushi')
        self.assertEqual(result, expected)

    def test_contar_letras_incorrect(self):
        expected = 'There is 4 uppercase letters and 12 lowercase letters.'
        result = contarLetras('Lyfter')
        self.assertNotEqual(result, expected)

    def test_contar_letras_has_character(self):
        expected = 'There is 3 uppercase letters and 13 lowercase letters.'
        result = contarLetras('I love Nacion Sushi')
        self.assertIn('3', result)

class TestOrderWords(unittest.TestCase):
    def test_order_words_correct(self):
        expected = 'computadora-funcion-monitor-python-variable'
        result = order_words('python-variable-funcion-computadora-monitor')
        self.assertEqual(result, expected)

    def test_order_words_one_word(self):
        expected = 'python'
        result = order_words('python')
        self.assertEqual(result, expected)

    def test_order_words_with_empty_string(self):
        expected = ''
        result = order_words('')
        self.assertEqual(result, expected)


class TestPrimeNumbers(unittest.TestCase):
    def test_prime_numbers_correct(self):
        self.assertEqual(return_prime_number([1,4,6,7,13,9,67]), [7,13,67])

    def test_prime_numbers_instance(self):
        self.assertIsInstance(return_prime_number([1,4,6,7,13,9,67]), list)

    def test_prime_numbers_false(self):
        self.assertFalse(return_prime_number([1,4,6,8,9,10]))


