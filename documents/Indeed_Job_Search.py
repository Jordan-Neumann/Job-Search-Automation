
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

try:
    resultsCol = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "resultsCol"))
    )

    company = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "company"))
    )

    ratingsContent = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ratingsContent"))
    )
    
except:
    driver.quit()

results = driver.find_element_by_id("resultsCol")
titles = results.find_elements_by_tag_name("h2")
companies = driver.find_elements_by_class_name("company")
ratings = driver.find_elements_by_class_name("ratingsContent")

print(len(companies))
for t, c, r in zip(titles, companies, ratings):
    title = t.find_element_by_tag_name("a")
    title = title.get_attribute('textContent')
    title = title.lstrip()
    title = title.rstrip()

    rating = r.get_attribute("textContent")
    rating = rating.rstrip()

    company = c.get_attribute('textContent')
    print(title)
    print(company)
    print(rating)
    print()
    print()

time.sleep(10)
driver.quit()
