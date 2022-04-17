import requests
import datetime

# Для нахождения даты использовал срезы строк, т.к. думаю, что дата всегда будет на одном и том же месте.
# Если это не так, то следует сначала вырезать дату сплитом, а потом уже преобразовывать.


def currency_rates(args):
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    response_2 = (response.text.split('<CharCode>'))
    year = response.text[66:70]
    month = response.text[63:65]
    if month[0] == "0":
        month = month[1]
    day = response.text[60:62]
    if day[0] == "0":
        day = day[1]
    date = datetime.date(int(year), int(month), int(day))
    char_code = args.upper()
    for i in range(0, len(response_2)):
        if response_2[i].startswith(char_code):
            first_half = list(response_2[i].split("<Value>"))
            coast = float(((first_half[1][0:6])).replace(",", "."))
            print(f"{coast}, {date}")
    if char_code not in response.text:
        print("None")


if __name__ == "__main__":
    currency_rates("eur")
