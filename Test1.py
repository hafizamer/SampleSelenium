from selenium import webdriver
import time 
driver=webdriver.Chrome("/Users/hafiz/Documents/practice python/Selenium/FirstSeleniumProject/drivers/chromedriver.exe")
#driver=webdriver.Firefox()
#driver=webdriver.Ie()

driver.set_page_load_timeout(10)
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("facebook")
driver.find_element_by_name("btnK").click()
driver.find_element_by_partial_link_text("facebook.com").click()
time.sleep(4)
driver.quit()