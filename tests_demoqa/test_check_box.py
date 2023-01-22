

def test_check_box(self):
    """
    Данная функция работает с https://demoqa.com/checkbox.
    В данной функции последовательно проверяется нажатие на галочку возле соответствующей директории и
    возможность попасть внутрь.
    Порядок проверки следующий - Home -> Desktop -> Documents -> Downloads -> Notes ->Commands->
    WorkSpace -> Office -> React -> Angular -> Vue -> Public -> Private -> Classified -> General ->
    Word file.doc -> Excel File.doc
    """
    driver = self.driver
    driver.get(
        test_link_check_box)
    driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/span/label/span[1]").click()
    try:
        self.assertEqual("home", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except NoSuchElementException as e:
        print(str(e))
    time.sleep(5)

    # Опускаемся на 1 слой глубже

    driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/span/label/span[1]").click()
    driver.find_element(by=By.CSS_SELECTOR, value='.rct-collapse.rct-collapse-btn').click()
    driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[1]/span/label/span[1]").click()
    try:
        self.assertEqual("desktop", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except NoSuchElementException as e:
        print(str(e))
    logging.info('Desktop checked')
    time.sleep(5)
    driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[1]/span/label/span[1]").click()
    driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[2]/span/label/span[1]").click()
    try:
        self.assertEqual("documents", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except NoSuchElementException as e:
        print(str(e))
    logging.info('Documents checked')
    time.sleep(5)
    driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[2]/span/label/span[1]").click()
    driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[3]/span/label/span[1]").click()
    try:
        self.assertEqual("downloads", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except AssertionError as e:
        print(str(e))
    logging.info('Downloads checked')
    time.sleep(5)

    # Опускаемся на 1 слой глубже в разделе Desktop

    driver.find_element(by=By.XPATH, value="//*[@id='tree-node']/ol/li/ol/li[3]/span/label/span[1]").click()
    driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[1]/span/button').click()

    # Опустились

    logging.info('Down to the Desktop level')
    driver.find_element(by=By.XPATH,
                        value="//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]").click()
    try:
        self.assertEqual("notes", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except AssertionError as e:
        print(str(e))
    logging.info('Notes checked')
    time.sleep(5)
    driver.find_element(by=By.XPATH,
                        value="//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]").click()
    driver.find_element(by=By.XPATH,
                        value="//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[2]/span/label/span[1]").click()
    try:
        self.assertEqual("commands", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except AssertionError as e:
        print(str(e))
    logging.info('Commands checked')
    time.sleep(5)

    # Следующим действием выходим из desktop

    driver.find_element(by=By.XPATH,
                        value="//*[@id='tree-node']/ol/li/ol/li[1]/ol/li[2]/span/label/span[1]").click()
    driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[1]/span/button').click()
    logging.info('Down to the Documents level')
    driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/span/button').click()

    # Опустились на уровень Documents

    driver.find_element(by=By.XPATH,
                        value="//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/span/label/span[1]").click()
    try:
        self.assertEqual("workspace", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except AssertionError as e:
        print(str(e))
    logging.info("WorkSpace checked")
    time.sleep(5)
    driver.find_element(by=By.XPATH,
                        value="//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/span/label/span[1]").click()
    driver.find_element(by=By.XPATH,
                        value="//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/span/label/span[1]").click()
    try:
        self.assertEqual("office", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except AssertionError as e:
        print(str(e))
    logging.info("Office checked")

    # Проваливаемся на 1 уровень ниже в рамках Documents

    driver.find_element(by=By.XPATH,
                        value="//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/span/label/span[1]").click()
    driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/button').click()

    # Работаем со вложением WorkSpace

    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[1]/span/label/span[1]').click()
    try:
        self.assertEqual("react", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except AssertionError as e:
        print(str(e))
    logging.info('React checked')
    time.sleep(5)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[1]/span/label/span[1]').click()
    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[2]/span/label/span[1]').click()
    try:
        self.assertEqual("angular", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except AssertionError as e:
        print(str(e))
    logging.info('Angular checked')
    time.sleep(5)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[2]/span/label/span[1]').click()
    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[3]/span/label/span[1]').click()
    try:
        self.assertEqual("veu", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except AssertionError as e:
        print(str(e))
    logging.info('Veu Checked')
    time.sleep(5)

    # Выходим из уровня workspace

    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[3]/span/label/span[1]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/button').click()
    driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/span/button').click()

    # Работаем с уровнем Office

    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[1]/span/label/span[1]').click()
    try:
        self.assertEqual("public", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except AssertionError as e:
        print(str(e))
    logging.info('public checked')
    time.sleep(5)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[1]/span/label/span[1]').click()
    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[2]/span/label/span[1]').click()
    try:
        self.assertEqual("private", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except AssertionError as e:
        print(str(e))
    logging.info('Private was checked')
    time.sleep(5)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[2]/span/label/span[1]').click()
    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[3]/span/label/span[1]').click()
    try:
        self.assertEqual("classified", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except AssertionError as e:
        print(str(e))
    logging.info('Classified was checked')
    time.sleep(5)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[3]/span/label/span[1]').click()
    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[4]/span/label/span[1]').click()
    driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)
    try:
        self.assertEqual("general", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except AssertionError as e:
        print(str(e))
    logging.info('General was checked')
    time.sleep(5)

    # Выходим из уровня Office

    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[4]/span/label/span[1]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/span/button').click()
    driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/span/button').click()

    # Падаем в уровень Downloads

    driver.find_element(by=By.XPATH, value='//*[@id="tree-node"]/ol/li/ol/li[3]/span/button').click()
    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]').click()
    try:
        self.assertEqual("wordFile", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except AssertionError as e:
        print(str(e))
    logging.info('Word File checked')
    time.sleep(5)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]').click()
    driver.find_element(by=By.XPATH,
                        value='//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[2]/span/label/span[1]').click()
    try:
        self.assertEqual("excelFile", driver.find_element(by=By.XPATH, value="//*[@id='result']/span[2]").text)
    except AssertionError as e:
        print(str(e))
    logging.info('Excel File checked')
    time.sleep(5)