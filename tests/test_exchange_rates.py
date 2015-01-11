# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    # Python 2
    str_cls = unicode
except (NameError):
    # Python 3
    str_cls = str

from decimal import Decimal
import unittest
from .unittest_data import DataDecorator, data
import vat_moss.exchange_rates


@DataDecorator
class ExchangeRatesTests(unittest.TestCase):

    def test_fetch(self):
        valid_currency_codes = [
            'BGN',
            'CZK',
            'DKK',
            'EUR',
            'GBP',
            'HRK',
            'HUF',
            'NOK',
            'PLN',
            'RON',
            'SEK',
            'USD'
        ]

        date, rates = vat_moss.exchange_rates.fetch()

        self.assertIsInstance(date, str_cls)

        result_currency_codes = rates.keys()
        for code in valid_currency_codes:
            self.assertIn(code, result_currency_codes)

    @staticmethod
    def currency_formats():
        return (
            ('BGN', '4101.79', '4,101.79 Lev'),
            ('CZK', '4101.79', '4.101,79 Kč'),
            ('DKK', '4101.79', '4.101,79 Dkr'),
            ('EUR', '4101.79', '€4.101,79'),
            ('GBP', '4101.79', '£4,101.79'),
            ('HRK', '4101.79', '4.101,79 Kn'),
            ('HUF', '4101.79', '4.101,79 Ft'),
            ('NOK', '4101.79', '4.101,79 Nkr'),
            ('PLN', '4101.79', '4 101,79 Zł'),
            ('RON', '4101.79', '4.101,79 Lei'),
            ('SEK', '4101.79', '4 101,79 Skr'),
            ('USD', '4101.79', '$4,101.79'),
        )

    @data('currency_formats')
    def format(self, code, amount, expected_result):
        result = vat_moss.exchange_rates.format(Decimal(amount), code)
        self.assertEqual(expected_result, result)
