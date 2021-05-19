from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'D:\\utsav\\'}
chrome_options.add_experimental_option('prefs', prefs)


driver = webdriver.Chrome(r"C:\Users\APURAV\PycharmProjects\selenium test\Browsers\chromedriver.exe", options=chrome_options)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/")
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(.,'File Upload')]").click();
time.sleep(2)

driver.find_element_by_id("file-upload").send_keys("C:\\Users\\APURAV\\Desktop\\uploaded_file.jpg")
time.sleep(2)

driver.find_element_by_id("file-submit").send_keys(Keys.ENTER)
time.sleep(2)

driver.get("http://the-internet.herokuapp.com/")
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(.,'File Download')]").click();
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(.,'anki.jpg')]").click();
time.sleep(2)

driver.get("http://the-internet.herokuapp.com/")
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(.,'Multiple Windows')]").click();
time.sleep(2)

driver.find_element(By.XPATH, "//a[contains(.,'Click Here')]").click();
time.sleep(2)





