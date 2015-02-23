import sys
import unittest

from tests.test_billing_address import BillingAddressTests
from tests.test_declared_residence import DeclaredResidenceTests
from tests.test_geoip2 import Geoip2Tests
from tests.test_phone_number import PhoneNumberTests
from tests.test_exchange_rates import ExchangeRatesTests

if len(sys.argv) < 2 or sys.argv[1] != '--skip-id':
    from tests.test_id import IdTests
elif len(sys.argv) > 1 and sys.argv[1] == '--skip-id':
    del sys.argv[1]


if __name__ == '__main__':
    unittest.main()
