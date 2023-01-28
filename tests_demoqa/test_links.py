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

