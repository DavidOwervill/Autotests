from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import time


class LogInVars:
    # Перечень используемых локаторов в виде переменных
    # XPATH
    log_in_button = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/button"
    log_in_check = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[4]/div[1]/button"
    control_user_name = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/label[2]"
    log_in_failed = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div/p"


class LogInClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_log_in(self, username="TestUserName", password="David123456789!"):
        """
        Данная функция работает на страничке - https://demoqa.com/books.
        Вводятся данные для возможности за логиниться:
        TestUserName
        David123456789!
        Затем проводится проверка авторизации путем сверки НикНейма на страничке https://demoqa.com/books
        """

        # log_in_button = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/button"
        # log_in_check = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[4]/div[1]/button"
        # control_user_name = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/label[2]"
        driver = self.driver
        driver.get("https://demoqa.com/books")
        driver.find_element(by=By.XPATH,
                            value=LogInVars.log_in_button).click()
        time.sleep(3)
        driver.find_element(by=By.ID, value="userName").send_keys(username)
        time.sleep(3)
        driver.find_element(by=By.ID, value="password").send_keys(password)
        time.sleep(3)
        driver.find_element(by=By.XPATH,
                            value=LogInVars.log_in_check).click()
        time.sleep(3)
        try:
            self.assertEqual(username, driver.find_element(by=By.XPATH, value=LogInVars.control_user_name))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_log_in_failed(self, username: str = 11111, password: str = 22222222):
        """
        Данная функция работает на страничке - https://demoqa.com/books.
        Вводятся данные для возможности за логиниться:
        11111
        22222222
        Затем проводится проверка неудачной авторизации
        """
        driver = self.driver
        driver.get("https://demoqa.com/books")
        driver.find_element(by=By.XPATH,
                            value=LogInVars.log_in_button).click()
        time.sleep(3)
        driver.find_element(by=By.ID, value="userName").send_keys(username)
        time.sleep(3)
        driver.find_element(by=By.ID, value="password").send_keys(password)
        time.sleep(3)
        driver.find_element(by=By.XPATH,
                            value=LogInVars.log_in_check).click()
        time.sleep(3)
        try:
            self.assertEqual("Invalid username or password!",
                             driver.find_element(by=By.XPATH, value=LogInVars.log_in_failed))
        except AssertionError as e:
            self.verificationErrors.append(str(e))


if __name__ == '__main__':
    unittest.main()
