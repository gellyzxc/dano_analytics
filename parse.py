import requests
from bs4 import BeautifulSoup
from slugify import slugify
import html
from lxml import etree 

links =  [
    'https://rusdtp.ru/stat-dtp/belgorodskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/bryanskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/vladimirskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/voronezhskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/ivanovskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/kaluzhskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/kostromskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/kurskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/lipeczkaya-oblast/',
    'https://rusdtp.ru/stat-dtp/gor-moskva/',
    'https://rusdtp.ru/stat-dtp/moskovskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/orlovskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/ryazanskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/smolenskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/tambovskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/tverskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/tulskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/yaroslavskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/respublika-kareliya/',
    'https://rusdtp.ru/stat-dtp/respublika-komi/',
    'https://rusdtp.ru/stat-dtp/arhangelskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/vologodskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/kaliningradskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/leningradskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/gor-sankt-peterburg/',
    'https://rusdtp.ru/stat-dtp/murmanskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/novgorodskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/pskovskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/neneczkij-avtonomnyj-okrug/',
    'https://rusdtp.ru/stat-dtp/respublika-adygeya-adygeya/',
    'https://rusdtp.ru/stat-dtp/respublika-kalmykiya/',
    'https://rusdtp.ru/stat-dtp/respublika-krym/',
    'https://rusdtp.ru/stat-dtp/krasnodarskij-kraj/',
    'https://rusdtp.ru/stat-dtp/volgogradskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/rostovskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/astrahanskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/gor-sevastopol/',
    'https://rusdtp.ru/stat-dtp/respublika-dagestan/',
    'https://rusdtp.ru/stat-dtp/respublika-ingushetiya/',
    'https://rusdtp.ru/stat-dtp/kabardino-balkarskaya-respublika/',
    'https://rusdtp.ru/stat-dtp/karachaevo-cherkesskaya-respublika/',
    'https://rusdtp.ru/stat-dtp/respublika-severnaya-osetiya-alaniya/',
    'https://rusdtp.ru/stat-dtp/chechenskaya-respublika/',
    'https://rusdtp.ru/stat-dtp/stavropolskij-kraj/',
    'https://rusdtp.ru/stat-dtp/respublika-bashkortostan/',
    'https://rusdtp.ru/stat-dtp/respublika-marij-el/',
    'https://rusdtp.ru/stat-dtp/respublika-mordoviya/',
    'https://rusdtp.ru/stat-dtp/respublika-tatarstan-tatarstan/',
    'https://rusdtp.ru/stat-dtp/udmurtskaya-respublika/',
    'https://rusdtp.ru/stat-dtp/chuvashskaya-respublika-chuvashiya/',
    'https://rusdtp.ru/stat-dtp/permskij-kraj/',
    'https://rusdtp.ru/stat-dtp/kirovskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/nizhegorodskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/orenburgskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/penzenskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/samarskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/saratovskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/ulyanovskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/kurganskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/sverdlovskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/tyumenskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/chelyabinskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/hanty-mansijskij-avtonomnyj-okrug-yugra/',
    'https://rusdtp.ru/stat-dtp/yamalo-neneczkij-avtonomnyj-okrug/',
    'https://rusdtp.ru/stat-dtp/respublika-altaj/',
    'https://rusdtp.ru/stat-dtp/respublika-tyva/',
    'https://rusdtp.ru/stat-dtp/respublika-hakasiya/',
    'https://rusdtp.ru/stat-dtp/altajskij-kraj/',
    'https://rusdtp.ru/stat-dtp/krasnoyarskij-kraj/',
    'https://rusdtp.ru/stat-dtp/irkutskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/kemerovskaya-oblast-kuzbass/',
    'https://rusdtp.ru/stat-dtp/novosibirskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/omskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/tomskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/respublika-buryatiya/',
    'https://rusdtp.ru/stat-dtp/respublika-saha-yakutiya/',
    'https://rusdtp.ru/stat-dtp/zabajkalskij-kraj/',
    'https://rusdtp.ru/stat-dtp/primorskij-kraj/',
    'https://rusdtp.ru/stat-dtp/kamchatskij-kraj/',
    'https://rusdtp.ru/stat-dtp/habarovskij-kraj/',
    'https://rusdtp.ru/stat-dtp/amurskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/magadanskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/sahalinskaya-oblast/',
    'https://rusdtp.ru/stat-dtp/evrejskaya-avtonomnaya-oblast/',
    'https://rusdtp.ru/stat-dtp/chukotskij-avtonomnyj-okrug/',
    'https://rusdtp.ru/stat-dtp/sirius/',
]
regions = ['Алтайский край', 'Амурская область', 'Архангельская область', 'Астраханская область', 'Белгородская область', 'Брянская область', 'Владимирская область', 'Волгоградская область', 'Вологодская область', 'Воронежская область', 'Забайкальский край', 'Ивановская область', 'Иркутская область', 'Калининградская область', 'Калужская область', 'Камчатский край', 'Кемеровская область', 'Кировская область', 'Костромская область', 'Краснодарский край', 'Красноярский край', 'Курганская область', 'Курская область', 'Ленинградская область', 'Липецкая область', 'Магаданская область', 'Москва', 'Московская область', 'Мурманская область', 'Ненецкий автономный округ', 'Нижегородская область', 'Новгородская область', 'Новосибирская область', 'Омская область', 'Оренбургская область', 'Орловская область', 'Пензенская область', 'Пермский край', 'Приморский край', 'Псковская область', 'Республика Адыгея', 'Республика Алтай', 'Республика Башкортостан', 'Республика Бурятия', 'Республика Калмыкия', 'Республика Карелия', 'Республика Коми', 'Республика Марий Эл', 'Республика Мордовия', 'Республика Саха (Якутия)', 'Республика Татарстан', 'Республика Тыва (Тува)', 'Ростовская область', 'Рязанская область', 'Самарская область', 'Санкт-Петербург', 'Саратовская область', 'Сахалинская область', 'Свердловская область', 'Смоленская область', 'Ставропольский край', 'Тамбовская область', 'Тверская область', 'Томская область', 'Тульская область', 'Тюменская область', 'Удмуртская республика', 'Ульяновская область', 'Хабаровский край', 'Ханты-Мансийский автономный округ', 'Челябинская область', 'Чувашская республика', 'Чукотский автономный округ', 'Ямало-Ненецкий автономный округ', 'Ярославская область']

dtps = {}

for item in links:
    print(item)
    page = requests.get(item)
    data = html.unescape(page.text)
    # print(data)
    soup = BeautifulSoup(data, "html.parser")

    divs = soup.find_all('div', class_="main-death-rate-r-item-row")
    # for div in divs:
    #     if div.get('class') == ['myclass']:
    #     print(div)
    xuis = soup.find_all('div', class_="main-search-item active")
    # print()
    dtps[xuis[0].text] = divs[0].text.strip().split("\n")[1]
    # print(divs[0].text.strip().split("\n")[1])
    # break

print(dtps)
    