from selenium import webdriver
import unittest


class SetUpUniChrome(unittest.TestCase):
    def setUp(self):
        # настройка для не открывающегося окна браузера
        # self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless")
        # конец настройки неоткрывающегося окна
        self.driver = webdriver.Chrome() #options=self.chrome_options
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
