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
            ('at', 'ATU 38289400',),
            ('be', 'BE0844.044.609',),
            ('bg', 'BG160072254',),
            ('cy', 'CY 10132211L',),
            ('cz', 'CZ15046575',),
            ('de', 'DE 173548186',),
            ('dk', 'DK 65 19 68 16',),
            ('ee', 'EE 100 931 558',),
            ('el', 'EL 094259216',),
            ('es', 'ES B58378431',),
            ('fi', 'FI- 2077474-0',),
            ('fr', 'FR 27 514868827',),
            ('gb', 'GB 365684514',),
            ('hr', 'HR76639357285',),
            ('hu', 'HU24166575',),
            ('ie', 'IE6388047V',),
            ('it', 'IT05175700482',),
            ('lt', 'LT100006688411',),
            ('lu', 'LU21416127',),
            ('lv', 'LV90009253362',),
            ('mt', 'MT20681625',),
            ('nl', 'NL 814246205 B01',),
            ('no', 'NO974760673MVA',),
            ('pl', 'PL 5263024325',),
            ('pt', 'pt 502332743',),
            ('ro', 'RO 24063308',),
            ('se', 'SE 516405444601',),
            ('si', 'si47992115',),
            ('sk', 'sk2020270780',),
        )

    @staticmethod
    def invalid_ids():
        return (
            ('GBGD000',),
            ('IE000000',),
            ('AT1',)
        )

    @data('valid_ids', True)
    def validate_id(self, vat_id):
        mapped_country_code = vat_id.strip()[0:2].upper()
        # Greece uses a different VAT prefix than their ISO 3166-1 country code
        if mapped_country_code == 'EL':
            mapped_country_code = 'GR'

        result = vat_moss.id.validate(vat_id)
        result_country_code = result[0][0:2]

        self.assertEqual(result_country_code, mapped_country_code)

    @data('invalid_ids')
    def validate_id_invalid(self, vat_id):
        self.assertRaises(vat_moss.errors.InvalidError, vat_moss.id.validate, vat_id)
