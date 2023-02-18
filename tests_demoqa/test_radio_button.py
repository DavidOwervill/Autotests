from selenium.webdriver.common.by import By
from setting_chrome import SetUpUniChrome
import unittest
import time


class LocatorsRadioButton:
    YouHaveSelected = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/p"
    YesButton = "custom-control-label"
    ImpressiveButton = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/label"


class RadioButton(SetUpUniChrome):
    def test_radio_button(self):
        """
        Данная функция работает с сайтом https://demoqa.com/radio-button.
        Проверяет нажатие на кнопку Yes, Impressive.
        Кнопка No не действительна.

        """
        driver = self.driver
        driver.get("https://demoqa.com/radio-button")

        driver.find_element(by=By.CLASS_NAME, value=LocatorsRadioButton.YesButton).click()
        time.sleep(15)
        try:
            self.assertEqual("You have selected Yes", driver.find_element(by=By.XPATH,
                                                                          value=LocatorsRadioButton.YouHaveSelected).text)
        except AssertionError as v:
            print(str(v))

        driver.find_element(by=By.XPATH, value=LocatorsRadioButton.ImpressiveButton).click()
        time.sleep(15)
        try:
            self.assertEqual("You have selected Impressive", driver.find_element(by=By.XPATH,
                                                                                 value=LocatorsRadioButton.YouHaveSelected).text)
        except AssertionError as v:
            print(str(v))


if __name__ == "__main__":
    unittest.main()
