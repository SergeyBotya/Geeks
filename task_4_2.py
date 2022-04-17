import requests


def currency_rates(args):
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    response_2 = (response.text.split('<CharCode>'))
    char_code = args.upper()
    for i in range(0, len(response_2)):
        if response_2[i].startswith(char_code):
            first_half = list(response_2[i].split("<Value>"))
            coast = float(((first_half[1][0:6])).replace(",", "."))
            print(coast)
    if char_code not in response.text:
        print("None")

currency_rates("usd")