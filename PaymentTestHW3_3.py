from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

service = Service(executable_path="Users/User/Desktop/GIT/Autotests/drivers")
driver = webdriver.Chrome(service=service)


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    # Тестирование не введенного значения CCV2

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get(
            "https://sandbox.cardpay.com/MI/cardpayment2.html?orderXml=PE9SREVSIFdBTExFVF9JRD0nODI5OScgT1JERVJfTlVNQkVSPSc0NTgyMTEnIEFNT1VOVD0nMjkxLjg2JyBDVVJSRU5DWT0nRVVSJyAgRU1BSUw9J2N1c3RvbWVyQGV4YW1wbGUuY29tJz4KPEFERFJFU1MgQ09VTlRSWT0nVVNBJyBTVEFURT0nTlknIFpJUD0nMTAwMDEnIENJVFk9J05ZJyBTVFJFRVQ9JzY3NyBTVFJFRVQnIFBIT05FPSc4NzY5OTA5MCcgVFlQRT0nQklMTElORycvPgo8L09SREVSPg==&sha512=998150a2b27484b776a1628bfe7505a9cb430f276dfa35b14315c1c8f03381a90490f6608f0dcff789273e05926cd782e1bb941418a9673f43c47595aa7b8b0d")
        driver.find_element(by=By.ID, value="input-card-number").click()
        driver.find_element(by=By.ID, value="input-card-number").clear()
        driver.find_element(by=By.ID, value="input-card-number").send_keys("4000 0000 0000 0051")
        driver.find_element(by=By.ID, value="input-card-number").click()
        driver.find_element(by=By.ID, value="input-card-holder").send_keys("QWERTY QWERTY")
        driver.find_element(by=By.ID, value="card-expires-month").click()
        Select(driver.find_element(by=By.ID, value="card-expires-month")).select_by_visible_text("05")
        driver.find_element(by=By.ID, value="card-expires-month").click()
        Select(driver.find_element(by=By.ID, value="card-expires-year")).select_by_visible_text("2024")
#        driver.find_element(by=By.ID, value="input-card-cvc").click()
#        driver.find_element(by=By.ID, value="input-card-cvc").send_keys("123")
        driver.find_element(by=By.ID, value="action-submit").click()
        try:
            self.assertEqual("CVV2/CVC2/CAV2 is required",
                             driver.find_element(by=By.XPATH, value="/html/body/div[1]/form/section[2]/section/div[1]/div/div[4]/div/label").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    # Тестирование не введенного значения Expires

    def test_app_dynamics_job_2(self):
        driver = self.driver
        driver.get(
            "https://sandbox.cardpay.com/MI/cardpayment2.html?orderXml=PE9SREVSIFdBTExFVF9JRD0nODI5OScgT1JERVJfTlVNQkVSPSc0NTgyMTEnIEFNT1VOVD0nMjkxLjg2JyBDVVJSRU5DWT0nRVVSJyAgRU1BSUw9J2N1c3RvbWVyQGV4YW1wbGUuY29tJz4KPEFERFJFU1MgQ09VTlRSWT0nVVNBJyBTVEFURT0nTlknIFpJUD0nMTAwMDEnIENJVFk9J05ZJyBTVFJFRVQ9JzY3NyBTVFJFRVQnIFBIT05FPSc4NzY5OTA5MCcgVFlQRT0nQklMTElORycvPgo8L09SREVSPg==&sha512=998150a2b27484b776a1628bfe7505a9cb430f276dfa35b14315c1c8f03381a90490f6608f0dcff789273e05926cd782e1bb941418a9673f43c47595aa7b8b0d")
        driver.find_element(by=By.ID, value="input-card-number").click()
        driver.find_element(by=By.ID, value="input-card-number").clear()
        driver.find_element(by=By.ID, value="input-card-number").send_keys("4000 0000 0000 0051")
        driver.find_element(by=By.ID, value="input-card-number").click()
        driver.find_element(by=By.ID, value="input-card-holder").send_keys("QWERTY QWERTY")
#        driver.find_element(by=By.ID, value="card-expires-month").click()
#        Select(driver.find_element(by=By.ID, value="card-expires-month")).select_by_visible_text("05")
#         driver.find_element(by=By.ID, value="card-expires-month").click()
#         Select(driver.find_element(by=By.ID, value="card-expires-year")).select_by_visible_text("2024")
        driver.find_element(by=By.ID, value="input-card-cvc").click()
        driver.find_element(by=By.ID, value="input-card-cvc").send_keys("123")
        driver.find_element(by=By.ID, value="action-submit").click()
        try:
            self.assertEqual("Expiration Date is required", driver.find_element(by=By.XPATH,
                                                                             value="/html/body/div[1]/form/section[2]/section/div[1]/div/div[3]/div/label").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    # Тестирование неверно введенного имени держателя карты

    def test_app_dynamics_job_3(self):
        driver = self.driver
        driver.get(
            "https://sandbox.cardpay.com/MI/cardpayment2.html?orderXml=PE9SREVSIFdBTExFVF9JRD0nODI5OScgT1JERVJfTlVNQkVSPSc0NTgyMTEnIEFNT1VOVD0nMjkxLjg2JyBDVVJSRU5DWT0nRVVSJyAgRU1BSUw9J2N1c3RvbWVyQGV4YW1wbGUuY29tJz4KPEFERFJFU1MgQ09VTlRSWT0nVVNBJyBTVEFURT0nTlknIFpJUD0nMTAwMDEnIENJVFk9J05ZJyBTVFJFRVQ9JzY3NyBTVFJFRVQnIFBIT05FPSc4NzY5OTA5MCcgVFlQRT0nQklMTElORycvPgo8L09SREVSPg==&sha512=998150a2b27484b776a1628bfe7505a9cb430f276dfa35b14315c1c8f03381a90490f6608f0dcff789273e05926cd782e1bb941418a9673f43c47595aa7b8b0d")
        driver.find_element(by=By.ID, value="input-card-number").click()
        driver.find_element(by=By.ID, value="input-card-number").clear()
        driver.find_element(by=By.ID, value="input-card-number").send_keys("4000 0000 0000 0051")
        driver.find_element(by=By.ID, value="input-card-number").click()
        driver.find_element(by=By.ID, value="input-card-holder").send_keys("5759769808")
        driver.find_element(by=By.ID, value="card-expires-month").click()
        Select(driver.find_element(by=By.ID, value="card-expires-month")).select_by_visible_text("05")
        driver.find_element(by=By.ID, value="card-expires-month").click()
        Select(driver.find_element(by=By.ID, value="card-expires-year")).select_by_visible_text("2024")
        driver.find_element(by=By.ID, value="input-card-cvc").click()
        driver.find_element(by=By.ID, value="input-card-cvc").send_keys("123")
        driver.find_element(by=By.ID, value="action-submit").click()
        try:
            self.assertEqual("Cardholder name is not valid", driver.find_element(by=By.XPATH,
                                                                                 value="/html/body/div[1]/form/section[2]/section/div[1]/div/div[2]/div/label").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    # Тестирование неверно введенного номера карты

    def test_app_dynamics_job_4(self):
            driver = self.driver
            driver.get(
                "https://sandbox.cardpay.com/MI/cardpayment2.html?orderXml=PE9SREVSIFdBTExFVF9JRD0nODI5OScgT1JERVJfTlVNQkVSPSc0NTgyMTEnIEFNT1VOVD0nMjkxLjg2JyBDVVJSRU5DWT0nRVVSJyAgRU1BSUw9J2N1c3RvbWVyQGV4YW1wbGUuY29tJz4KPEFERFJFU1MgQ09VTlRSWT0nVVNBJyBTVEFURT0nTlknIFpJUD0nMTAwMDEnIENJVFk9J05ZJyBTVFJFRVQ9JzY3NyBTVFJFRVQnIFBIT05FPSc4NzY5OTA5MCcgVFlQRT0nQklMTElORycvPgo8L09SREVSPg==&sha512=998150a2b27484b776a1628bfe7505a9cb430f276dfa35b14315c1c8f03381a90490f6608f0dcff789273e05926cd782e1bb941418a9673f43c47595aa7b8b0d")
            driver.find_element(by=By.ID, value="input-card-number").click()
            driver.find_element(by=By.ID, value="input-card-number").clear()
            driver.find_element(by=By.ID, value="input-card-number").send_keys("1231 2312 3123 1212 321")
            driver.find_element(by=By.ID, value="input-card-number").click()
            driver.find_element(by=By.ID, value="input-card-holder").send_keys("QWERTY QWERTY")
            driver.find_element(by=By.ID, value="card-expires-month").click()
            Select(driver.find_element(by=By.ID, value="card-expires-month")).select_by_visible_text("05")
            driver.find_element(by=By.ID, value="card-expires-month").click()
            Select(driver.find_element(by=By.ID, value="card-expires-year")).select_by_visible_text("2024")
            driver.find_element(by=By.ID, value="input-card-cvc").click()
            driver.find_element(by=By.ID, value="input-card-cvc").send_keys("123")
            driver.find_element(by=By.ID, value="action-submit").click()
            try:
                self.assertEqual("Card number is not valid", driver.find_element(by=By.XPATH,
                                                                                 value="/html/body/div[1]/form/section[2]/section/div[1]/div/div[1]/div/label").text)
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    # Тестирование не введенного номера карты

    def test_app_dynamics_job_5(self):
            driver = self.driver
            driver.get(
                "https://sandbox.cardpay.com/MI/cardpayment2.html?orderXml=PE9SREVSIFdBTExFVF9JRD0nODI5OScgT1JERVJfTlVNQkVSPSc0NTgyMTEnIEFNT1VOVD0nMjkxLjg2JyBDVVJSRU5DWT0nRVVSJyAgRU1BSUw9J2N1c3RvbWVyQGV4YW1wbGUuY29tJz4KPEFERFJFU1MgQ09VTlRSWT0nVVNBJyBTVEFURT0nTlknIFpJUD0nMTAwMDEnIENJVFk9J05ZJyBTVFJFRVQ9JzY3NyBTVFJFRVQnIFBIT05FPSc4NzY5OTA5MCcgVFlQRT0nQklMTElORycvPgo8L09SREVSPg==&sha512=998150a2b27484b776a1628bfe7505a9cb430f276dfa35b14315c1c8f03381a90490f6608f0dcff789273e05926cd782e1bb941418a9673f43c47595aa7b8b0d")
            driver.find_element(by=By.ID, value="input-card-number").click()
            driver.find_element(by=By.ID, value="input-card-number").clear()
#            driver.find_element(by=By.ID, value="input-card-number").send_keys("4000 0000 0000 0051")
#            driver.find_element(by=By.ID, value="input-card-number").click()
            driver.find_element(by=By.ID, value="input-card-holder").send_keys("QWERTY QWERTY")
            driver.find_element(by=By.ID, value="card-expires-month").click()
            Select(driver.find_element(by=By.ID, value="card-expires-month")).select_by_visible_text("05")
            driver.find_element(by=By.ID, value="card-expires-month").click()
            Select(driver.find_element(by=By.ID, value="card-expires-year")).select_by_visible_text("2024")
            driver.find_element(by=By.ID, value="input-card-cvc").click()
            driver.find_element(by=By.ID, value="input-card-cvc").send_keys("123")
            driver.find_element(by=By.ID, value="action-submit").click()
            try:
                self.assertEqual("Card number is required", driver.find_element(by=By.XPATH,
                                                                                     value="/html/body/div[1]/form/section[2]/section/div[1]/div/div[1]/div/label").text)
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    # Тестирование не введенного держателя карты

    def test_app_dynamics_job_6(self):
            driver = self.driver
            driver.get(
                "https://sandbox.cardpay.com/MI/cardpayment2.html?orderXml=PE9SREVSIFdBTExFVF9JRD0nODI5OScgT1JERVJfTlVNQkVSPSc0NTgyMTEnIEFNT1VOVD0nMjkxLjg2JyBDVVJSRU5DWT0nRVVSJyAgRU1BSUw9J2N1c3RvbWVyQGV4YW1wbGUuY29tJz4KPEFERFJFU1MgQ09VTlRSWT0nVVNBJyBTVEFURT0nTlknIFpJUD0nMTAwMDEnIENJVFk9J05ZJyBTVFJFRVQ9JzY3NyBTVFJFRVQnIFBIT05FPSc4NzY5OTA5MCcgVFlQRT0nQklMTElORycvPgo8L09SREVSPg==&sha512=998150a2b27484b776a1628bfe7505a9cb430f276dfa35b14315c1c8f03381a90490f6608f0dcff789273e05926cd782e1bb941418a9673f43c47595aa7b8b0d")
            driver.find_element(by=By.ID, value="input-card-number").click()
            driver.find_element(by=By.ID, value="input-card-number").clear()
            driver.find_element(by=By.ID, value="input-card-number").send_keys("4000 0000 0000 0051")
            driver.find_element(by=By.ID, value="input-card-number").click()
            # driver.find_element(by=By.ID, value="input-card-holder").send_keys("QWERTY QWERTY")
            # driver.find_element(by=By.ID, value="card-expires-month").click()
            Select(driver.find_element(by=By.ID, value="card-expires-month")).select_by_visible_text("05")
            driver.find_element(by=By.ID, value="card-expires-month").click()
            Select(driver.find_element(by=By.ID, value="card-expires-year")).select_by_visible_text("2024")
            driver.find_element(by=By.ID, value="input-card-cvc").click()
            driver.find_element(by=By.ID, value="input-card-cvc").send_keys("123")
            driver.find_element(by=By.ID, value="action-submit").click()
            try:
                self.assertEqual("Cardholder name is required", driver.find_element(by=By.XPATH,
                                                                                 value="/html/body/div[1]/form/section[2]/section/div[1]/div/div[2]/div/label").text)
            except AssertionError as e:
                self.verificationErrors.append(str(e))

    # def is_element_present(self, how, what):
    #
    #     try:
    #         self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e:
    #         return False
    #     return True

    # def is_alert_present(self):
    #     try:
    #         self.driver.switch_to_alert()
    #     except NoAlertPresentException as e:
    #         return False
    #     return True

    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally:
    #         self.accept_next_alert = True

    # def tearDown(self):
    #     # To know more about the difference between verify and assert,
    #     # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
    #     self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    x = AppDynamicsJob()
    x.test_app_dynamics_job()
    x.test_app_dynamics_job2()
    x.test_app_dynamics_job3()
    x.test_app_dynamics_job_4()
    x.test_app_dynamics_job_5()
    x.test_app_dynamics_job_6()

