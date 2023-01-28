def test_buttons(self):
    """
    Данная функция проводит проверку работы сайта https://demoqa.com/buttons.
    Вводит 3 переменные и далее с помощью ActionChains выполняет:
    double_click().perform() - двойной клик,
    context_click().perform() - клик правой кнопкой мыши,
    click().perform() - обычный клик левой кнопкой мыши.

    """
    driver = self.driver
    driver.get(test_link_buttons)

    # Создаем переменную для двойного клика

    double_click = driver.find_element(by=By.XPATH, value='//*[@id="doubleClickBtn"]')
    action = ActionChains(driver)
    action.double_click(double_click).perform()
    time.sleep(5)
    try:
        self.assertEqual("You have done a double click", driver.find_element(by=By.XPATH,
                                                                             value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[1]").text)
    except AssertionError as v:
        print(str(v))

    # Создаем переменную для правого клика

    right_click = driver.find_element(by=By.XPATH, value='//*[@id="rightClickBtn"]')
    action.context_click(right_click).perform()
    time.sleep(5)
    try:
        self.assertEqual("You have done a right click", driver.find_element(by=By.XPATH,
                                                                            value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[2]").text)
    except AssertionError as v:
        print(str(v))

    # Создаем переменную для левого клика

    left_click = driver.find_element(by=By.XPATH,
                                     value='/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button')
    action.click(left_click).perform()
    time.sleep(5)
    try:
        self.assertEqual("You have done a dynamic click", driver.find_element(by=By.XPATH,
                                                                              value="/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[3]").text)
    except AssertionError as v:
        print(str(v))
    logging.info("Buttons in checked")