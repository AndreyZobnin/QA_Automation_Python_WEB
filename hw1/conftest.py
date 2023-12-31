import pytest
import yaml
import requests

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    username, password, address_login = data['username'], data['password'], data['url_login']

S = requests.Session()


@pytest.fixture()
def user_login():
    rest1 = S.post(url=address_login, data={'username': username, 'password': password})
    return rest1.json()['token']


@pytest.fixture()
def new_post():
    title = 'Рукокры́лые'
    description = ('"Рукокры́лые"  — Второй по величине (после грызунов) отряд млекопитающих'
                   ' База данных Американского общества маммалогов ')
    content = ('География.\nРукокрылые распространены очень широко. Кроме тундры, приполярных районов и некоторых океанических островов они есть везде. Более многочисленны в тропиках. Рукокрылые являются эндемичными видами на многих океанических островах в отсутствие наземных млекопитающих, так как способны преодолевать большие расстояния над морем.
Плотность расселения летучих мышей в средних широтах — 20—150 на квадратный километр, в Средней Азии — до 1000. При этом до северной границы тайги простираются ареалы не более двух или трёх видов представителей семейства обыкновенные летучие мыши, в южной части США и Средиземноморья видов насчитывается уже несколько десятков, а в бассейнах Конго и Амазонки — несколько сотен видов. Причиной такого резкого увеличения числа видов являются высокая плотность рукокрылых в тропиках и обострение вследствие этого их конкурентных взаимоотношений.
В Москве летучие мыши не только регулярно встречаются в окраинных лесопарках, но даже зимуют в здании университета на Ленинских горах.
В фауне России насчитывается около 40 видов рукокрылых.')
    return title, description, content
