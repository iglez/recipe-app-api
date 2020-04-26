from django.test import TestCase

from app.calc import add, subsctract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Test that two number are added toigehter"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ Test that values are substracted and returned"""
        self.assertEqual(subsctract(5, 11), 6)
