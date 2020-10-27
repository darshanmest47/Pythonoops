from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()
options.add_argument('--incognito')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.maximize_window()
driver.get('https://www.gmail.com')

driver.find_element(By.XPATH, "//input[@type='email']").send_keys("darshanmesta33@gmail.com")
driver.find_element(By.XPATH, "//div[@class='VfPpkd-RLmnJb']").click()
    # WebDriverWait(driver, 300).until(
    #     expected_conditions.presence_of_element_located((By.XPATH, "//div[text()='Compose']")))
    #
    # driver.find_element(By.XPATH, "//div[text()='Compose']").click()
    #9999
    # WebDriverWait(driver, 200).until(
    #     expected_conditions.presence_of_element_located((By.XPATH, "//textarea[@name='to' and @id=':105']")))
    # driver.find_element(By.XPATH, "//textarea[@name='to' and @id=':105']").send_keys("surajmesta47@gmail.com")



