from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://youtube.com')

searchbox = driver.find_element('//*[@id="search"]')
searchbox.send_keys('Hum Nashe Me To Nahin')

searchButton = driver.find_element('//*[@id="search-icon-legacy"]')
searchButton.click()