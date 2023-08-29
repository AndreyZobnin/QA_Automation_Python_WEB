import time
import yaml
from module import Site

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)

sleep = testdata['sleep_time']
site = Site(testdata['address'])
name = testdata['username']
passwd = testdata['password']
post_title = testdata['post_title']
post_description = testdata['post_description']
post_content = testdata['post_content']


def test_login_invalid_user(x_selector_1, x_selector_2, btn_selector_1, x_selector_3, expected_result_1):
    #Негативный тест попытки входа на сайт несуществующим пользователем
    input1 = site.find_element('xpath', x_selector_1)
    input1.send_keys('test')

    input2 = site.find_element('xpath', x_selector_2)
    input2.send_keys('test')

    btn = site.find_element('css', btn_selector_1)
    btn.click()

    error_label = site.find_element('xpath', x_selector_3)
    result = error_label.text

    assert result == expected_result_1, 'Test 1 failed'


def test_valid_login(x_selector_1, x_selector_2, btn_selector_1,
                     x_selector_3, x_selector_4,
                     expected_result_1, expected_result_2):
    #Позитивный тест входа на сайт
    input1 = site.find_element('xpath', x_selector_1)
    input1.clear()
    input1.send_keys(name)

    input2 = site.find_element('xpath', x_selector_2)
    input2.clear()
    input2.send_keys(passwd)

    btn = site.find_element('css', btn_selector_1)
    btn.click()

    link = site.find_element('xpath', x_selector_4).text

    assert link == expected_result_2, 'Test 2 failed'


def test_add_post(btn_selector_2, btn_selector_3,
                  x_selector_5, x_selector_6, x_selector_7, x_selector_8):
    #Позитивный тест добавления поста
    btn = site.find_element('css', btn_selector_2)
    time.sleep(sleep)
    btn.click()
    time.sleep(sleep)

    input1 = site.find_element('xpath', x_selector_5)
    input1.clear()
    input1.send_keys(post_title)

    input2 = site.find_element('xpath', x_selector_6)
    input2.clear()
    input2.send_keys(post_description)

    input3 = site.find_element('xpath', x_selector_7)
    input3.clear()
    input3.send_keys(post_content)

    save_btn = site.find_element('css', btn_selector_3)
    save_btn.click()

    time.sleep(sleep)
    post_name = site.find_element('xpath', x_selector_8).text

    site.close()

    assert post_name == post_title, 'Test 3 failed'
