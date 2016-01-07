import argparse
import os
from six.moves.urllib.parse import urlunparse, urljoin
from datetime import date, timedelta
import calendar
import requests
from collections import OrderedDict
from six import print_
import json


parser = argparse.ArgumentParser()
parser.add_argument('exchange')
parser.add_argument('asset')
parser.add_argument('year', type=int)
parser.add_argument('month', type= int)
args = parser.parse_args()

access_code = os.environ['CRYPTOIQ_ACCESS_CODE']

base_path = 'api/marketdata/orderbooktop/'
def get_order_book_url(d, hour):
    api_path = '/'.join((args.exchange, args.asset, str(d), str(hour)))
    path = urljoin(base_path, api_path)
    
    parts = (
        'https',
        'cryptoiq.io',
        path,
        None,
        'sac=' + access_code,
        None
    )
    return urlunparse(parts)


# generate hourly UTC datetimes between start date and yesterday's date
start = date(args.year, args.month, 1)
days = calendar.monthrange(start.year, start.month)[1]
dates = [start + timedelta(days=x) for x in range(0, days)]

session = requests.Session()
session.mount("https://", requests.adapters.HTTPAdapter(max_retries=1))
for d in dates:
    for hour in range(0, 24):
        url = get_order_book_url(d, hour)
        books = session.get(url).json(object_pairs_hook=OrderedDict)
        for book in books:
            print_(json.dumps(book))
