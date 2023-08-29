import pytest
import yaml

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def x_selector_1():
    #Поле ввода username страницы авторизации
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector_2():
    #Поле ввода password страницы авторизации
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector_3():
    #Блок ошибки страницы авторизации
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def x_selector_4():
    """Ссылка на профиль пользователя с выпадающим меню на главной странице"""
    return '//*[@id="app"]/main/nav/ul/li[3]/a'


@pytest.fixture()
def x_selector_5():
    #Поле ввода Title формы создания поста
    return """/html/body/div/main/div/div/form/div/div/div[1]/div/label/input"""


@pytest.fixture()
def x_selector_6():
    #Поле ввода Description формы создания поста
    return """/html/body/div/main/div/div/form/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def x_selector_7():
    #Поле ввода Content формы создания поста
    return """/html/body/div/main/div/div/form/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def x_selector_8():
    #Название поста на странице поста сразу после его создания
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def btn_selector_1():
    #Кнопка Login страницы авторизации
    return 'button'


@pytest.fixture()
def btn_selector_2():
    #Кнопка создания поста на главной странице
    return '#create-btn'


@pytest.fixture()
def btn_selector_3():
    #Кнопка сохранения поста SAVE формы создания поста
    return '.mdc-button__label'


@pytest.fixture()
def expected_result_1():
    #Ожидаемый результат в блоке ошибки при вводе несуществующего пользователя
    return '401'


@pytest.fixture()
def expected_result_2():
    #Ожидаемый результат названия ссылки на профиль пользователя на главной странице
    return f'Hello, {testdata["username"]}'
