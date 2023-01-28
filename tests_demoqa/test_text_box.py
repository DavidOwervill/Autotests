





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
