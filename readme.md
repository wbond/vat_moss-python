# vat_moss

A library to determine the VAT rate for a customer of a company providing
digital services to individuals in the EU or Norway.

**This readme primarily covers the Python `vat_moss` library API. I have written
an extensive amount of guidance in the [VAT MOSS Overview](overview.md). I
highly recommend you read that first.** It includes information about invoices,
registration, exchange rates and more.

## Supports

Python 2.7, 3.3 and 3.4.

## Approach

My current approach to VAT place of supply proof and rate selection is to:

 1. Using geolocation on the user's IP address to determine what country
    they are likely in
 2. Show prices VAT-inclusive for EU countries. In EU countries, my customers
    will pay 30% more to cover the VAT, plus exchange rate fluctuations and
    costs related to paying the collected VAT to the HRMC. All of this takes
    time and things like international wire tranfers cost money. Currently the
    highest VAT rate is 27%. Many are around 20%. 30% covers the highest, plus
    provides a little extra to cover the costs related to VAT compliance.
 3. When the user checks out, have them self-declare residence country
    (pre-populated from IP geolocation). If their country has any VAT
    exceptions, let them pick one.
 4. If the IP geolocation and declared residence match, allow the user to check
    out. You have two pieces of non-contradictory place of supply proof.
 5. If the IP geolocation and declared residence do not match, ask the user
    for their phone number and compare with geolocation and declared residence.
    If any two match, let the user check out. Otherwise ask them to resolve the
    discrepency. Save the two non-conflicting pieces of information as place
    of supply proof.
 6. If the user is located in an EU country, allow them to enter their VAT ID.
    Validate this ID. If it is valid, deduct the appropriate percentage amount
    from VAT-inclusive prices and let the user check out. To calculate the
    VAT-exclusive price, divide the VAT-include price by (1.0 + VAT rate).
 7. Once the customer has successfully checked out, generate an invoice that
    meets VAT requirements. This means including things like your VAT ID for
    EU customers and including the customers VAT ID (if provided), along with
    some other country-specific currency requirements. See the 
    [VAT MOSS Overview](overview.md) for more information.

## API

 - [Determine VAT Rate from Billing Address](#determine-vat-rate-from-billing-address)
 - [Determine VAT Rate from Declared Residence](#determine-vat-rate-from-declared-residence)
 - [Determine VAT Rate from GeoLite2 Database](#determine-vat-rate-from-geolite2-database)
 - [Determine VAT Rate from International Phone Number](#determine-vat-rate-from-international-phone-number)
 - [Validate a VAT ID](#validate-a-vat-id)

### Determine VAT Rate from Billing Address

*Either this method, or Determine VAT Rate from Declared Residence, can be used
as one piece of location proof. Using both will not result in two pieces of
proof since both are user-provided locations.*

The user's VAT Rate can be determined by processing a payment and using the
billing address from the payment provider, or prompting the user to input their
country (code), postal code and city name.

The method signature is
`vat_moss.billing_address.calculate_rate(country_code, postal_code, city)`.
This will return a tuple of
`(Decimal rate, country code, exception name or None)`. Examples:

 - `(Decimal('0.0'),  'US', None)`
 - `(Decimal('0.19'), 'DE', None)`
 - `(Decimal('0.0'),  'DE', 'Heligoland')`

The exception name will be one of the exemptions to the normal VAT rates. See
the end of http://ec.europa.eu/taxation_customs/resources/documents/taxation/vat/how_vat_works/rates/vat_rates_en.pdf
for a full list.

```python
import vat_moss.billing_address

try:
    # Values from user input or payment provider
    country_code = 'US'
    postal_code = '01950'
    city = 'Newburyport'

    result = vat_moss.billing_address.calculate_rate(country_code, postal_code, city)
    rate, country_code, exception_name = result
    
    # Save place of supply proof

except (ValueError):
    # One of the user input values is empty or not a string
```

For place of supply proof, you should save the country code, postal code, city
name, detected rate and any exception name.

### Determine VAT Rate from Declared Residence

*Either this method, or Determine VAT Rate from Billing Address, can be used
as one piece of location proof. Using both will not result in two pieces of
proof since both are user-provided locations.*

The user's VAT Rate can be determined by prompting the user with a list of
valid countries obtained from `vat_moss.declared_residence.options()`. If the
user chooses a country with one or more exceptions, the user should be
presented with another list of "None" and each exception name. This should be
labeled something like: "Special VAT Rate".

The method signature to get the appropriate rate is
`vat_moss.declared_residence.calculate_rate(country_code, exception_name)`.
This will return a tuple of
`(Decimal rate, country code, exception name or None)`. Examples:

 - `(Decimal('0.0'), 'US', None)`
 - `(Decimal('0.19'), 'DE', None)`
 - `(Decimal('0.0'), 'DE', 'Heligoland')`

```python
import vat_moss.declared_residence

try:
    # Loop through this list of dicts and build a <select> using the 'name' key
    # as the text and 'code' key as the value. The 'exceptions' key is a list of
    # valid VAT exceptions for that country. You will probably need to write
    # some JS to show a checkbox if the selected country has exception, and then
    # present the user with another <select> allowing then to pick "None" or
    # one of the exception names.
    residence_options = vat_moss.declared_residence.options()

    # Values from user input
    country_code = 'DE'
    exception_name = 'Heligoland'

    result = vat_moss.declared_residence.calculate_rate(country_code, exception_name)
    rate, country_code, exception_name = result
    
    # Save place of supply proof

except (ValueError):
    # One of the user input values is empty or not a string
```

For place of supply proof, you should save the country code, detected rate and
any exception name.

### Determine VAT Rate from GeoLite2 Database

The company MaxMind offers a
[http://dev.maxmind.com/geoip/geoip2/geolite2/](free geo IP lookup database).

For this you'll need to install something like the [nginx module](https://github.com/leev/ngx_http_geoip2_module),
[apache module](https://github.com/maxmind/mod_maxminddb) or one of the various
[programming language packages](http://dev.maxmind.com/geoip/geoip2/web-services/).

Personally I like to do it at the web server level since it is fast and always
available.

Once you have the data, you need to feed the country code, subdivision name and
city name into the method
`vat_moss.geoip2.calculate_rate(country_code, subdivision, city, address_country_code, address_exception)`.
The `subdivision` should be the first subdivision name from the GeoLite2
database. The `address_country_code` and `address_exception` should be from
`vat_moss.billing_address.calculate_rate()` or
`vat_moss.declared_residence.calculate_rate()`. This information is necessary
since some exceptions are city-specific and can't solely be detected by the
user's IP address. This will return a tuple of
`(Decimal rate, country code, exception name or None)`. Examples:

 - `(Decimal('0.0'), 'US', None)`
 - `(Decimal('0.19'), 'DE', None)`
 - `(Decimal('0.0'), 'DE', 'Heligoland')`

The exception name will be one of the exemptions to the normal VAT rates. See
the end of http://ec.europa.eu/taxation_customs/resources/documents/taxation/vat/how_vat_works/rates/vat_rates_en.pdf
for a full list.

```python
import vat_moss.geoip2

try:
    # Values from web server or API
    ip = '8.8.4.4'
    country_code = 'US'
    subdivision_name = 'Massachusetts'
    city_name = 'Newburyport'

    # Values from the result of vat_moss.billing_address.calculate_rate() or
    # vat_moss.declared_residence.calculate_rate()
    address_country_code = 'US'
    address_exception = None

    result = vat_moss.geoip2.calculate_rate(country_code, subdivision_name, city_name, address_country_code, address_exception)
    rate, country_code, exception_name = result
    
    # Save place of supply proof

except (ValueError):
    # One of the user input values is empty or not a string
```

For place of supply proof, you should save the IP address; country code,
subdivision name and city name from GeoLite2; the detected rate and any
exception name.

#### Omitting address_country_code and address_exception

If the `address_country_code` and `address_exception` are not provided, in some
situations this function will not be able to definitively determine the
VAT rate for the user. This is because some exemptions are for individual
cities, which are only tracked via GeoLite2 at the district level. This sounds
confusing, but if you look at the GeoLite2 data, you'll see some of the city
entries are actually district names. Lame, I know.

In those situations, a `vat_moss.errors.UndefinitiveError()` exception will be
raised.

### Determine VAT Rate from International Phone Number

Prompt the user for their international phone number (with leading +). Once
you have the data, you need to feed the phone number to
`vat_moss.phone_number.calculate_rate(phone_number, address_country_code, address_exception)`.
The `address_country_code` and `address_exception` should be from
`vat_moss.billing_address.calculate_rate()` or
`vat_moss.declared_residence.calculate_rate()`. This information is necessary
since some exceptions are city-specific and can't solely be detected by the
user's phone number. This will return a tuple of
`(Decimal rate, country code, exception name or None)`. Examples:

 - `(Decimal('0.0'), 'US', None)`
 - `(Decimal('0.19'), 'DE', None)`
 - `(Decimal('0.0'), 'DE', 'Heligoland')`

The exception name will be one of the exemptions to the normal VAT rates. See
the end of http://ec.europa.eu/taxation_customs/resources/documents/taxation/vat/how_vat_works/rates/vat_rates_en.pdf
for a full list.

```python
import vat_moss.phone_number

try:
    # Values from user
    phone_number = '+19785720330'

    # Values from the result of vat_moss.billing_address.calculate_rate() or
    # vat_moss.declared_residence.calculate_rate()
    address_country_code = 'US'
    address_exception = None

    result = vat_moss.phone_number.calculate_rate(phone_number, address_country_code, address_exception)
    rate, country_code, exception_name = result
    
    # Save place of supply proof

except (ValueError):
    # One of the user input values is empty or not a string
```

For place of supply proof, you should save the phone number, detected rate and
any exception name.

#### Omitting address_country_code and address_exception

If the `address_country_code` and `address_exception` are not provided, in some
situations this function will not be able to definitively determine the
VAT rate for the user. This is because some exemptions are for individual
cities, which can not be definitely determined by the user's phone number area
code.

In those situations, a `vat_moss.errors.UndefinitiveError()` exception will be
raised.

### Validate a VAT ID

EU businesses do not need to be charged VAT. Instead, under the VAT reverse
charge mechanism, you provide them with an invoice listing the price of your
digital services, and they are responsible for figuring out the VAT due and
paying it, according to their normal accounting practices.

The way to determine if a customer in the EU is a business is to validate their
VAT ID.

VAT IDs should contain the two-character country code. See
http://en.wikipedia.org/wiki/VAT_identification_number for more info.

The VAT ID can have spaces, dashes or periods within it. Some basic formatting
checks are done to prevent expensive HTTP calls to the web services that
validate the numbers. However, extensive checksum are not validated. If the
format looks fairly correct, it gets sent along to the web server.


```python
import vat_moss.id
import vat_moss.errors
import urllib.error

try:
    result = vat_moss.id.validate('GB GD001')
    if result:
        country_code, normalized_id, company_name = result
        # Do your processing to not charge VAT

except (vat_moss.errors.InvalidError):
    # Make the user enter a new value

except (urllib.error.URLError):
    # There was an error contacting the validation API.
    #
    # Unfortunately this tends to happen a lot with EU countries because the
    # VIES service is a proxy for 28 separate member-state APIs.
    #
    # Tell your customer they have to pay VAT and can recover it
    # through appropriate accounting practices.
```

## Tests

Run the tests via:

```bash
python tests.py
```

## License

MIT License - see the LICENSE file.
