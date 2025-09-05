from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np

# Set up ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

topurl = "https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/schedule/#fromDate=2025-06-08&gender=men&undefined=men"
url = "https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/schedule/21444/?match=germany-vs-canada"
url2 = "https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/schedule/21446/?match=China-vs-Serbia"
driver.get(topurl)

match_urls = []
driver.implicitly_wait(5)
#matches = driver.find_elements(By.CLASS_NAME, "vbw-gs2-mc-wrap")
matches = driver.find_elements(By.CSS_SELECTOR, ".vbw-gs2-matches .vbw-gs2-date-row .vbw-gs2-date-body .vbw-gs2-comp-row.active .vbw-gs2-comp-body .vbw-gs2-match-item.vbw-mu-finished:not(.hidden)")
for match in matches:
    print(match)
    mcard = match.find_element(By.CSS_SELECTOR, ".vbw-gs2-match-data-card .vbw-gs2-mc-wrap")
    link = mcard.get_attribute("href")
    #print(link)
    match_urls.append(link)
for l in match_urls:
    print(l)

# statsA = driver.find_elements(By.CSS_SELECTOR, ".-td-teamA")[:3]
# statsB = driver.find_elements(By.CSS_SELECTOR, ".-td-teamB")[:3]
# statsAB = zip(statsA, statsB)
# statslst = []
# for stat in statsAB:
#     print("this is stat: ", stat)
#     s = stat.get_attribute("textContent")
#     statslst.append(int(s))
# print(statslst)



print("thats it")