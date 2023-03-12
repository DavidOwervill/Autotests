import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("set_up_chrome")
class TestLinks:
    def test_links(self):
        """
        Данная функция работает с https://demoqa.com/links.
        Выполняет проверку ссылок в гиперссылках.
        """
        driver = self.driver
        driver.get("https://demoqa.com/links")
        home_link = driver.find_element(by=By.ID, value="simpleLink").get_attribute("href")
        assert 'https://demoqa.com/' == home_link
        homehl_link = driver.find_element(by=By.ID, value="dynamicLink").get_attribute('href')
        assert 'https://demoqa.com/' == homehl_link

