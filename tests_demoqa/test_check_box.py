from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time, logging


class LocatorsCheckBox():
    # XPATH
    home_check_box = "//*[@id='tree-node']/ol/li/span/label/span[1]"
    home_title = "//*[@id='result']/span[2]"
    desktop_check_box = "//*[@id='tree-node']/ol/li/ol/li[1]/span/label/span[1]"
    desktop_title = "//*[@id='result']/span[2]"
    documents_check_box = "//*[@id='tree-node']/ol/li/ol/li[2]/span/label/span[1]"
    documents_title = "//*[@id='result']/span[2]"
    documents_level_aria_button = "//*[@id='tree-node']/ol/li/ol/li[2]/span/button"
    downloads_check_box = "//*[@id='tree-node']/ol/li/ol/li[3]/span/label/span[1]"
    downloads_title = "//*[@id='result']/span[2]"
    downloads_level_aria_button = '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button'
    desktop_level_aria_button =  "//*[@id='tree-node']/ol/li/ol/li[1]/span/button"
    notes_check_box = "//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]"
    notes_title = "//*[@id='result']/span[2]"
    commands_check_box = "//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[2]/span/label/span[1]"
    commands_title = "//*[@id='result']/span[2]"
    workspace_check_box = "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/span/label/span[1]"
    workspace_title = "//*[@id='result']/span[2]"
    workspace_level_aria_button = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/button'
    office_check_box = "//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/span/label/span[1]"
    office_title = "//*[@id='result']/span[2]"
    office_level_aria_button = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/span/button'
    react_check_box = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[1]/span/label/span[1]'
    react_title = "//*[@id='result']/span[2]"
    angular_check_box = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[2]/span/label/span[1]'
    title_check = "//*[@id='result']/span[2]"
    veu_check_box = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[3]/span/label/span[1]'
    public_check_box = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[1]/span/label/span[1]'
    private_check_box = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[2]/span/label/span[1]'
    classified_check_box = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[3]/span/label/span[1]'
    general_check_box = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[4]/span/label/span[1]'
    wordfile_check_box = '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]'
    excelfile_check_box = '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[2]/span/label/span[1]'
    # CSS
    first_level_aria_button = ".rct-collapse.rct-collapse-btn"




class CheckBox(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

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
            "https://demoqa.com/checkbox")
        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.home_check_box).click()
        try:
            self.assertEqual("home", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.home_title).text)
        except NoSuchElementException as e:
            print(str(e))
        time.sleep(5)

        # Опускаемся на 1 слой глубже

        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.home_check_box).click()
        driver.find_element(by=By.CSS_SELECTOR, value=LocatorsCheckBox.first_level_aria_button).click()
        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.desktop_check_box).click()
        try:
            self.assertEqual("desktop", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.desktop_title).text)
        except NoSuchElementException as e:
            print(str(e))
        logging.info('Desktop checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.desktop_check_box).click()
        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.documents_check_box).click()
        try:
            self.assertEqual("documents", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.documents_title).text)
        except NoSuchElementException as e:
            print(str(e))
        logging.info('Documents checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.documents_check_box).click()
        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.downloads_check_box).click()
        try:
            self.assertEqual("downloads", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.downloads_title).text)
        except AssertionError as e:
            print(str(e))
        logging.info('Downloads checked')
        time.sleep(5)

        # Опускаемся на 1 слой глубже в разделе Desktop

        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.downloads_check_box).click()
        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.desktop_level_aria_button).click()

        # Опустились

        logging.info('Down to the Desktop level')
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.notes_check_box).click()
        try:
            self.assertEqual("notes", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.notes_title).text)
        except AssertionError as e:
            print(str(e))
        logging.info('Notes checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.notes_check_box).click()
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.commands_check_box).click()
        try:
            self.assertEqual("commands", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.commands_title).text)
        except AssertionError as e:
            print(str(e))
        logging.info('Commands checked')
        time.sleep(5)

        # Следующим действием выходим из desktop

        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.commands_check_box).click()
        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.desktop_level_aria_button).click()
        logging.info('Down to the Documents level')
        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.documents_level_aria_button).click()

        # Опустились на уровень Documents

        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.workspace_check_box).click()
        try:
            self.assertEqual("workspace", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.workspace_title).text)
        except AssertionError as e:
            print(str(e))
        logging.info("WorkSpace checked")
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.workspace_check_box).click()
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.office_check_box).click()
        try:
            self.assertEqual("office", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.office_title).text)
        except AssertionError as e:
            print(str(e))
        logging.info("Office checked")

        # Проваливаемся на 1 уровень ниже в рамках Documents

        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.office_check_box).click()
        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.workspace_level_aria_button).click()

        # Работаем со вложением WorkSpace

        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.react_check_box).click()
        try:
            self.assertEqual("react", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.react_title).text)
        except AssertionError as e:
            print(str(e))
        logging.info('React checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.react_check_box).click()
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.angular_check_box).click()
        try:
            self.assertEqual("angular", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text)
        except AssertionError as e:
            print(str(e))
        logging.info('Angular checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.angular_check_box).click()
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.veu_check_box).click()
        try:
            self.assertEqual("veu", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text)
        except AssertionError as e:
            print(str(e))
        logging.info('Veu Checked')
        time.sleep(5)

        # Выходим из уровня workspace

        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.veu_check_box).click()
        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.workspace_level_aria_button).click()
        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.office_level_aria_button).click()

        # Работаем с уровнем Office

        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.public_check_box).click()
        try:
            self.assertEqual("public", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text)
        except AssertionError as e:
            print(str(e))
        logging.info('public checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.public_check_box).click()
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.private_check_box).click()
        try:
            self.assertEqual("private", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text)
        except AssertionError as e:
            print(str(e))
        logging.info('Private was checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.private_check_box).click()
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.classified_check_box).click()
        try:
            self.assertEqual("classified", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text)
        except AssertionError as e:
            print(str(e))
        logging.info('Classified was checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.classified_check_box).click()
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.general_check_box).click()
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        try:
            self.assertEqual("general", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text)
        except AssertionError as e:
            print(str(e))
        logging.info('General was checked')
        time.sleep(5)

        # Выходим из уровня Office

        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.general_check_box).click()
        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.office_level_aria_button).click()
        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.workspace_level_aria_button).click()

        # Падаем в уровень Downloads

        driver.find_element(by=By.XPATH, value=LocatorsCheckBox.downloads_level_aria_button).click()
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.wordfile_check_box).click()
        try:
            self.assertEqual("wordFile", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text)
        except AssertionError as e:
            print(str(e))
        logging.info('Word File checked')
        time.sleep(5)
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.wordfile_check_box).click()
        driver.find_element(by=By.XPATH,
                            value=LocatorsCheckBox.excelfile_check_box).click()
        try:
            self.assertEqual("excelFile", driver.find_element(by=By.XPATH, value=LocatorsCheckBox.title_check).text)
        except AssertionError as e:
            print(str(e))
        logging.info('Excel File checked')
        time.sleep(5)