from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import sys   #used to set the proper exit code


def test_scores_service(application_url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(application_url)
    score = 0
    try:
        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text)
    except:
        print("ID wasnot found")
        pass

    if 1 <= score <= 1000:
        return True
    else:
        return False

def main_function():
    application_url= "http:127.0.0.1:5000"
    if test_scores_service(application_url):
        print("done")
        sys.exit(0)
    else:
        sys.exit(-1)


main_function()