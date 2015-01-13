# VAT MOSS Overview

To ensure a level playing field for EU-based businesses and non-EU-based
businesses, the EU requires non-EU-based businesses to collect VAT on sales of
[digital services](https://www.gov.uk/vat-on-digital-services-in-the-eu) to
consumers located in the EU.

This means any US, Canadian, etc business selling SasS, software licenses,
ebooks, music, or other digital goods needs to collect VAT. Thankfully on
January 1st, 2015, the concept of the VAT Mini One-Stop-Shop was introduced.
This allows companies to register with a single EU country (member state) and
submit all VAT tax money collected to that one country. Otherwise businesses
would have to submit returns to 28 different countries.

Unfortunately, it isn't that simple. Not only do you have to collect VAT, you
have to do it at 28 different tax rates and collect multiple pieces of
non-contradictory location proof to justify why you are charging the rate you
are.

Oh, and EU businesses will provide you with a VAT ID, which you need to validate
against an ancient SOAP web service that is actually a proxy to 28 different
web services. Unfortunately the connection to those other web services goes down
a lot, so you will get HTTP 500 errors regularly. Anyway, if your customer does
provide a valid VAT ID, you should not collect VAT from them.

Did I mention that in addition to there being 28 different countries in the EU
with different VAT tax rates, there are also a handful of cities and regions in
those countries that are exempt from VAT, or have a special VAT rate?

Finally, for consumers in some EU countries, but all EU businesses, you need to
issue a VAT-compatible invoice. Lucky us, there isn't a single standard for what
needs to be on a VAT invoice. Instead each country can have its own
requirements.

Then, four times a year you need to submit a return listing all of the sales
you made to consumers in the EU, broken down by country and tax rate. Once you
submit that, you have to send an international wire transfer from your bank to a
bank in a foreign country. Apparently if you are located in the EU, this is a
relatively simple, and inexpensive process. In the US, most banks charge between
$40-60 per wire transfer, and have kinda crappy exchange rates.

One last thing. Norway has their own VAT on e-Services setup since they are not
part of the EU. At least they only require registering if you sell more than
$7,000 of services to consumers in Norway. Collecting VAT for customers in the
EU is required from your first sale.

## Selling Knowledge, One Transaction at a Time

There are quite a number of SaaS companies out there that are willing to help
with *some* parts of this process. And they'll charge somewhere between 2-5% of
your sales price for it. Some even want a flat monthly fee in addition to
per-transaction fees. I wasn't really keen on paying that much, especially
since it wasn't terribly clear to me exactly what value they were providing.

It is clear to me that plenty of businesses suddenly realized they to deal with
VAT on digital services to EU customers. Some of the SaaS providers in the VAT
MOSS market seem to be focusing their marketing around fear and uncertainty.

For some businesses, I am sure that there are SaaS solutions that make perfect
sense. Especially if you are just starting out and don't have established
systems in place for licensing, downloads, etc. There are even services that
will take a bigger chunk of your income, and will sub-license your digital
goods, absolving you of any sort of EU tax liability.

However, it also seemed to me that many of these companies were really selling
knowledge, wrapped up as software solutions. The uncertainty is more around:

 - How to I determine where a customer is located?
 - How do I tell if a customer is a business?
 - What tax rate do I charge the customer?
 - What are the invoice requirements for sales to EU businesses and consumers?

## Original Research, For You

I have spent quite a bit of time researching how to abide by these tax laws. My
hope is that my research will help a bunch of other companies understand what
is going on and give them enough information (and open-source code) to make
informed dicisions on how to deal with the EU/Norway and VAT for digital
services.

## Disclaimer

I am not a tax lawyer. I am a software engineer and entreprenuer. Do not take
tax advice from me. I provide no warranty or guarantee about this information,
whether explicit or implied. I am not responsible for any damages, liability
or claims arising from or in connection with using the information or code I
provide.

*Guess what, those SaaS solutions don't guarantee anything either.*

## Definitions

Here are a few terms that will be useful when discussing VAT MOSS:

 - **Place of Supply**: when providing digital services, the place of supply is
   the normal location of residence of the consumer. The place of supply is
   a concept from EU VAT law. It determines what tax rate is used and what
   invoice requirements you must follow.
 - **Reverse Charge**: when selling digital services to businesses, you do not
   need to charge VAT or collect place of supply proof. Instead, the business
   itself will end up dealing with the VAT. This is known as a "reverse charge".
 - **Non-Union Scheme**: when a business selling digital goods is not located
   in the EU. EU-based businesses much follow the *Union Scheme*.

## Norway and Switzerland

Norway and Switzerland are not part of the EU, but have their own VAT systems.

The `vat_moss` Python library includes support for Norway VAT on e-services,
however you do not need to register for, or collect it, unless you sell at
least $7,000 worth of services to Norwegian consumers in a year. You can learn
more about it at http://www.voesnorway.com/.

Recently, the Swiss government [issued a statement](https://www.news.admin.ch/message/index.html?lang=en&msg-id=55183)
indicating that foreign companies only providing e-services to Swiss consumers
will be exempt from tax liability. This is good news, considering that it
appears you have to hire a Swiss tax representative if you are a foreign
company and need to pay Swiss taxes.

## VAT MOSS Registration

You need to pick a country to register for VAT MOSS with. Personally I chose
Great Britian since the [HMRC](https://www.gov.uk/government/organisations/hm-revenue-customs)
seems to have a bunch of documentation about VAT MOSS and since they speak
English. Most of my information about details is pulled from them and their
guidance.

It took about 24 hours for HMRC to create a registration for my US-based
business. They did ask a question about the nature of what I was selling.

[Register with the HMRC](https://online.hmrc.gov.uk/registration/organisation/moss/introduction). If you are not located in the EU, you want to register for the
*Non-Union Scheme*. Also, make sure you save your numeric User ID when you first
register for the British government services. You need that to log in.

## Place of Supply Proof

For each sale you need to have two pieces of non-contradictory place of supply
proof. This can be any of the following:

 - Billing address
 - Self-declared location of residence
 - Phone number mapped to country/region
 - IP address w/ geolocation
 - Country of issuing bank for credit card (PayPal does not provide)

Unless you do some work to authorize a credit card before capture and don't use
PayPal, the country of issuing bank is not very helpful. A user's IP address
and phone number alone aren't specific enough to handle a number of the regions
exempt from VAT, since they are individual cities.

The `vat_moss` Python library helps in mapping the first four options to VAT
rates, including handling of all of the exceptions.

## Invoices

[Some countries don't require a VAT invoice for consumer purchases](http://www.taxamo.com/moss-invoicing-revealed/),
but some of your purchases will almost certainly be from businesses, so you need
to have these invoices set up anyway. Might as well provide them to everyone so
that if a business can't validate their ID through VIES, they don't have to ask
you for a one-off invoice.

When a business provides a valid VAT ID, the "reverse charge" rule applies. This
means you should not charge the business any VAT, but instead they will account
for the VAT due using their normal account practices.

To satisfy invoice requirements in all countries you need to include:

 - The word "Invoice"
 - Sequential invoice number
 - The word "Original"
 - Date
 - If issuing a refund, a reference to the original invoice number
 - Your VAT ID from registering for HMRC VAT MOSS - mine starts with "EU"
 - Your name and address
 - Customer VAT ID, if provided (only businesses have these)
 - Customer name and address
 - A listing of goods: name, quantity, unit price, total price (both VAT exclusive)
 - Date of supply
 - Amount taxable in payment currency (e.g. USD)
   - BG: Taxable amount in BGN also
 - Any discounts to the amount and the rate of discount
 - For customers with a valid VAT ID:
   - Do not charge VAT or show it on the invoice
   - Include the note "Reverse charge applies - purchaser responsible for VAT" instead. Certain countries
     have special wording required:
     - BE: "VAT to be accounted for by the recipient - article 51, § 2 of the Belgian VAT code"
     - GB: "Customer to pay output tax of £{AMOUNT} to HMRC"
 - For customers without a VAT ID:
    - The VAT rate applied
    - VAT tax amount in payment currency (e.g. USD) and EUR (Euro). Countries
      with their own currency require the VAT amount in that currency instead
      of EUR. Include a note of the exchange rate being calculated via the ECB
      including date published.
      - BG: BGN (Bulgarian Lev)
      - HR: HRK (Croatian Kuna)
      - CZ: CZK (Czech Koruna)
      - DK: DKK (Danish Krone)
      - GB: GBP (British Pound Sterling)
      - HU: HUF (Hungarian Forint)
      - PL: PLN (Polish Złoty)
      - RO: RON (Romanian Leu)
      - SE: SEK (Swedish Krona)
 - Total amount payable in payment currency (e.g. USD)

Amounts shown in a currency other than the payment currency should use the
rate published by the ECB at the time of the transaction.

This information is pulled from Article 226 of the EU Directive 2006/112/EC
http://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32006L0112&from=EN.
Some details were obtained from
http://www.kpmg.com/Global/en/IssuesAndInsights/ArticlesPublications/vat-gst-essentials/Pages/default.aspx.

## MOSS Returns

According to
http://www.ion.icaew.com/ClientFiles/c1db2be4-7bd5-41f3-996a-764f237080bb/MOSS%20Helpsheet%203%20QandAs.pdf
the return will need to include the following:

 - Member state of consumption
 - VAT rate type, standard or reduced (always standards for e-services)
 - VAT rate in member state
 - Total net value of supplies

When it is time to file the return, they will provide Excel and Libre Office
templates. I suppose we shall see the details then.

The HMRC system will use the information listed above plus the European Central
Bank exchange rate information from the last day of the quarter the return is
for to translate values not in GBP to GBP. However, if you are generating
invoices for customers (which you probably should be since businesses require
them), you can record the GBP value of the VAT collected based on the ECB rate
the date the purchase is made, and use that when submitting your quarterly
payments. Information about this obtained from
https://www.gov.uk/register-and-use-the-vat-mini-one-stop-shop.

You will then have to pay the amount specified via bank/wire transfer. This
could cost $40-$60 if you have a US bank. Other payment options to look at
include:

 - http://www.usforex.com/our-services/transfer-money/europe
 - https://www.xoom.com/united-kingdom/send-money
 - https://transferwise.com/us1

## Merchandise Returns/Chargebacks

In order to get VAT refunded to you when you give users returns or when
chargebacks occur, you will have to file an ammended return with corrections to
the HMRC. See
http://www.ion.icaew.com/ClientFiles/c1db2be4-7bd5-41f3-996a-764f237080bb/MOSS%20Helpsheet%203%20QandAs.pdf
for questions and answers related to this.

*I have no idea how the UK government will send money back to US businesses. It
probably isn't worth the hastle unless the corrections are significant in
value.*
