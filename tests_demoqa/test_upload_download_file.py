from selenium.webdriver.common.by import By
from setting_chrome import SetUpUniChrome
import unittest
import time


class UploadDownload(SetUpUniChrome):
    def test_upload_download_file(self):
        driver = self.driver
        driver.get("https://demoqa.com/upload-download")
        upload = driver.find_element(by=By.XPATH, value="//*[@id='uploadFile']")
        time.sleep(5)
        upload.send_keys("C:/Users/User/Desktop/GIT/Autotests/img/sampleFile.jpeg")
        time.sleep(5)


if __name__ == "__main__":
    unittest.main()
