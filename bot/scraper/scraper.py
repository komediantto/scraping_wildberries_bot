import requests
import urllib.parse


def find_goods(query: str, articul: list):
    answers_list = []
    query = urllib.parse.quote_plus(query)
    try:
        for i in range(1, 101):
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'ru,en;q=0.9',
                'Connection': 'keep-alive',
                'Origin': 'https://www.wildberries.ru',
                'Referer': f'https://www.wildberries.ru/catalog/0/search.aspx?page={i}&sort=popular&search={query}',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36',
                'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            response = requests.get(f'https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&couponsGeo=3,21&curr=rub&dest=-1216601,-103906,-331414,-331412&emp=0&lang=ru&locale=ru&page={i}&pricemarginCoeff=1.0&query={query}&reg=0&regions=82,69,68,86,30,48,1,22,66&resultset=catalog&sort=popular&spp=0&suppressSpellcheck=false', headers=headers).json()
            print(f'Проверяю страницу номер {i}...')
            for index, product in enumerate(response['data']['products']):
                try:
                    if str(product['id']) in articul:
                        if i == 1:
                            x = (f'Страница номер {i}, позиция {index + 3}')
                            answers_list.insert(0, x)
                        else:
                            x = (f'Страница номер {i}, позиция {index + 1}')
                            answers_list.insert(0, x)
                except Exception:
                    print('Товар слишком глубоко(')
    except KeyError:
        pass
    return answers_list
