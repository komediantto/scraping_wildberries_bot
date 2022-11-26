import requests
import urllib.parse
from fake_useragent import UserAgent


ua = UserAgent()


def find_goods(query: str, articul: list, city: str):
    answers_list = []
    query = urllib.parse.quote_plus(query)
    if city == 'Калининград':
        regs = '82,69,68,86,30,48,1,22,66'
    elif city == 'Санкт-Петербург':
        regs = '80,64,83,4,38,33,70,82,69,68,86,30,40,48,1,22,66,31'
    else:
        regs = '80,64,83,4,38,33,70,82,69,68,86,75,30,40,48,1,22,66,31,71'
    try:
        for i in range(1, 101):
            # promo = 1
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'ru,en;q=0.9',
                'Connection': 'keep-alive',
                'Origin': 'https://www.wildberries.ru',
                'Referer': f'https://www.wildberries.ru/catalog/0/search.aspx?page={i}&sort=popular&search={query}',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
                'User-Agent': str(ua.random),
                'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            response = requests.get(f'https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&couponsGeo=3,21&curr=rub&dest=-1216601,-103906,-331414,-331412&emp=0&lang=ru&locale=ru&page={i}&pricemarginCoeff=1.0&query={query}&reg=0&regions={regs}&resultset=catalog&sort=rate&spp=0&suppressSpellcheck=false', headers=headers).json()
            print(f'Проверяю страницу номер {i}...')
            for index, product in enumerate(response['data']['products']):
                if str(product['id']) in articul:
                    x = (f'Артикул { product["id"] } на странице номер {i}, '
                         f'позиция {index + 1}.\nПоиск с сортировкой по '
                         'рейтингу')
                    answers_list.insert(0, x)
    except KeyError:
        pass
    diff = len(set(articul)) - len(answers_list)
    print(diff)
    if diff > 0:
        for _ in range(diff):
            answers_list.append('Артикул отсутствует в поисковой выдаче')
    return answers_list
