from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver_path = 'C:\\Users\\Hp\\Downloads\\chromedriver.exe'

    driver = webdriver.Chrome(driver_path, chrome_options=options)
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