import unittest

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from setting_chrome import SetUpUniChrome
import time


class LocatorsBrokenLinks():
    ImageToolsQa = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/img[1]"
    BrokenImageToolsQA = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/img[2]"
    ValidLinks = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/a[1]"
    BrokenLinks = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/a[2]'


class BrokenLink(SetUpUniChrome):
    def test_broken_link(self):
        """
        Данная функция работает со страничкой https://demoqa.com/broken.
        Для начала, проверяет наличие картинок путем сверки href с заданной и затем делает скриншот.
        Далее нажимает на ссылки и проверяет правильность перехода по нужной ссылке.
        """
        driver = self.driver
        driver.get("https://demoqa.com/broken")
        # counter_broken_link = 0
        # counter_broken_link += 1
        # driver.get_screenshot_as_png()
        # driver.save_screenshot(f"broken_link_{counter_broken_link}.png")
        try:
            self.assertEqual("https://demoqa.com/images/Toolsqa.jpg", driver.find_element(by=By.XPATH,
                                                                                          value=LocatorsBrokenLinks.ImageToolsQa).get_attribute(
                "src"))
        except NoSuchElementException as nsex:
            print(str(nsex))
        try:
            self.assertEqual("https://demoqa.com/images/Toolsqa_1.jpg", driver.find_element(by=By.XPATH,
                                                                                            value=LocatorsBrokenLinks.BrokenImageToolsQA).get_attribute(
                "src"))
        except NoSuchElementException as nsex:
            print(str(nsex))
        driver.execute_script("window.scrollTo(0, 250);")
        driver.find_element(by=By.XPATH, value=LocatorsBrokenLinks.ValidLinks).click()
        time.sleep(5)
        url_correct = driver.current_url
        driver.back()
        try:
            self.assertEqual("https://demoqa.com/", url_correct)
        except NoSuchElementException as nsex:
            print(str(nsex))
        driver.find_element(by=By.XPATH, value=LocatorsBrokenLinks.BrokenLinks).click()
        time.sleep(5)
        url_uncorrect = driver.current_url
        try:
            self.assertEqual("http://the-internet.herokuapp.com/status_codes/500", url_uncorrect)
        except NoSuchElementException as nsex:
            print(str(nsex))
        driver.back()


if __name__ == "__main__":
    unittest.main()
