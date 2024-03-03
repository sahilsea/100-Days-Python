from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome Open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options= chrome_options)
driver.get('https://www.python.org/')

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# print(f'The price is {price_dollar.text}.{price_cents.text}')

# search_bar = driver.find_element(By.NAME, value= 'q')
# print(search_bar.get_attribute('placeholder'))

# search_bar = driver.find_element(By.NAME, value= 'q')
# download_widget = driver.find_element(By.XPATH, value= '//*[@id="content"]/div/section/div[1]/div[2]/h2')
# print(download_widget.text)
# date_dict = { key : value }
for i in range(1,6):
    date_time = driver.find_element(By.CSS_SELECTOR, value = f'#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li:nth-child({i}) > time')
    event = driver.find_element(By.CSS_SELECTOR, value = f'#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li:nth-child({i}) > a')
    print(event.text)



# driver.close()
driver.quit()