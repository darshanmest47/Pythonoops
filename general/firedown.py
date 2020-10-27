from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

fp = FirefoxProfile()
fp.set_preference("browser.download.manager.showWhenStarts", False)
fp.set_preference("browser.download.manager.showAlertOnComplete", False)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
fp.set_preference("browser.download.dir", "C:\\Users\\Darshan\\Desktop\\resumes")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)

driver.get("https://docupub.com/pdfconvert/")
wc = WebDriverWait(driver, 50)
wc.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@type='file']")))
driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
    "C:\\Users\\Darshan\\Desktop\\resumes\\Darshan_Resume.docx")

wc.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='uploadBtn']")))
driver.find_element(By.XPATH, "//input[@id='uploadBtn']").click()

wc.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Giri')]")))
driver.find_element(By.XPATH, "//a[contains(text(),'Dar')]").click()

handles = driver.window_handles

print(len(handles))
driver.switch_to.window(handles[1])
wc.until(expected_conditions.title_contains('Darshan'))
print(driver.title)
wc.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@id='download']")))
driver.find_element(By.XPATH, "//button[@id='download']").click()



