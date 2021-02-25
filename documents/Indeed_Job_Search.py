
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH, options=options)

driver.get("https://www.indeed.com/")
search = driver.find_element_by_id("text-input-what")
search.send_keys("data science")
search.send_keys(Keys.ENTER)
time.sleep(5)

search = driver.find_element_by_id("where")
search.clear()
search.send_keys("United States")
search.send_keys(Keys.ENTER)
time.sleep(5)

link = driver.find_element_by_class_name("no-wrap")
link = link.find_element_by_partial_link_text("date")
link.send_keys(Keys.ENTER)


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
summary = driver.find_elements_by_class_name("summary")

joblist = []

for t, c, r, s in zip(titles, companies, ratings, summary):
    title = t.find_element_by_tag_name("a")
    title = title.get_attribute('textContent')
    title = title.strip()

    company = c.get_attribute('textContent')
    company = company.strip()

    rating = r.get_attribute("textContent")
    rating = rating.strip()

    summary = s.get_attribute("textContent")
    summary = summary.strip()

    jobs = {'title': title,
            'company': company,
            'rating': rating,
            'summary': summary}
    
    joblist.append(jobs)

df = pd.DataFrame(joblist)
df.to_csv('jobs.csv', index = False, header = True)

time.sleep(10)
driver.quit()
