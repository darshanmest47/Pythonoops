from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
# options.add_argument('--incognito')
options.add_experimental_option("prefs", {"download.default_directory": "C:\\Users\\Darshan\\Desktop\\resumes"})

# options.add_experimental_option("download.default_directory=C:\\Users\\Darshan\\Desktop\\resumes")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://www.selenium.dev/downloads/")
driver.find_element(By.XPATH, "//div[@class='right']/p/a[contains(text(),'3.')]").click()
