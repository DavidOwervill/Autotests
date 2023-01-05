from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re, logging, doctest
from datetime import datetime


# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# driver.get_screenshot_as_file("homepage.png")
# driver.save_screenshot("myscreenshot.png")

# Перечень переменных со ссылками на проверяемые странички

service = Service(executable_path="Users/User/Desktop/GIT/Autotests/drivers")
driver = webdriver.Chrome(service=service)
test_link = "https://demoqa.com/books"
test_link_text_box = "https://demoqa.com/text-box"
test_link_check_box = "https://demoqa.com/checkbox"
test_link_radio_button = "https://demoqa.com/radio-button"
test_link_web_table = "https://demoqa.com/webtables"
test_link_buttons = 'https://demoqa.com/buttons'
test_link_links = "https://demoqa.com/links"
test_link_broken = "https://demoqa.com/broken"
test_link_upload_download = "https://demoqa.com/upload-download"


# Настройка логов
now_data = datetime.now().date()
logging.basicConfig(level=logging.INFO, filename=f"py_log_{now_data}.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.debug("This is a debug message")
# logging.error("This is an error message")


class ToolsQA(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_log_in(self):
        """
        Данная функция работает на страничке - https://demoqa.com/books.
        Вводятся данные для возможности за логиниться:
        TestUserName
        David123456789!
        Затем проводится проверка авторизации путем сверки НикНейма на страничке https://demoqa.com/books
        """
        driver = self.driver
        driver.get(
            test_link)
        driver.find_element(by=By.XPATH,
                            value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/button").click()
        driver.implicitly_wait(60)
        driver.find_element(by=By.ID, value="userName").send_keys("TestUserName")
        driver.implicitly_wait(60)
        driver.find_element(by=By.ID, value="password").send_keys("David123456789!")
        driver.implicitly_wait(60)
        logging.info("Заходим в тестовый профиль")
        driver.find_element(by=By.XPATH,
                            value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[4]/div[1]/button").click()
        driver.implicitly_wait(60)
        counter = 0
        counter += 1
        driver.get_screenshot_as_png()
        driver.save_screenshot(f"login{counter}.png")
        try:
            self.assertEqual("TestUserName", driver.find_element(by=By.XPATH,
                                                                 value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/label[2]"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        logging.info("Тест вхождения в профиль пройден успешно")

    def test_books_open(self):
        """
        Данная функция работает с https://demoqa.com/books.
        В данной функции мы проверяем содержимое книжного магазина выбирая последовательно все книги на сайте
        и сверяем с первой строчкой в карточке ISBN, что бы проверить что открыта именно данная вкладка.
        В разработке добавления сверки URL.
        Так же, данная функция делает скриншот после выполнения проверки каждой книги. Данная функция введена для
        визуального контроля карточки товара.
        """
        driver = self.driver
        driver.get(
            test_link)
        driver.find_element(by=By.ID, value="see-book-Git Pocket Guide").click()
        time.sleep(3)
        try:
            self.assertEqual("9781449325862", driver.find_element(by=By.XPATH,
                                                                  value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        counter = 0
        counter += 1
        driver.get_screenshot_as_png()
        driver.save_screenshot(f"booksOpen{counter}.png")
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.find_element(by=By.XPATH,
                            value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div/button").click()
        time.sleep(3)
        driver.find_element(by=By.ID, value="see-book-Learning JavaScript Design Patterns").click()
        time.sleep(3)
        try:
            self.assertEqual("9781449331818", driver.find_element(by=By.XPATH,
                                                                  value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        counter += 1
        driver.get_screenshot_as_png()
        driver.save_screenshot(f"booksOpen{counter}.png")
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.find_element(by=By.XPATH,
                            value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div/button").click()
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        time.sleep(3)
        driver.find_element(by=By.ID, value="see-book-Designing Evolvable Web APIs with ASP.NET").click()
        time.sleep(3)
        try:
            self.assertEqual("9781449337711", driver.find_element(by=By.XPATH,
                                                                  value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        counter += 1
        driver.get_screenshot_as_png()
        driver.save_screenshot(f"booksOpen{counter}.png")
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.find_element(by=By.XPATH,
                            value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div/button").click()
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        time.sleep(3)
        driver.find_element(by=By.ID, value="see-book-Speaking JavaScript").click()
        time.sleep(3)
        try:
            self.assertEqual("9781449365035", driver.find_element(by=By.XPATH,
                                                                  value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        counter += 1
        driver.get_screenshot_as_png()
        driver.save_screenshot(f"booksOpen{counter}.png")
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.find_element(by=By.XPATH,
                            value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div/button").click()
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        time.sleep(3)
        driver.find_element(by=By.ID, value="see-book-You Don't Know JS").click()
        time.sleep(3)
        try:
            self.assertEqual("9781491904244", driver.find_element(by=By.XPATH,
                                                                  value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/label").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        counter += 1
        driver.get_screenshot_as_png()
        driver.save_screenshot(f"booksOpen{counter}.png")
        driver.execute_script("window.scrollTo(0, 350);")
        time.sleep(3)
        button_back_to_the_store = driver.find_element(by=By.XPATH,
                                                       value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[9]/div/button")
        driver.execute_script("arguments[0].click();", button_back_to_the_store)
        time.sleep(3)
        logging.info("Bookstore content verification test completed successfully")

    def test_text_box(self):
        """
        Данная функция работает со страничкой https://demoqa.com/text-box.
        Сначала заполняем форму следующими значениями -
        Full Name Test Write,
        testmail@gmail.com,
        Test Current Address,
        Test Permanent Address.
        Затем осуществляем последовательную проверку внесенных значений.
        """
        driver = self.driver
        driver.get(
            test_link_text_box)
        driver.find_element(by=By.ID, value="userName").send_keys("Full Name Test Write")
        time.sleep(3)
        driver.find_element(by=By.ID, value="userEmail").send_keys("testmail@gmail.com")
        time.sleep(3)
        driver.find_element(by=By.ID, value="currentAddress").send_keys("Test Current Address")
        time.sleep(3)
        driver.find_element(by=By.ID, value="permanentAddress").send_keys('Test Permanent Address')
        time.sleep(3)
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.find_element(by=By.ID, value="submit").click()
        time.sleep(10)
        try:
            self.assertEqual("Name:Full Name Test Write",
                             driver.find_element(by=By.XPATH, value="//*[@id='name']").text)
        except ValueError as e:
            print(str(e))
        logging.info("Check User Name")
        try:
            self.assertEqual("Email:testmail@gmail.com",
                             driver.find_element(by=By.XPATH, value="//*[@id='email']").text)
        except ValueError as e:
            print(str(e))
        logging.info("Check Email")
        try:
            self.assertEqual("Current Address :Test Current Address", driver.find_element(by=By.XPATH,
                                                                                          value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[3]").text)
        except ValueError as e:
            print(str(e))
        logging.info("Check Current Address")
        try:
            self.assertEqual("Permananet Address :Test Permanent Address", driver.find_element(by=By.XPATH,
                                                                                               value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[4]").text)
        except ValueError as e:
            print(str(e))
        logging.info("Check permanent address")

    def test_check_box(self):
        """
        Данная функция работает с https://demoqa.com/checkbox.
        В данной функции последовательно проверяется нажатие на галочку возле соответствующей директории и
        возможность попасть внутрь.
        Порядок проверки следующий - Home -> Desktop -> Documents -> Downloads -> Notes ->Commands->
        WorkSpace -> Office -> React -> Angular -> Vue -> Public -> Private -> Classified -> General ->
        Word file.doc -> Excel File.doc
        """
        driver = self.driver
        driver.get(
            test_link_check_box)
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/span/label/span[1]").click()
        try:
            self.assertEqual("home", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except NoSuchElementException as e:
            print(str(e))
        time.sleep(5)

        # Опускаемся на 1 слой глубже

        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/span/label/span[1]").click()
        driver.find_element(by=By.CSS_SELECTOR, value='.rct-collapse.rct-collapse-btn').click()
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[1]/span/label/span[1]").click()
        try:
            self.assertEqual("desktop", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except NoSuchElementException as e:
            print(str(e))
        logging.info('Desktop checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[1]/span/label/span[1]").click()
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[2]/span/label/span[1]").click()
        try:
            self.assertEqual("documents", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except NoSuchElementException as e:
            print(str(e))
        logging.info('Documents checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[2]/span/label/span[1]").click()
        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[3]/span/label/span[1]").click()
        try:
            self.assertEqual("downloads", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except AssertionError as e:
            print(str(e))
        logging.info('Downloads checked')
        time.sleep(5)

        # Опускаемся на 1 слой глубже в разделе Desktop

        driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[3]/span/label/span[1]").click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[1]/span/button').click()

        # Опустились

        logging.info('Down to the Desktop level')
        driver.find_element(by=By.XPATH,
                            value="//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]").click()
        try:
            self.assertEqual("notes", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except AssertionError as e:
            print(str(e))
        logging.info('Notes checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value="//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]").click()
        driver.find_element(by=By.XPATH,
                            value="//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[2]/span/label/span[1]").click()
        try:
            self.assertEqual("commands", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except AssertionError as e:
            print(str(e))
        logging.info('Commands checked')
        time.sleep(5)

        # Следующим действием выходим из desktop

        driver.find_element(by=By.XPATH,
                            value="//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[2]/span/label/span[1]").click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[1]/span/button').click()
        logging.info('Down to the Documents level')
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/span/button').click()

        # Опустились на уровень Documents

        driver.find_element(by=By.XPATH,
                            value="//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/span/label/span[1]").click()
        try:
            self.assertEqual("workspace", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except AssertionError as e:
            print(str(e))
        logging.info("WorkSpace checked")
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value="//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/span/label/span[1]").click()
        driver.find_element(by=By.XPATH,
                            value="//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/span/label/span[1]").click()
        try:
            self.assertEqual("office", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except AssertionError as e:
            print(str(e))
        logging.info("Office checked")

        # Проваливаемся на 1 уровень ниже в рамках Documents

        driver.find_element(by=By.XPATH,
                            value="//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/span/label/span[1]").click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/button').click()

        # Работаем со вложением WorkSpace

        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[1]/span/label/span[1]').click()
        try:
            self.assertEqual("react", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except AssertionError as e:
            print(str(e))
        logging.info('React checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[1]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[2]/span/label/span[1]').click()
        try:
            self.assertEqual("angular", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except AssertionError as e:
            print(str(e))
        logging.info('Angular checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[2]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[3]/span/label/span[1]').click()
        try:
            self.assertEqual("veu", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except AssertionError as e:
            print(str(e))
        logging.info('Veu Checked')
        time.sleep(5)

        # Выходим из уровня workspace

        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[3]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/span/button').click()

        # Работаем с уровнем Office

        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[1]/span/label/span[1]').click()
        try:
            self.assertEqual("public", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except AssertionError as e:
            print(str(e))
        logging.info('public checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[1]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[2]/span/label/span[1]').click()
        try:
            self.assertEqual("private", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except AssertionError as e:
            print(str(e))
        logging.info('Private was checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[2]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[3]/span/label/span[1]').click()
        try:
            self.assertEqual("classified", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except AssertionError as e:
            print(str(e))
        logging.info('Classified was checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[3]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[4]/span/label/span[1]').click()
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        try:
            self.assertEqual("general", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except AssertionError as e:
            print(str(e))
        logging.info('General was checked')
        time.sleep(5)

        # Выходим из уровня Office

        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[4]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/span/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/button').click()

        # Падаем в уровень Downloads

        driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[3]/span/button').click()
        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]').click()
        try:
            self.assertEqual("wordFile", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except AssertionError as e:
            print(str(e))
        logging.info('Word File checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]').click()
        driver.find_element(by=By.XPATH,
                            value='//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[2]/span/label/span[1]').click()
        try:
            self.assertEqual("excelFile", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
        except AssertionError as e:
            print(str(e))
        logging.info('Excel File checked')
        time.sleep(5)

    def test_radio_button(self):
        """
        Данная функция работает с сайтом https://demoqa.com/radio-button.
        Проверяет нажатие на кнопку Yes, Impressive.
        Кнопка No не действительна.
        Так же в случае попадания функции в except выполняет скриншот.

        """
        driver = self.driver
        driver.get(
            test_link_radio_button)
        counter = 0
        driver.find_element(by=By.CLASS_NAME, value="custom-control-label").click()
        time.sleep(15)
        try:
            self.assertEqual("You have selected Yes", driver.find_element(by=By.XPATH,
                                                                          value="//*[@id='app']/div/div/div[2]/div[2]/div[2]/p").text)
        except AssertionError as v:
            print(str(v))
            counter += 1
            driver.get_screenshot_as_png()
            driver.save_screenshot(f"RadioButton{counter}.png")

        driver.find_element(by=By.XPATH, value="//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/label").click()
        time.sleep(15)
        try:
            self.assertEqual("You have selected Impressive", driver.find_element(by=By.XPATH,
                                                                                 value="//*[@id='app']/div/div/div[2]/div[2]/div[2]/p").text)
        except AssertionError as v:
            print(str(v))
            counter += 1
            driver.get_screenshot_as_png()
            driver.save_screenshot(f"RadioButton{counter}.png")
        logging.info("Rudio button checked")

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
        driver.get(
            test_link_web_table)
        driver.find_element(by=By.ID, value="addNewRecordButton").click()
        time.sleep(10)

        # Вносим данные в открывшемся окне

        driver.find_element(by=By.ID, value='firstName').send_keys('Test First Name')
        time.sleep(5)
        driver.find_element(by=By.ID, value='lastName').send_keys('Test Last Name')
        time.sleep(5)
        driver.find_element(by=By.ID, value='userEmail').send_keys('TestMail@test.com')
        time.sleep(5)
        driver.find_element(by=By.ID, value='age').send_keys('23')
        time.sleep(5)
        driver.find_element(by=By.ID, value='salary').send_keys('23')
        time.sleep(5)
        driver.find_element(by=By.ID, value='department').send_keys('Test department')
        driver.find_element(by=By.ID, value='submit').click()
        logging.info("Test form is filled")
        time.sleep(15)

        # Проверяем внесение данных в исходную табличку

        try:
            self.assertEqual('Test First Name', driver.find_element(by=By.XPATH,
                                                                    value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[1]').text)
        except AssertionError as v:
            print(str(v))
        try:
            self.assertEqual('Test Last Name', driver.find_element(by=By.XPATH,
                                                                   value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[2]').text)
        except AssertionError as v:
            print(str(v))
        try:
            self.assertEqual('23', driver.find_element(by=By.XPATH,
                                                       value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[3]').text)
        except AssertionError as v:
            print(str(v))
        try:
            self.assertEqual('TestMail@test.com', driver.find_element(by=By.XPATH,
                                                                      value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[4]').text)
        except AssertionError as v:
            print(str(v))
        try:
            self.assertEqual('23', driver.find_element(by=By.XPATH,
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
        logging.info('Test form is checked')

    def test_buttons(self):
        """
        Данная функция проводит проверку работы сайта https://demoqa.com/buttons.
        Вводит 3 переменные и далее с помощью ActionChains выполняет:
        double_click().perform() - двойной клик,
        context_click().perform() - клик правой кнопкой мыши,
        click().perform() - обычный клик левой кнопкой мыши.

        """
        driver = self.driver
        driver.get(test_link_buttons)

        # Создаем переменную для двойного клика

        double_click = driver.find_element(by=By.XPATH, value='//*[@id="doubleClickBtn"]')
        action = ActionChains(driver)
        action.double_click(double_click).perform()
        time.sleep(5)
        try:
            self.assertEqual("You have done a double click", driver.find_element(by=By.XPATH,
                                                                                 value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[1]").text)
        except AssertionError as v:
            print(str(v))

        # Создаем переменную для правого клика

        right_click = driver.find_element(by=By.XPATH, value='//*[@id="rightClickBtn"]')
        action.context_click(right_click).perform()
        time.sleep(5)
        try:
            self.assertEqual("You have done a right click", driver.find_element(by=By.XPATH,
                                                                                value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[2]").text)
        except AssertionError as v:
            print(str(v))

        # Создаем переменную для левого клика

        left_click = driver.find_element(by=By.XPATH,
                                         value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button')
        action.click(left_click).perform()
        time.sleep(5)
        try:
            self.assertEqual("You have done a dynamic click", driver.find_element(by=By.XPATH,
                                                                                  value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[3]").text)
        except AssertionError as v:
            print(str(v))
        logging.info("Buttons in checked")

    def test_links(self):
        """
        Данная функция работает с https://demoqa.com/links.
        Выполняет проверку ссылок в гиперссылках.
        """
        driver = self.driver
        driver.get(test_link_links)
        home_link = driver.find_element(by=By.ID, value="simpleLink").get_attribute("href")
        try:
            self.assertEqual('https://demoqa.com/', home_link)
            logging.info("Home link URL has checked successfully")
        except AssertionError as ae:
            print(str(ae))
            logging.error('Assertion error on home_link')
        # Homehl
        homehl_link = driver.find_element(by=By.ID, value="dynamicLink").get_attribute('href')
        try:
            self.assertEqual('https://demoqa.com/', homehl_link)
            logging.info("Homehl link URL has checked successfully")
        except AssertionError as ae:
            print(str(ae))
            logging.error('Assertion error on homehl_link')


    def test_broken_link(self):
        """
        Данная функция работает со страничкой https://demoqa.com/broken.
        Для начала, проверяет наличие картинок путем сверки href с заданной и затем делает скриншот.
        Далее нажимает на ссылки и проверяет правильность перехода по нужной ссылке.
        """
        driver = self.driver
        driver.get(test_link_broken)
        counter_broken_link = 0
        counter_broken_link += 1
        driver.get_screenshot_as_png()
        driver.save_screenshot(f"broken_link_{counter_broken_link}.png")
        try:
            self.assertEqual("https://demoqa.com/images/Toolsqa.jpg", driver.find_element(by=By.XPATH, value="//*[@id='app']/div/div/div[2]/div[2]/div[2]/img[1]").get_attribute("src"))
        except NoSuchElementException as nsex:
            print(str(nsex))
        try:
            self.assertEqual("https://demoqa.com/images/Toolsqa_1.jpg", driver.find_element(by=By.XPATH, value="//*[@id='app']/div/div/div[2]/div[2]/div[2]/img[2]").get_attribute("src"))
        except NoSuchElementException as nsex:
            print(str(nsex))
        driver.execute_script("window.scrollTo(0, 250);")
        driver.find_element(by=By.XPATH, value="//*[@id='app']/div/div/div[2]/div[2]/div[2]/a[1]").click()
        time.sleep(5)
        url_correct = driver.current_url
        driver.back()
        try:
            self.assertEqual("https://demoqa.com/", url_correct)
        except NoSuchElementException as nsex:
            print(str(nsex))
        driver.find_element(by=By.XPATH, value='//*[@id="app"]/div/div/div[2]/div[2]/div[2]/a[2]').click()
        time.sleep(5)
        url_uncorrect = driver.current_url
        try:
            self.assertEqual("http://the-internet.herokuapp.com/status_codes/500", url_uncorrect)
        except NoSuchElementException as nsex:
            print(str(nsex))
        driver.back()


    def test_upload_download_file(self):
        driver = self.driver
        driver.get(test_link_upload_download)
        upload = driver.find_element(by=By.XPATH, value="//*[@id='uploadFile']")
        time.sleep(5)
        upload.send_keys("C:/Users/User/Desktop/GIT/Autotests/img/sampleFile.jpeg")
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
    x = ToolsQA()
