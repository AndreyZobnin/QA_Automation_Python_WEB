import pytest
import yaml

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser_type = testdata['browser']


@pytest.fixture(scope='session')
def browser():
    if browser_type == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
        driver.maximize_window()
    elif browser_type == 'chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
    elif browser_type == 'edge':
        service = Service(executable_path=EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=service, options=options)
        driver.maximize_window()
    yield driver
    driver.quit()