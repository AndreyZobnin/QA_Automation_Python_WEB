import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


class Site:
    def __init__(self, address):
        match browser:
            case 'firefox':
                service = Service(executable_path=GeckoDriverManager().install())
                options = webdriver.FirefoxOptions()
                self.driver = webdriver.Firefox(service=service, options=options)
            case 'chrome':
                service = Service(executable_path=ChromeDriverManager().install())
                options = webdriver.ChromeOptions()
                self.driver = webdriver.Chrome(service=service, options=options)
            case 'edge':
                service = Service(executable_path=EdgeChromiumDriverManager().install())
                options = webdriver.EdgeOptions()
                self.driver = webdriver.Edge(service=service, options=options)
        self.driver.implicitly_wait(testdata['implicitly_wait'])
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(testdata['sleep_time'])

    def find_element(self, mode, path):
        match mode:
            case 'css':
                element = self.driver.find_element(By.CSS_SELECTOR, path)
            case 'xpath':
                element = self.driver.find_element(By.XPATH, path)
            case _:
                element = None
        return element

    def get_element_property(self, mode, path, el_property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(el_property)

    def close(self):
        self.driver.close()
