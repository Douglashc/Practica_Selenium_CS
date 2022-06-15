from selenium import webdriver

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver_path = 'C:\\Users\\Hp\\Downloads\\chromedriver.exe'

    driver = webdriver.Chrome(driver_path, chrome_options=options)
    driver.get('https://www.leagueoflegends.com/')