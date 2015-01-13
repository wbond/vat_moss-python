# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from decimal import Decimal
from .unittest_data import DataDecorator, data
import vat_moss.billing_address


@DataDecorator
class BillingAddressTests(unittest.TestCase):

    @staticmethod
    def addresses():
        return (
            # Example user input                                # Expected result
            ('AT',  '6691',      'Jungholz',                    Decimal('0.19'), 'AT', 'Jungholz'),
            ('AT',  '6991',      'Mittelberg',                  Decimal('0.19'), 'AT', 'Mittelberg'),
            ('at',  '6992',      'Mittelberg',                  Decimal('0.19'), 'AT', 'Mittelberg'),
            ('AT',  'AT-6993',   'Mittelberg',                  Decimal('0.19'), 'AT', 'Mittelberg'),
            ('AT',  '6971',      'Hard',                        Decimal('0.20'), 'AT', None),

            ('BE',  '1000',      'Brussels',                    Decimal('0.21'), 'BE', None),

            ('BG',  '1000',      'Sofia',                       Decimal('0.20'), 'BG', None),

            ('CH',  '8238',      'Büsingen am Hochrhein',       Decimal('0.0'),  'DE', 'Büsingen am Hochrhein'),
            ('CH',  '6911',      "Campione d'Italia",           Decimal('0.0'),  'IT', "Campione d'Italia"),
            ('CH',  '3907',      'Domodossola',                 Decimal('0.22'), 'IT', None),

            ('CY',  'CY-1010',   'Nicosia',                     Decimal('0.19'), 'CY', None),
            ('CY',  '1010',      'Nicosia',                     Decimal('0.19'), 'CY', None),

            ('CZ',  '250 00',    'Prague',                      Decimal('0.21'), 'CZ', None),

            ('DE',  '87491',     'Jungholz',                    Decimal('0.19'), 'AT', 'Jungholz'),
            ('de',  '87567',     'Mittelberg',                  Decimal('0.19'), 'AT', 'Mittelberg'),
            ('de ', '87568',     'mittelberg',                  Decimal('0.19'), 'AT', 'Mittelberg'),
            ('DE',  'DE-87569',  'Mittelberg',                  Decimal('0.19'), 'AT', 'Mittelberg'),
            ('DE',  '78266',     'Büsingen am Hochrhein',       Decimal('0.0'),  'DE', 'Büsingen am Hochrhein'),
            ('DE',  '27498',     'Heligoland',                  Decimal('0.0'),  'DE', 'Heligoland'),
            ('DE',  '04774',     'Dahlen',                      Decimal('0.19'), 'DE', None),

            ('DK',  '1000',      'Copenhagen',                  Decimal('0.25'), 'DK', None),

            ('EE',  '15199',     'Tallinn',                     Decimal('0.20'), 'EE', None),

            ('ES',  '38001',     'Santa Cruz de Tenerife',      Decimal('0.0'),  'ES', 'Canary Islands'),
            ('ES',  '35630',     'Antigua',                     Decimal('0.0'),  'ES', 'Canary Islands'),
            ('ES',  '35001',     'Las Palmas',                  Decimal('0.0'),  'ES', 'Canary Islands'),
            ('ES',  '35500',     'Arrecife',                    Decimal('0.0'),  'ES', 'Canary Islands'),
            ('ES',  '38700',     'Santa Cruz de La Palma',      Decimal('0.0'),  'ES', 'Canary Islands'),
            ('ES',  '38880',     'San Sebastián de La Gomera',  Decimal('0.0'),  'ES', 'Canary Islands'),
            ('ES',  '38900',     'Valverde',                    Decimal('0.0'),  'ES', 'Canary Islands'),
            ('ES',  '35540',     'Caleta de Sebo',              Decimal('0.0'),  'ES', 'Canary Islands'),
            ('ES',  '35530',     'Teguise',                     Decimal('0.0'),  'ES', 'Canary Islands'),
            ('ES',  '52002',     'Melilla',                     Decimal('0.0'),  'ES', 'Melilla'),
            ('ES',  '51001',     'Ceuta',                       Decimal('0.0'),  'ES', 'Ceuta'),
            ('es',  '28001',     'Mardrid',                     Decimal('0.21'), 'ES', None),

            ('FI',  '00140',     'Helsinki',                    Decimal('0.24'), 'FI', None),

            ('FR',  '75016',     'Paris',                       Decimal('0.20'), 'FR', None),

            ('GB',  'BFP O57',   'Akrotiri',                    Decimal('0.19'), 'CY', None),
            ('GB',  'BFP O58',   'Dhekelia',                    Decimal('0.19'), 'CY', None),
            ('GB',  'W8 4RU',    'London',                      Decimal('0.20'), 'GB', None),

            ('GR',  '63086',     'Mount Athos',                 Decimal('0.0'),  'GR', 'Mount Athos'),
            ('GR',  '10001',     'Athens',                      Decimal('0.23'), 'GR', None),

            ('HR',  'HR-10000',  'Zagreb',                      Decimal('0.25'), 'HR', None),

            ('HU',  '1239',      'Budapest',                    Decimal('0.27'), 'HU', None),

            ('IE',  'Dublin 1',  'Dublin',                      Decimal('0.23'), 'IE', None),
            ('IE',  None,        'Galway',                      Decimal('0.23'), 'IE', None),

            ('it',  '22060',     "Campione d'Italia",           Decimal('0.0'),  'IT', "Campione d'Italia"),
            ('IT',  '22060',     'Campione dItalia',            Decimal('0.0'),  'IT', "Campione d'Italia"),
            ('it ', '22060',     'Campione',                    Decimal('0.0'),  'IT', "Campione d'Italia"),
            ('it',  '23030',     'Livigno',                     Decimal('0.0'),  'IT', 'Livigno'),
            ('IT',  '00100',     'Rome',                        Decimal('0.22'), 'IT', None),

            ('LT',  '01001',     'Vilnius',                     Decimal('0.21'), 'LT', None),

            ('LU',  'L-1248',    'Luxembourg',                  Decimal('0.15'), 'LU', None),

            ('LV',  'LV-1001',   'Riga',                        Decimal('0.21'), 'LV', None),

            ('MT',  'VLT',       'Valletta',                    Decimal('0.18'), 'MT', None),

            ('NL',  '1000',      'Amsterdam',                   Decimal('0.21'), 'NL', None),

            ('PL',  '00-001',    'Warsaw',                      Decimal('0.23'), 'PL', None),

            ('PT',  '9970',      'Santa Cruz das Flores',       Decimal('0.0'),  'PT', 'Azores'),
            ('PT',  '9980-024',  'Vila do Corvo',               Decimal('0.0'),  'PT', 'Azores'),
            ('PT',  '9880-352',  'Santa Cruz da Graciosa',      Decimal('0.0'),  'PT', 'Azores'),
            ('PT',  '9701-101',  'Angra do Heroísmo',           Decimal('0.0'),  'PT', 'Azores'),
            ('PT',  '9800-539',  'Velas',                       Decimal('0.0'),  'PT', 'Azores'),
            ('PT',  '9930-135',  'Lajes do Pico',               Decimal('0.0'),  'PT', 'Azores'),
            ('PT',  '9900-997',  'Horta',                       Decimal('0.0'),  'PT', 'Azores'),
            ('PT',  '9560-045',  'Lagoa',                       Decimal('0.0'),  'PT', 'Azores'),
            ('PT',  '9580-539',  'Vila do Porto',               Decimal('0.0'),  'PT', 'Azores'),
            ('PT',  '9000',      'Funchal',                     Decimal('0.0'),  'PT', 'Madeira'),
            ('PT',  '1149-014',  'Lisbon',                      Decimal('0.23'), 'PT', None),

            ('RO',  '010131',    'București',                   Decimal('0.24'), 'RO', None),

            ('SE',  'SE-100 00', 'Stockholm',                   Decimal('0.25'), 'SE', None),

            ('SI',  '1000',      'Ljubljana',                   Decimal('0.22'), 'SI', None),

            ('SK',  '811 02',    'Bratislava',                  Decimal('0.20'), 'SK', None),

            ('MC',  '98025',     'Monaco',                      Decimal('0.20'), 'MC', None),

            ('IM',  'IM2 1RB',   'Douglas',                     Decimal('0.20'), 'IM', None),

            ('NO',  '0001',      'Oslo',                        Decimal('0.25'), 'NO', None),

            ('US',  '01950',     'Newburyport',                 Decimal('0.0'),  'US', None),

            ('CA',  'K2R 1C5',   'Ottawa',                      Decimal('0.0'),  'CA', None),

        )

    @data('addresses')
    def calculate_rate(self, country_code, postal_code, city, expected_rate, expected_country_code, expected_exception_name):
        result = vat_moss.billing_address.calculate_rate(country_code, postal_code, city)
        result_rate, result_country_code, result_exception_name = result

        self.assertEqual(result_rate, expected_rate)
        self.assertEqual(result_country_code, expected_country_code)
        self.assertEqual(result_exception_name, expected_exception_name)

    @staticmethod
    def invalid_addresses():
        return (
            ('CA',  None,    'Ottawa'),
            ('US',  None,    'Boston'),
            ('',    '02108', 'Boston'),
            ('US',  '02108', None),
        )

    @data('invalid_addresses')
    def calculate_rate_invalid(self, country_code, postal_code, city):
        self.assertRaises(ValueError, vat_moss.billing_address.calculate_rate, country_code, postal_code, city)
