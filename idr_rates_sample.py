import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')
json_data = {
    "usd": {"code": "USD", "alphaCode": "USD", "numericCode": "840", "name": "U.S. Dollar", "rate": 7.0895582888144e-5,
            "date": "Mon, 21 Dec 2020 00:00:01 GMT", "inverseRate": 14105.251120902},
    "eur": {"code": "EUR", "alphaCode": "EUR", "numericCode": "978", "name": "Euro", "rate": 5.7870661296172e-5,
            "date": "Mon, 21 Dec 2020 00:00:01 GMT", "inverseRate": 17279.913130458}}
for data in json_data.values() :
    print(data ['code'])
    print(data ['name'])
    print(data ['date'])
    print(data ['inverseRate'])