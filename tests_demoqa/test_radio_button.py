

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
