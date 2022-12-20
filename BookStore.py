from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest, time, re, logging, doctest

# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select


service = Service(executable_path="Users/User/Desktop/GIT/Autotests/drivers")
driver = webdriver.Chrome(service=service)
test_link = "https://demoqa.com/books"
test_link_text_box = "https://demoqa.com/text-box"
test_link_check_box = "https://demoqa.com/checkbox"

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w", format="%(asctime)s %(levelname)s %(message)s")

logging.info("This is an info message")
logging.warn("This is a warning message")
logging.debug("This is a debug message")
logging.error("This is an error message")

class BookStore(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

# driver.get_screenshot_as_file("homepage.png")
# driver.save_screenshot("myscreenshot.png")


# Тестирование login

    def test_log_in(self):
        driver = self.driver
        driver.get(
             test_link)
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/button").click()
        driver.implicitly_wait(60)
        driver.find_element(by=By.ID, value="userName").send_keys("TestUserName")
        driver.implicitly_wait(60)
        driver.find_element(by=By.ID, value="password").send_keys("David123456789!")
        driver.implicitly_wait(60)
        logging.info("Заходим в тестовый профиль")
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[4]/div[1]/button").click()
        driver.implicitly_wait(60)
        counter = 0
        counter += 1
        driver.get_screenshot_as_png()
        driver.save_screenshot(f"login{counter}.png")
        try:
            self.assertEqual("TestUserName", driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/label[2]"))
        except AssertionError as e:
                 self.verificationErrors.append(str(e))
        logging.info("Тест вхождения в профиль пройден успешно")

    def test_books_open(self):
        driver = self.driver
        driver.get(
            test_link)
        driver.find_element(by=By.ID, value="see-book-Git Pocket Guide").click()
        driver.implicitly_wait(30)
        try:
            self.assertEqual("9781449325862", driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        counter = 0
        counter += 1
        driver.get_screenshot_as_png()
        driver.save_screenshot(f"booksOpen{counter}.png")
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div/button").click()
        driver.implicitly_wait(30)
        driver.find_element(by=By.ID, value="see-book-Learning JavaScript Design Patterns").click()
        driver.implicitly_wait(30)
        try:
            self.assertEqual("9781449331818", driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        counter += 1
        driver.get_screenshot_as_png()
        driver.save_screenshot(f"booksOpen{counter}.png")
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.find_element(by=By.XPATH,
                            value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div/button").click()
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.implicitly_wait(30)
        driver.find_element(by=By.ID, value="see-book-Designing Evolvable Web APIs with ASP.NET").click()
        driver.implicitly_wait(30)
        try:
            self.assertEqual("9781449337711", driver.find_element(by=By.XPATH,
                                                                  value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        counter += 1
        driver.get_screenshot_as_png()
        driver.save_screenshot(f"booksOpen{counter}.png")
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.find_element(by=By.XPATH,
                            value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div/button").click()
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.implicitly_wait(30)
        driver.find_element(by=By.ID, value="see-book-Speaking JavaScript").click()
        driver.implicitly_wait(30)
        try:
            self.assertEqual("9781449365035", driver.find_element(by=By.XPATH,
                                                                  value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        counter += 1
        driver.get_screenshot_as_png()
        driver.save_screenshot(f"booksOpen{counter}.png")
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.find_element(by=By.XPATH,
                            value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div/button").click()
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.implicitly_wait(30)
        driver.find_element(by=By.ID, value="see-book-You Don't Know JS").click()
        driver.implicitly_wait(30)
        try:
            self.assertEqual("9781491904244", driver.find_element(by=By.XPATH,
                                                                  value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        counter += 1
        driver.get_screenshot_as_png()
        driver.save_screenshot(f"booksOpen{counter}.png")
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.find_element(by=By.XPATH,
                            value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div/button").click()
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.implicitly_wait(30)
        logging.info("Тест на проверку содержимого книжного магазина выполнен успешно")

    def test_text_box(self):
        driver = self.driver
        driver.get(
            test_link_text_box)
        driver.find_element(by=By.ID, value="userName").send_keys("Full Name Test Write")
        driver.find_element(by=By.ID, value="userEmail").send_keys("testmail@gmail.com")
        driver.find_element(by=By.ID, value="currentAddress").send_keys("Test Current Address")
        driver.find_element(by=By.ID, value="permanentAddress").send_keys('Test Permanent Address')
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.find_element(by=By.ID, value="submit").click()
        time.sleep(30)
        try:
            self.assertEqual("Name:Full Name Test Write", driver.find_element(by=By.XPATH, value="//*[@id='name']").text)
        except ValueError as e:
            print(str(e))
        logging.info("Check User Name")
        try:
            self.assertEqual("Email:testmail@gmail.com", driver.find_element(by=By.XPATH, value="//*[@id='email']").text)
        except ValueError as e:
            print(str(e))
        logging.info("Check Email")
        try:
            self.assertEqual("Current Address :Test Current Address", driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[3]").text)
        except ValueError as e:
            print(str(e))
        logging.info("Check Current Address")
        try:
            self.assertEqual("Permananet Address :Test Permanent Address", driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[4]").text)
        except ValueError as e:
            print(str(e))
        logging.info("Check permanent address")


    def test_check_box(self):
        driver = self.driver
        driver.get(
            test_link_check_box)
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/span/label/span[1]").click()
        try:
            self.assertEqual("home", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        time.sleep(5)
        # Опускаемся на 1 слой глубже
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/span/label/span[1]").click()
        driver.find_element(by=By.CSS_SELECTOR, value='.rct-collapse.rct-collapse-btn').click()
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[1]/span/label/span[1]").click()
        try:
            self.assertEqual("desktop", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info('Desktop checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[1]/span/label/span[1]").click()
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[2]/span/label/span[1]").click()
        try:
            self.assertEqual("documents", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info('Documents checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[2]/span/label/span[1]").click()
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[3]/span/label/span[1]").click()
        try:
            self.assertEqual("downloads", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info('Downloads checked')
        time.sleep(5)
        # Опускаемся на 1 слой глубже в разделе Desktop
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[3]/span/label/span[1]").click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[1]/span/button').click()
        # Опустились
        logging.info('Down to the Desktop level')
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]").click()
        try:
            self.assertEqual("notes", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info('Notes checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]").click()
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[2]/span/label/span[1]").click()
        try:
            self.assertEqual("commands", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info('Commands checked')
        time.sleep(5)
        # Следующим действием выходим из destop
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[2]/span/label/span[1]").click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[1]/span/button').click()
        logging.info('Down to the Documents level')
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/span/button').click()
        # Опустились на уровень Documents
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/span/label/span[1]").click()
        try:
            self.assertEqual("workspace", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info("WorkSpace checked")
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/span/label/span[1]").click()
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/span/label/span[1]").click()
        try:
            self.assertEqual("office", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info("Office checked")
        # Проваливаемся на 1 уровень ниже в рамках Documents
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/span/label/span[1]").click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/button').click()
        # Работаем со вложением WorkSpace
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[1]/span/label/span[1]').click()
        try:
            self.assertEqual("react", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info('React checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[1]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[2]/span/label/span[1]').click()
        try:
            self.assertEqual("angular", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info('Angular checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[2]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[3]/span/label/span[1]').click()
        try:
            self.assertEqual("vue", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info('Vue Checked')
        time.sleep(5)
        # Выходим из уровня workspace
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[3]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/span/button').click()
        # Работаем с уровнем Office
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[1]/span/label/span[1]').click()
        try:
            self.assertEqual("public", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info('public checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[1]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[2]/span/label/span[1]').click()
        try:
            self.assertEqual("private", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info('Private was checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[2]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[3]/span/label/span[1]').click()
        try:
            self.assertEqual("classified", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info('Classified was checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[3]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[4]/span/label/span[1]').click()
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        try:
            self.assertEqual("general", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info('General was checked')
        time.sleep(5)
        # Выходим из уровня Office
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[4]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/span/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/button').click()
        # Падаем в уровень Downloads
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[3]/span/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]').click()
        try:
            self.assertEqual("wordFile", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info('Word File checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[2]/span/label/span[1]').click()
        try:
            self.assertEqual("excelFile", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]"))
        except AssertionError as e:
            print(str(e))
        logging.info('Excel File checked')
        time.sleep(5)















    # def is_element_present(self, how, what):
    #
    #     try:
    #         self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e:
    #         return False
    #     return True

    # def is_alert_present(self):
    #     try:
    #         self.driver.switch_to_alert()
    #     except NoAlertPresentException as e:
    #         return False
    #     return True

    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally:
    #         self.accept_next_alert = True

    # def tearDown(self):
    #     # To know more about the difference between verify and assert,
    #     # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
    #     self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    x = BookStore()
    x.test_log_in()

