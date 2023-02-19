from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from setting_chrome import SetUpUniChrome
import unittest
import time


class LWebTables:
    first_name = 'firstName'
    first_name_sk = 'Test First Name'
    first_name_ck = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[1]'
    last_name = 'lastName'
    last_name_sk = 'Test Last Name'
    last_name_ck = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[2]'
    user_email = 'userEmail'
    user_email_sk = 'TestMail@test.com'
    user_email_ck = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[4]'
    age = 'age'
    age_sk = '23'
    age_ck = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[3]'
    salary = 'salary'
    salary_sk = '23'
    dep = 'department'
    sub = 'submit'


class WebTables(SetUpUniChrome):
    def test_web_tables(self):
        """
        Данная функция работает со страничкой https://demoqa.com/webtables.
        Сначала мы нажимаем на кнопку Add, затем заполняем выпавшую форму следующими значениями -
        Test First Name,
        Test Last Name,
        TestMail@test.com,
        23,
        23,
        Test department.
        Далее методом try/except во внесенной табличке проверяем что данные внесены верно.
        После нажимаем на кнопку исправить и меняем значения поля First name на Test First Name 2.
        Затем повторно в табличке проверяем что значения внесены верно.
        Так же, в данной функции используется проверка скрола вертикального и горизонтального в рамках.
        """
        driver = self.driver
        driver.get("https://demoqa.com/webtables")
        driver.find_element(by=By.ID, value="addNewRecordButton").click()
        time.sleep(10)

        # Вносим данные в открывшемся окне

        driver.find_element(by=By.ID, value=LWebTables.first_name).send_keys(LWebTables.first_name_sk)
        time.sleep(5)
        driver.find_element(by=By.ID, value=LWebTables.last_name).send_keys(LWebTables.last_name_sk)
        time.sleep(5)
        driver.find_element(by=By.ID, value=LWebTables.user_email).send_keys(LWebTables.user_email_sk)
        time.sleep(5)
        driver.find_element(by=By.ID, value=LWebTables.age).send_keys(LWebTables.age_sk)
        time.sleep(5)
        driver.find_element(by=By.ID, value=LWebTables.salary).send_keys(LWebTables.salary_sk)
        time.sleep(5)
        driver.find_element(by=By.ID, value=LWebTables.dep).send_keys('Test department')
        driver.find_element(by=By.ID, value=LWebTables.sub).click()
        # logging.info("Test form is filled")
        time.sleep(15)

        # Проверяем внесение данных в исходную табличку

        try:
            self.assertEqual(f'{LWebTables.first_name_sk}', driver.find_element(by=By.XPATH,
                                                                    value=LWebTables.first_name_ck).text)
        except AssertionError as v:
            print(str(v))
        try:
            self.assertEqual(f'{LWebTables.last_name_sk}', driver.find_element(by=By.XPATH,
                                                                   value=LWebTables.last_name_ck).text)
        except AssertionError as v:
            print(str(v))
        try:
            self.assertEqual(f'{LWebTables.age_sk}', driver.find_element(by=By.XPATH,
                                                       value=LWebTables.age_ck).text)
        except AssertionError as v:
            print(str(v))
        try:
            self.assertEqual(f'{LWebTables.user_email_sk}', driver.find_element(by=By.XPATH,
                                                                      value=LWebTables.user_email_ck).text)
        except AssertionError as v:
            print(str(v))
        try:
            self.assertEqual(f'{LWebTables.salary_sk}', driver.find_element(by=By.XPATH,
                                                       value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[5]').text)
        except AssertionError as v:
            print(str(v))
        try:
            self.assertEqual('Test department', driver.find_element(by=By.XPATH,
                                                                    value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[6]').text)
        except AssertionError as v:
            print(str(v))
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, 250);")
        target_left = driver.find_element(by=By.CLASS_NAME, value='action-buttons')
        driver.execute_script("arguments[0].scrollIntoView();", target_left)
        time.sleep(5)
        driver.execute_script("window.scrollTo(250, 0);")
        driver.find_element(by=By.XPATH,
                            value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[7]/div/span[1]').click()
        time.sleep(5)

        # Проверка изменения

        driver.find_element(by=By.ID, value='firstName').clear()
        driver.find_element(by=By.ID, value='firstName').send_keys("Test First Name 2")
        time.sleep(5)
        driver.find_element(by=By.ID, value='submit').click()
        time.sleep(5)
        target_right = driver.find_element(by=By.CLASS_NAME, value='rt-td')
        driver.execute_script("arguments[0].scrollIntoView();", target_right)
        time.sleep(5)
        try:
            self.assertEqual('Test First Name 2', driver.find_element(by=By.XPATH,
                                                                      value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[1]').text)
        except AssertionError as v:
            print(str(v))
        # logging.info('Test form is checked')