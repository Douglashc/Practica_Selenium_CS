from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

if __name__ == '__main__':

    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://www.leagueoflegends.com/')

    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                           'a._2I66LI-wCuX47s2um7O7kh riotbar-anonymous-link _3qlG68WiAAf2HCeuzuwHXj riotbar-account-action'.replace(
                                               ' ', '.')))) \
        .click()

    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.NAME,
                                           'username'))) \
        .send_keys('leo161998')

    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.NAME,
                                           'password'))) \
        .send_keys('comida544533')

    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                           'button.mobile-button mobile-button__submit'.replace(
                                               ' ', '.')))) \
        .click()

    time.sleep(20)
    driver.quit()