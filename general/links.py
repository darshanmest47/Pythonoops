from packaging.requirements import URL
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--incognito')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://www.google.com')

list_items = driver.find_elements(By.TAG_NAME, 'a')

for ele in list_items:
    href = ele.get_attribute('href')
    url = requests.get(href)
    print(url.status_code)

samp_url = "http://mynewportofolio1.herokuapp.com/"
samp_res = requests.get(samp_url)
print(samp_res.status_code)

time.sleep(5)
driver.quit()
