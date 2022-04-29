import requests
import json


def print_message(amount, rate, code):
    print(f'You received {round(amount * rate, 2)} {code.upper()}.')


def main():
    my_currency_code = input().lower()
    r = requests.get(f'http://www.floatrates.com/daily/{my_currency_code}.json')
    if my_currency_code.lower() != 'usd':
        exchange_cache = {'usd': json.loads(r.content)['usd']['rate'],
                          'eur': json.loads(r.content)['eur']['rate']}
    else:
        exchange_cache = {'usd': 1,
                          'eur': json.loads(r.content)['eur']['rate']}

    while True:
        receive_currency_code = input().lower()
        if not receive_currency_code:
            break
        my_currency_amount = float(input())
        print(f'Checking the cache...')
        if receive_currency_code in exchange_cache:
            print(f'Oh! It is in the cache!')
            print_message(my_currency_amount, exchange_cache[receive_currency_code], receive_currency_code)
        else:
            print(f'Sorry, but it is not in the cache!')
            exchange_cache[receive_currency_code] = json.loads(r.content)[receive_currency_code]["rate"]
            print_message(my_currency_amount, exchange_cache[receive_currency_code], receive_currency_code)


if __name__ == '__main__':
    main()
