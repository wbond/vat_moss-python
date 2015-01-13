# VAT MOSS Implementation Approach

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
