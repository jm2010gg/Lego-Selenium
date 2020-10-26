import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

class Lego_Registration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.lego.com/pl-pl')



    def testWrongEmail(self):
        driver = self.driver
        # 1. Kliknij dalej.
        dalej_btn = WebDriverWait(driver, 40)\
        .until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="age-gate-grown-up-cta"]')))
        dalej_btn.click()

        # 2. Akceptuj pliki cookie.
        cookie_btn = WebDriverWait(driver, 40)\
        .until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="cookie-banner-normal-button"]')))
        cookie_btn.click()

        # 3. Kliknij 'Konto'.
        konto_btn = WebDriverWait(driver, 40)\
        .until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="util-bar-account-dropdown"]')))
        konto_btn.click()

        # 4. Kliknij 'Zarejestruj sie'.
        zarejestruj_sie_btn = WebDriverWait(driver, 40)\
        .until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="legoid-register-link"]')))
        zarejestruj_sie_btn.click()

        # 5. Wprowadz adres bledny email(brak .).
        adres_email = WebDriverWait(driver, 40)\
        .until(EC.presence_of_element_located((By.NAME, 'email')))
        adres_email.send_keys("lawendaaaaa@wppl")

        # 6. Wpisz haslo.
        password = driver.find_element_by_name('password')
        password.send_keys('Kwiatkowo8!')

        # 7. Wpisz date urodzenia.
        day = driver.find_element_by_id('day')
        day.send_keys('12')

        month = driver.find_element_by_id('month')
        month.send_keys('12')

        year = driver.find_element_by_id('year')
        year.send_keys('2000')

        # 8. Wybierz 'Kraj i region'
        country = driver.find_element_by_name('country')
        country.click()
        country.send_keys('Polska')
        country.send_keys(Keys.RETURN)

        # 9. Zaakceptuj warunki korzystania.
        warunki_korzystania = driver.find_element_by_xpath('//*[@id="registerform"]/div[5]/div[1]/div[1]/div[1]/label/span[2]')
        warunki_korzystania.click()

        ###TEST###
        # Szukam bledow na stronie
        errors=driver.find_elements_by_id('emailError')
        # Szukam widocznych bledow
        visible_errors=[]
        for e in errors:
            if e.is_displayed():
                visible_errors.append(e)
        # Sprawdzam, czy widoczny jest jeden blad
        # print(len(visible_errors))
        assert len(visible_errors) == 1
        # Sprawdzam tresc bledu
        # print(visible_errors[0].text)
        assert visible_errors[0].text=="Adres e-mail jest nieprawidlowy"

        # Sprzatam po tescie.
        def tearDown(self):
            self.driver.quit()
