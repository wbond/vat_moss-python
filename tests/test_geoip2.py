# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from decimal import Decimal
from .unittest_data import DataDecorator, data
import vat_moss.geoip2


@DataDecorator
class Geoip2Tests(unittest.TestCase):

    @staticmethod
    def geodata():
        return (
            # GeoLite2 Data                                                # Address info                   # Expected result
            ('AT', 'Tyrol',                     'Reutte',                  'AT', 'Jungholz',                Decimal('0.19'), 'AT', 'Jungholz'),
            ('AT', 'Tyrol',                     'Reutte',                  'AT', None,                      Decimal('0.20'), 'AT', None),
            ('AT', 'Vorarlberg',                'Mittelberg',              'AT', 'Mittelberg',              Decimal('0.19'), 'AT', 'Mittelberg'),
            ('AT', 'Salzburg',                  'Salzburg',                'AT', None,                      Decimal('0.20'), 'AT', None),

            ('BE', 'Brussels Capital',          'Schaarbeek',              'BE', None,                      Decimal('0.21'), 'BE', None),
            ('BG', 'Sofia-Capital',             'Sofia',                   'BG', None,                      Decimal('0.20'), 'BG', None),
            ('CY', 'Lefkosia',                  'Nicosia',                 'CY', None,                      Decimal('0.19'), 'CY', None),
            ('CZ', 'Hlavni mesto Praha',        'Prague',                  'CZ', None,                      Decimal('0.21'), 'CZ', None),

            ('DE', 'Schleswig-Holstein',        'Pinneberg',               'DE', 'Heligoland',              Decimal('0.0'),  'DE', 'Heligoland'),
            ('DE', 'Schleswig-Holstein',        'Pinneberg',               'DE', None,                      Decimal('0.19'), 'DE', None),
            ('DE', 'Baden-Württemberg Region',  'Konstanz',                'DE', 'Büsingen am Hochrhein',   Decimal('0.0'),  'DE', 'Büsingen am Hochrhein'),
            ('DE', 'Schleswig-Holstein',        'Berlin',                  'DE', None,                      Decimal('0.19'), 'DE', None),
            # Test an exception address with a non-exception geoip2 record
            ('DE', 'Schleswig-Holstein',        'Berlin',                  'DE', 'Heligoland',              Decimal('0.19'), 'DE', None),

            ('DK', 'Capital Region',            'Copenhagen',              'DK', None,                      Decimal('0.25'), 'DK', None),
            ('EE', 'Harju',                     'Tallinn',                 'EE', None,                      Decimal('0.20'), 'EE', None),

            ('ES', 'Canary Islands',            'Santa Cruz de Tenerife',  'ES', 'Canary Islands',          Decimal('0.0'),  'ES', 'Canary Islands'),

            ('ES', 'Melilla',                   'Melilla',                 'ES', 'Melilla',                 Decimal('0.0'),  'ES', 'Melilla'),
            ('ES', 'Ceuta',                     'Ceuta',                   'ES', 'Ceuta',                   Decimal('0.0'),  'ES', 'Ceuta'),
            ('ES', 'Madrid',                    'Madrid',                  'ES', None,                      Decimal('0.21'), 'ES', None),

            ('FI', '',                          'Helsinki',                'FI', None,                      Decimal('0.24'), 'FI', None),
            ('FR', 'Île-de-France',             'Paris',                   'FR', None,                      Decimal('0.20'), 'FR', None),
            ('GB', 'England',                   'London',                  'GB', None,                      Decimal('0.20'), 'GB', None),

            ('GR', 'Central Macedonia',         'Ormylia',                 'GR', 'Mount Athos',             Decimal('0.0'),  'GR', 'Mount Athos'),
            ('GR', 'Central Macedonia',         'Ormylia',                 'GR', None,                      Decimal('0.23'), 'GR', None),
            ('GR', 'Attica',                    'Athens',                  'GR', None,                      Decimal('0.23'), 'GR', None),

            ('HR', 'Grad Zagreb',               'Zagreb',                  'HR', None,                      Decimal('0.25'), 'HR', None),
            ('HU', 'Budapest fovaros',          'Budapest',                'HU', None,                      Decimal('0.27'), 'HU', None),
            ('IE', 'Leinster',                  'Dublin',                  'IE', None,                      Decimal('0.23'), 'IE', None),

            ('IT', 'Lombardy',                  'Como',                    'IT', "Campione d'Italia",       Decimal('0.0'),  'IT', "Campione d'Italia"),
            ('IT', 'Lombardy',                  'Como',                    'IT', None,                      Decimal('0.22'), 'IT', None),
            ('IT', 'Lombardy',                  'Livigno',                 'IT', 'Livigno',                 Decimal('0.0'),  'IT', 'Livigno'),
            # Test an exception geoip2 record with a non-exception address
            ('IT', 'Lombardy',                  'Livigno',                 'IT', None,                      Decimal('0.0'),  'IT', 'Livigno'),
            ('IT', 'Lombardy',                  'Cologne',                 'IT', None,                      Decimal('0.22'), 'IT', None),

            ('LT', 'Vilnius County',            'Vilnius',                 'LT', None,                      Decimal('0.21'), 'LT', None),
            ('LU', 'District de Luxembourg',    'Luxembourg',              'LU', None,                      Decimal('0.15'), 'LU', None),
            ('LV', 'Riga',                      'Riga',                    'LV', None,                      Decimal('0.21'), 'LV', None),
            ('MT', 'Il-Belt Valletta',          'Valletta',                'MT', None,                      Decimal('0.18'), 'MT', None),
            ('NL', 'North Holland',             'Amsterdam',               'NL', None,                      Decimal('0.21'), 'NL', None),
            ('PL', 'Masovian Voivodeship',      'Warsaw',                  'PL', None,                      Decimal('0.23'), 'PL', None),

            ('PT', 'Azores',                    'Lajes',                   'PT', 'Azores',                  Decimal('0.0'),  'PT', 'Azores'),
            ('PT', 'Azores',                    'Lajes',                   'PT', None,                      Decimal('0.0'),  'PT', 'Azores'),
            ('PT', 'Madeira',                   'Santa Cruz',              'PT', 'Madeira',                 Decimal('0.0'),  'PT', 'Madeira'),
            ('PT', 'Madeira',                   'Santa Cruz',              'PT', None,                      Decimal('0.0'),  'PT', 'Madeira'),
            ('PT', 'Lisbon',                    'Lisbon',                  'PT', None,                      Decimal('0.23'), 'PT', None),

            ('RO', 'Bucuresti',                 'Bucharest',               'RO', None,                      Decimal('0.24'), 'RO', None),
            ('SE', 'Stockholm',                 'Stockholm',               'SE', None,                      Decimal('0.25'), 'SE', None),
            ('SI', '',                          'Ljubljana',               'SI', None,                      Decimal('0.22'), 'SI', None),
            ('SK', 'Bratislavsky kraj',         'Bratislava',              'SK', None,                      Decimal('0.20'), 'SK', None),

            ('MC', 'Monaco',                    'Monaco',                  'MC', None,                      Decimal('0.20'), 'MC', None),
            ('IM', '',                          'Douglas',                 'IM', None,                      Decimal('0.20'), 'IM', None),

            ('NO', 'Oslo County',               'Oslo',                    'NO', None,                      Decimal('0.25'), 'NO', None),

            ('US', 'Massachusetts',             'Newburyport',             'US', None,                      Decimal('0.0'),  'US', None),
            ('CA', 'Ontario',                   'Ottawa',                  'CA', None,                      Decimal('0.0'),  'CA', None),
        )

    @data('geodata')
    def calculate_rate(self, country_code, subdivision, city, address_country_code, address_exception, expected_rate, expected_country_code, expected_exception_name):
        result = vat_moss.geoip2.calculate_rate(country_code, subdivision, city, address_country_code, address_exception)
        result_rate, result_country_code, result_exception_name = result

        self.assertEqual(result_rate, expected_rate)
        self.assertEqual(result_country_code, expected_country_code)
        self.assertEqual(result_exception_name, expected_exception_name)
