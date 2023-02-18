from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from setting_chrome import SetUpUniChrome
import unittest
import time


class LocatorsTextBox:
    UserName = "userName"
    UserNameCheck = "//*[@id='name']"
    UserEmail = "userEmail"
    UserEmailCheck = "//*[@id='email']"
    CurrentAddress = "currentAddress"
    CACheck = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[3]"
    PermanentAddress = "permanentAddress"
    PACheck = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[4]"
    TestUserName = "Full Name Test Write"
    TestUserEmail = "testmail@gmail.com"
    TestCurrentAddress = "Test Current Address"
    TestPermanentAddress = 'Test Permanent Address'


class TestBox(SetUpUniChrome):
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
        driver.get("https://demoqa.com/text-box")
        driver.find_element(by=By.ID, value=LocatorsTextBox.UserName).send_keys(LocatorsTextBox.TestUserName)
        time.sleep(3)
        driver.find_element(by=By.ID, value=LocatorsTextBox.UserEmail).send_keys(LocatorsTextBox.TestUserEmail)
        time.sleep(3)
        driver.find_element(by=By.ID, value=LocatorsTextBox.CurrentAddress).send_keys(
            LocatorsTextBox.TestCurrentAddress)
        time.sleep(3)
        driver.find_element(by=By.ID, value=LocatorsTextBox.PermanentAddress).send_keys(
            LocatorsTextBox.TestPermanentAddress)
        time.sleep(3)
        driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
        driver.find_element(by=By.ID, value="submit").click()
        time.sleep(10)
        try:
            self.assertEqual(f"Name:{LocatorsTextBox.TestUserName}",
                             driver.find_element(by=By.XPATH, value=LocatorsTextBox.UserNameCheck).text)
        except ValueError as e:
            print(str(e))
        # logging.info("Check User Name")
        try:
            self.assertEqual(f"Email:{LocatorsTextBox.TestUserEmail}",
                             driver.find_element(by=By.XPATH, value=LocatorsTextBox.UserEmailCheck).text)
        except ValueError as e:
            print(str(e))
        # logging.info("Check Email")
        try:
            self.assertEqual(f"Current Address :{LocatorsTextBox.TestCurrentAddress}",
                             driver.find_element(by=By.XPATH,
                                                 value=LocatorsTextBox.CACheck).text)
        except ValueError as e:
            print(str(e))
        # logging.info("Check Current Address")
        try:
            self.assertEqual(f"Permananet Address :{LocatorsTextBox.TestPermanentAddress}",
                             driver.find_element(by=By.XPATH,
                                                 value=LocatorsTextBox.PACheck).text)
        except ValueError as e:
            print(str(e))
        # logging.info("Check permanent address")


if __name__ == "__main__":
    unittest.main()
