CryptoIQ Tools
==============

Scripts for working with CryptoIQ API

See [CryptoIQ website](https://cryptoiq.io/) for signup.


Environment Variables
---------------------

* `CRYPTOIQ_ACCESS_CODE`: Your CryptoIQ access code.


Usage
------------

All scripts print to stdout. Use redirection to save output to files and
and pipes to provide input to other programs.

### Order Books per Month

Get a month of exchange order books json and print to stdout.

    python orderbooks_month.py <exchange> <asset> <year> <month>

* `exchange`: Exchange supported by API
* `asset`: Asset supported by exchange
* `year`: Year to get from API
* `month`: Month to get from API
