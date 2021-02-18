
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH, options=options)


driver.get("https://careers.truist.com/ListJobs/All/")
search = driver.find_element_by_id("keyword-search")
search.send_keys("data")


search = driver.find_element_by_id("btnSearch")
search.send_keys(Keys.ENTER)
time.sleep(3)

elements = driver.find_elements_by_class_name("coloriginaljobtitle")

for element in elements:
    title = element.get_attribute('textContent')
    title = title.lstrip()
    title = title.rstrip()
    print(title)

time.sleep(3)
driver.quit()



