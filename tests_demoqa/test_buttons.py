import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from setting_chrome import SetUpUniChrome
import time


class LocatorsButtons:
    FindDoubleClick = '//*[@id="doubleClickBtn"]'
    DoubleClick = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[1]"
    FindRightClick = '//*[@id="rightClickBtn"]'
    RightClick = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[2]"
    FindDynamicClick = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button'
    DynamicClick = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[3]"


class Buttons(SetUpUniChrome):
    def test_buttons(self):
        """
        Данная функция проводит проверку работы сайта https://demoqa.com/buttons.
        Вводит 3 переменные и далее с помощью ActionChains выполняет:
        double_click().perform() - двойной клик,
        context_click().perform() - клик правой кнопкой мыши,
        click().perform() - обычный клик левой кнопкой мыши.

        """
        driver = self.driver
        driver.get('https://demoqa.com/buttons')

        # Создаем переменную для двойного клика

        double_click = driver.find_element(by=By.XPATH, value=LocatorsButtons.FindDoubleClick)
        action = ActionChains(driver)
        action.double_click(double_click).perform()
        time.sleep(5)
        try:
            self.assertEqual("You have done a double click", driver.find_element(by=By.XPATH,
                                                                                 value=LocatorsButtons.DoubleClick).text)
        except AssertionError as v:
            print(str(v))

        # Создаем переменную для правого клика

        right_click = driver.find_element(by=By.XPATH, value=LocatorsButtons.FindRightClick)
        action.context_click(right_click).perform()
        time.sleep(5)
        try:
            self.assertEqual("You have done a right click", driver.find_element(by=By.XPATH,
                                                                                value=LocatorsButtons.RightClick).text)
        except AssertionError as v:
            print(str(v))

        # Создаем переменную для левого клика

        left_click = driver.find_element(by=By.XPATH,
                                         value=LocatorsButtons.FindDynamicClick)
        action.click(left_click).perform()
        time.sleep(5)
        try:
            self.assertEqual("You have done a dynamic click", driver.find_element(by=By.XPATH,
                                                                                  value=LocatorsButtons.DynamicClick).text)
        except AssertionError as v:
            print(str(v))


if __name__ == "__main__":
    unittest.main()