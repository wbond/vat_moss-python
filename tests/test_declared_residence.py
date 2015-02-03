# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from decimal import Decimal
from .unittest_data import DataDecorator, data
import vat_moss.declared_residence


@DataDecorator
class DeclaredResidenceTests(unittest.TestCase):

    @staticmethod
    def residences():
        return (
            # User input                           # Expected result
            ('AT', 'Jungholz',                    Decimal('0.19'), 'AT', 'Jungholz'),
            ('AT', 'Mittelberg',                  Decimal('0.19'), 'AT', 'Mittelberg'),
            ('AT', None,                          Decimal('0.20'), 'AT', None),
            ('BE', None,                          Decimal('0.21'), 'BE', None),
            ('BG', None,                          Decimal('0.20'), 'BG', None),
            ('CY', None,                          Decimal('0.19'), 'CY', None),
            ('CZ', None,                          Decimal('0.21'), 'CZ', None),
            ('DE', 'Heligoland',                  Decimal('0.0'),  'DE', 'Heligoland'),
            ('DE', 'Büsingen am Hochrhein',       Decimal('0.0'),  'DE', 'Büsingen am Hochrhein'),
            ('DE', None,                          Decimal('0.19'), 'DE', None),
            ('DK', None,                          Decimal('0.25'), 'DK', None),
            ('EE', None,                          Decimal('0.20'), 'EE', None),
            ('ES', 'Canary Islands',              Decimal('0.0'),  'ES', 'Canary Islands'),
            ('ES', 'Melilla',                     Decimal('0.0'),  'ES', 'Melilla'),
            ('ES', 'Ceuta',                       Decimal('0.0'),  'ES', 'Ceuta'),
            ('ES', None,                          Decimal('0.21'), 'ES', None),
            ('FI', None,                          Decimal('0.24'), 'FI', None),
            ('FR', None,                          Decimal('0.20'), 'FR', None),
            ('GB', 'Akrotiri',                    Decimal('0.19'), 'CY', None),
            ('GB', 'Dhekelia',                    Decimal('0.19'), 'CY', None),
            ('GB', None,                          Decimal('0.20'), 'GB', None),
            ('GR', 'Mount Athos',                 Decimal('0.0'),  'GR', 'Mount Athos'),
            ('GR', None,                          Decimal('0.23'), 'GR', None),
            ('HR', None,                          Decimal('0.25'), 'HR', None),
            ('HU', None,                          Decimal('0.27'), 'HU', None),
            ('IE', None,                          Decimal('0.23'), 'IE', None),
            ('IT', "Campione d'Italia",           Decimal('0.0'),  'IT', "Campione d'Italia"),
            ('IT', 'Livigno',                     Decimal('0.0'),  'IT', 'Livigno'),
            ('IT', None,                          Decimal('0.22'), 'IT', None),
            ('LT', None,                          Decimal('0.21'), 'LT', None),
            ('LU', None,                          Decimal('0.15'), 'LU', None),
            ('LV', None,                          Decimal('0.21'), 'LV', None),
            ('MT', None,                          Decimal('0.18'), 'MT', None),
            ('NL', None,                          Decimal('0.21'), 'NL', None),
            ('PL', None,                          Decimal('0.23'), 'PL', None),
            ('PT', 'Azores',                      Decimal('0.0'),  'PT', 'Azores'),
            ('PT', 'Madeira',                     Decimal('0.0'),  'PT', 'Madeira'),
            ('PT', None,                          Decimal('0.23'), 'PT', None),
            ('RO', None,                          Decimal('0.24'), 'RO', None),
            ('SE', None,                          Decimal('0.25'), 'SE', None),
            ('SI', None,                          Decimal('0.22'), 'SI', None),
            ('SK', None,                          Decimal('0.20'), 'SK', None),
            ('MC', None,                          Decimal('0.20'), 'MC', None),
            ('IM', None,                          Decimal('0.20'), 'IM', None),
            ('NO', None,                          Decimal('0.25'), 'NO', None),
            ('US', None,                          Decimal('0.0'),  'US', None),
            ('CA', None,                          Decimal('0.0'),  'CA', None),
        )

    @data('residences')
    def calculate_rate(self, country_code, exception_name, expected_rate, expected_country_code, expected_exception_name):
        result = vat_moss.declared_residence.calculate_rate(country_code, exception_name)
        result_rate, result_country_code, result_exception_name = result

        self.assertEqual(result_rate, expected_rate)
        self.assertEqual(result_country_code, expected_country_code)
        self.assertEqual(result_exception_name, expected_exception_name)

    @staticmethod
    def exceptions():
        return (
            ['AT', ['Jungholz', 'Mittelberg']],
            ['DE', ['Büsingen am Hochrhein', 'Heligoland']],
            ['ES', ['Canary Islands', 'Ceuta', 'Melilla']],
            ['GB', ['Akrotiri', 'Dhekelia']],
            ['GR', ['Mount Athos']],
            ['IT', ["Campione d'Italia", 'Livigno']],
            ['PT', ['Azores', 'Madeira']],
            ['US', []],
            ['IM', []],
        )

    @data('exceptions')
    def exceptions_by_country(self, country, exceptions):
        result = vat_moss.declared_residence.exceptions_by_country(country)
        self.assertEqual(result, exceptions)
