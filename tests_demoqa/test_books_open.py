


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