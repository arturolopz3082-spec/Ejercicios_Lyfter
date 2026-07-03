import sys
import os
import json
import tempfile
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from logic import FinanceManager, Category, Movement, validate_title, validate_amount, validate_date, validate_category

from persistence import save_finance_info, load_finance_info, export_csv

class TestValidation(unittest.TestCase):
    def test_valid_title(self):
        self.assertIsNone(validate_title("Salario"))
    def test_title_only_spaces(self):
        self.assertIsNotNone(validate_title(""))
    def test_title_only_spaces_returns_error(self):
        self.assertIsNotNone(validate_title(" "))
    def test_title_too_long(self):
        self.assertIsNotNone(validate_title("A" * 1000))

    def test_valid_amount(self):
        amount, error = validate_amount("150.50")
        self.assertIsNotNone(amount, 150.50)
        self.assertIsNone(error)

    def test_amount_with_comma(self):
        amount, error = validate_amount("200,75")
        self.assertEqual(amount, 200.75)
        self.assertIsNone(error)

    def test_amount_zero_error(self):
        _, error = validate_amount("0")
        self.assertIsNotNone(error)

    def test_negative_amount_error(self):
        _, error = validate_amount("-50")
        self.assertIsNotNone(error)

    def test_text_validate_error(self):
        _, error = validate_amount("abc")
        self.assertIsNotNone(error)

    def test_valid_category(self):
        self.assertIsNone(validate_category("Comida"))

    def test_empty_category(self):
        self.assertIsNotNone(validate_category(""))

    def test_category_too_long(self):
        self.assertIsNotNone(validate_category("C" * 51))

class TestCategories(unittest.TestCase):

    def setUp(self):
        self.manager = FinanceManager()

    def test_add_category_correctly(self):
        ok, _ = self.manager.add_category("Transporte")
        self.assertTrue(ok)
        self.assertEqual(len(self.manager.categories), 1)

    def test_duplicate_category(self):
        self.manager.add_category("Comida")
        ok, msg = self.manager.add_category("Comida")
        self.assertFalse(ok)
        self.assertIn("ya existe", msg.lower())

    def test_duplicate_category_upper_case(self):
        self.manager.add_category("comida")
        ok, _ = self.manager.add_category("COMIDA")
        self.assertFalse(ok)

    def test_category_save_color(self):
        self.manager.add_category("Salud", "#FF0000")
        self.assertEqual(self.manager.categories[0].color, "#FF0000")

    def test_obtain_category_names(self):
        self.manager.add_category("A")
        self.manager.add_category("B")
        self.assertIn("A", self.manager.obtain_category_name())
        self.assertIn("B", self.manager.obtain_category_name())

    def test_obtain_color_category(self):
        self.manager.add_category("Test", "#123456")
        self.assertEqual(self.manager.obtain_color_category("Test"), "#123456")

    def test_color_category_not_exist(self):
        self.assertEqual(self.manager.obtain_color_category("X"), "#FFFFFF")

class TestMovements(unittest.TestCase):

    def setUp(self):
        self.manager = FinanceManager()
        self.manager.add_category("Trabajo")
        self.manager.add_category("Comida")

    def _add_income(self, title="Salario", amount="1000",
                    kind="Trabajo", income_date="01/01/2024"):
        return self.manager.add_movement(title, amount, kind,
                                              "Ingreso", income_date)

    def _add_expense(self, title="Pizza", amount="20",
                     kind="Comida", expense_date="02/01/2024"):
        return self.manager.add_movement(title, amount, kind,
                                              "Gasto", expense_date)

    def test_add_income_correct(self):
        ok, _ = self._add_income()
        self.assertTrue(ok)
        self.assertEqual(len(self.manager.movements), 1)

    def test_income_positive_amount(self):
        self._add_income(amount="500")
        self.assertGreater(self.manager.movements[0].amount, 0)

    def test_expense_negative_amount(self):
        self._add_expense(amount="30")
        self.assertLess(self.manager.movements[0].amount, 0)

    def test_without_categories(self):
        empty_manager = FinanceManager()
        ok, msg = empty_manager.add_movement(
            "Test", "100", "X", "Ingreso", "01/01/2024")
        self.assertFalse(ok)

    def test_category_does_not_exist(self):
        ok, _ = self.manager.add_movement(
            "Test", "50", "Inexistente", "Gasto", "01/01/2024")
        self.assertFalse(ok)

    def test_tipo_invalid_kind_error(self):
        ok, _ = self.manager.add_movement(
            "Test", "50", "Trabajo", "Donación", "01/01/2024")
        self.assertFalse(ok)

    def test_titulo_vacio_retorna_error(self):
        ok, _ = self.manager.add_movement(
            "", "100", "Trabajo", "Ingreso", "01/01/2024")
        self.assertFalse(ok)

    def test_monto_invalido_retorna_error(self):
        ok, _ = self.manager.add_movement(
            "Test", "no-es-numero", "Trabajo", "Ingreso", "01/01/2024")
        self.assertFalse(ok)