# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from .unittest_data import DataDecorator, data
import vat_moss.id
import vat_moss.errors


@DataDecorator
class IdTests(unittest.TestCase):

    @staticmethod
    def valid_ids():
        # These are all read, valid VAT IDs that we test against
        # VIES and data.brreg.no
        return (
            ('at', 'ATU 38289400',     'ATU38289400',    'AT'),
            ('be', 'BE0844.044.609',   'BE0844044609',   'BE'),
            ('bg', 'BG160072254',      'BG160072254',    'BG'),
            ('cy', 'CY 10132211L',     'CY10132211L',    'CY'),
            ('cz', 'CZ15046575',       'CZ15046575',     'CZ'),
            ('de', 'DE 173548186',     'DE173548186',    'DE'),
            ('dk', 'DK 65 19 68 16',   'DK65196816',     'DK'),
            ('ee', 'EE 100 931 558',   'EE100931558',    'EE'),
            ('el', 'EL 094259216',     'EL094259216',    'GR'),
            ('gr', 'GR094259216',      'EL094259216',    'GR'),
            ('es', 'ES B58378431',     'ESB58378431',    'ES'),
            ('fi', 'FI- 2077474-0',    'FI20774740',     'FI'),
            ('fr', 'FR 27 514868827',  'FR27514868827',  'FR'),
            ('gb', 'GB 365684514',     'GB365684514',    'GB'),
            ('hr', 'HR76639357285',    'HR76639357285',  'HR'),
            ('hu', 'HU24166575',       'HU24166575',     'HU'),
            ('ie', 'IE6388047V',       'IE6388047V',     'IE'),
            ('it', 'IT05175700482',    'IT05175700482',  'IT'),
            ('lt', 'LT120212314',      'LT120212314',    'LT'),
            ('lu', 'LU21416127',       'LU21416127',     'LU'),
            ('lv', 'LV90009253362',    'LV90009253362',  'LV'),
            ('mt', 'MT20681625',       'MT20681625',     'MT'),
            ('nl', 'NL 814246205 B01', 'NL814246205B01', 'NL'),
            ('no', 'NO974760673MVA',   'NO974760673MVA', 'NO'),
            ('pl', 'PL 5263024325',    'PL5263024325',   'PL'),
            ('pt', 'pt 502332743',     'PT502332743',    'PT'),
            ('ro', 'RO 24063308',      'RO24063308',     'RO'),
            ('se', 'SE 516405444601',  'SE516405444601', 'SE'),
            ('si', 'si47992115',       'SI47992115',     'SI'),
            ('sk', 'sk2020270780',     'SK2020270780',   'SK'),
            ('al', 'AL J 61929021 E',  None,             None)
        )

    @staticmethod
    def invalid_ids():
        return (
            ('GBGD000',),
            ('IE000000',),
            ('AT1',)
        )

    @data('valid_ids', True)
    def normalize(self, vat_id, expected_normalized_vat_id, expected_country_code):
        result = vat_moss.id.normalize(vat_id)
        self.assertEqual(expected_normalized_vat_id, result)

    @data('valid_ids', True)
    def validate_id(self, vat_id, expected_normalized_vat_id, expected_country_code):
        try:
            result = vat_moss.id.validate(vat_id)
            if result:
                country_code, normalized_vat_id, name = result
                self.assertEqual(expected_country_code, country_code)
                self.assertEqual(expected_normalized_vat_id, normalized_vat_id)
            else:
                self.assertEqual(expected_normalized_vat_id, result)
        except (vat_moss.errors.WebServiceUnavailableError):
            return unittest.skip('VIES webservice unavailable')

    @data('invalid_ids')
    def validate_id_invalid(self, vat_id):
        self.assertRaises(vat_moss.errors.InvalidError, vat_moss.id.validate, vat_id)
