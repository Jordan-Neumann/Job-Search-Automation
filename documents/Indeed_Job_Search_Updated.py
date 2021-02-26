
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH, options=options)

def search(what, where):

    website = "https://www.indeed.com/"
    driver.get(website)
    search = driver.find_element_by_id("text-input-what")
    search.send_keys(what)
    search.send_keys(Keys.ENTER)

    try:
        location = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "where"))
    )
    
    except:
        driver.quit()

    search = driver.find_element_by_id("where")
    search.clear()
    search.send_keys(where)
    search.send_keys(Keys.ENTER)

search("data science", "United States")

url = driver.current_url
titles_list = []
companies_list = []
ratings_list = []
summary_list = []
job_list = []

for i in range(0,50,10):

    num = f"&start={i}"
    driver.get(url+num)
    print(url+num)

    results = driver.find_element_by_id("resultsCol")
    titles = results.find_elements_by_tag_name("h2")
    companies = driver.find_elements_by_class_name("company")
    ratings = driver.find_elements_by_class_name("ratingsContent")
    summary = driver.find_elements_by_class_name("summary")
  
    for t, c, r, s in zip(titles, companies, ratings, summary):
        
        title = t.find_element_by_tag_name("a")
        title = title.get_attribute('textContent').strip()
        company = c.get_attribute('textContent').strip()
        rating = r.get_attribute("textContent").strip()
        summary = s.get_attribute("textContent").strip()

        jobs = {'title': title,
                'company': company,
                'rating': rating,
                'summary': summary}
        
        job_list.append(jobs)

df = pd.DataFrame(job_list)
df.to_csv('jobs2.csv', index = False, header = True)

time.sleep(10)
driver.quit()

