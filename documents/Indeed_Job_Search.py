
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH, options=options)

driver.get("https://www.indeed.com/")
search = driver.find_element_by_id("text-input-what")
search.send_keys("data")
search.send_keys(Keys.ENTER)
time.sleep(2)

search = driver.find_element_by_id("where")
search.clear()
search.send_keys("United States")
search.send_keys(Keys.ENTER)

results = driver.find_element_by_id("resultsCol")
titles = results.find_elements_by_tag_name("h2")
print(len(titles))
for titles1 in titles:
    title = titles1.find_element_by_tag_name("a")
    title = title.get_attribute('textContent')
    print(title)

time.sleep(5)
driver.quit()
