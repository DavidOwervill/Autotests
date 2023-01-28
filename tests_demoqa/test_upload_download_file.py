def test_upload_download_file(self):
    driver = self.driver
    driver.get(test_link_upload_download)
    upload = driver.find_element(by=By.XPATH, value="//*[@id='uploadFile']")
    time.sleep(5)
    upload.send_keys("C:/Users/User/Desktop/GIT/Autotests/img/sampleFile.jpeg")
    time.sleep(5)