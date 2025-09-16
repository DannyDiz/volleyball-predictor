from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import numpy as np

# Set up ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# following link should be the schedule link that contains the first match of the tourney.
my_url = "https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/schedule/#fromDate=2025-06-07&gender=men&undefined=men"
not_schedule_end = True
driver.get(my_url)
driver.implicitly_wait(10)

match_urls = []

# Store scraped data
data = []

# navigate to each match data card which contains a link to the match's statistics
while not_schedule_end:
    matches = driver.find_elements(By.CSS_SELECTOR, ".vbw-gs2-matches .vbw-gs2-date-row .vbw-gs2-date-body .vbw-gs2-comp-row.active .vbw-gs2-comp-body .vbw-gs2-match-item.vbw-mu-finished:not(.hidden)")

    for match in matches:
        mcard = match.find_element(By.CSS_SELECTOR, ".vbw-gs2-match-data-card .vbw-gs2-mc-wrap")
        link = mcard.get_attribute("href")
        print(link)
        match_urls.append(link)
        cat = match.find_element(By.CSS_SELECTOR, ".vbw-round-pool-phase").get_attribute("textContent")
        if "Final 1-2" in cat:
            not_schedule_end = False

    button = driver.find_element(By.CLASS_NAME, "nav-right")
    button.click()
#print(match_urls)

# collect statistics from each match
for url in match_urls:
    print("scraping match stats")
    driver.get(url)
    driver.implicitly_wait(10)

    mid = int(driver.find_element(By.CLASS_NAME, "vbw-match-header").get_attribute("data-match-no"))
    teamA = driver.find_element(By.CLASS_NAME, "vbw-mu__team--home").get_attribute("textContent")[:-3]
    teamB = driver.find_element(By.CLASS_NAME, "vbw-mu__team--away").get_attribute("textContent")[:-3]
    print("match ", mid, ": ", teamA, " vs ", teamB)
    
    score = driver.find_element(By.CLASS_NAME, "vbw-mu__score").get_attribute("textContent")
    scoreA = int(score[0])
    scoreB = int(score[-1])
    resA = "W"
    resB = "L"
    if scoreB > scoreA:
        resA = "L"
        resB = "W"

    sets = driver.find_elements(By.CLASS_NAME, "vbw-mu__sets--result")[:5]
    set_scores = []
    for s in sets:
        scores = s.get_attribute("textContent")
        a, b = scores.split("-")
        print("A score: ", a)
        print("B score: ", b)
        try:
            a_num = int(a)
            set_scores.append(a_num)
        except ValueError: set_scores.append(np.nan)
        try:
            b_num = int(b)
            set_scores.append(b_num)
        except ValueError: set_scores.append(np.nan)
    print("length of set_scores: ", len(set_scores))
    print("set_scores: ", set_scores)

    statsA = driver.find_elements(By.CSS_SELECTOR, ".-td-teamA")[:3]
    statsB = driver.find_elements(By.CSS_SELECTOR, ".-td-teamB")[:3]
    skillsA = driver.find_elements(By.CSS_SELECTOR, ".-td-teamA")[5:8]
    skillsB = driver.find_elements(By.CSS_SELECTOR, ".-td-teamB")[5:8]
    statslst, skillslst = [], []
    
    if len(statsA) == 0:
        statslst = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
        skillslst = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
    else:
        statsAB = []
        skillsAB = []
        print("len(statsA) == len(skillsB): ", len(statsA) == len(skillsB))
        for i in range(len(statsA)):
            statsAB.append(statsA[i])
            statsAB.append(statsB[i])
            skillsAB.append(skillsA[i])
            skillsAB.append(skillsB[i])
        
        print("len(statsAB) == len(skillsAB): ", len(statsAB) == len(skillsAB))
        for i in range(len(statsAB)):
            st = statsAB[i].get_attribute("textContent")
            statslst.append(int(st))
            sk = skillsAB[i].get_attribute("textContent")
            skillslst.append(int(sk))

    # parse statistics into dataframe format
    # team A
    data.append({
        "matchid": mid,
        "team": teamA,
        "opponent": teamB,
        "result": resA,
        "sets won": scoreA,
        "sets lost": scoreB,
        "set1": set_scores[0],
        "set2": set_scores[2],
        "set3": set_scores[4],
        "set4": set_scores[6],
        "set5": set_scores[8],
        "attacks": statslst[0], 
        "blocks": statslst[2],
        "serves": statslst[4],
        "digs": skillslst[0],
        "receives": skillslst[2],
        "sets": skillslst[4]
    })

    # team B
    data.append({
        "matchid": mid,
        "team": teamB,
        "opponent": teamA,
        "result": resB,
        "sets won": scoreB,
        "sets lost": scoreA,
        "set1": set_scores[1],
        "set2": set_scores[3],
        "set3": set_scores[5],
        "set4": set_scores[7],
        "set5": set_scores[9],
        "attacks": statslst[1],
        "blocks": statslst[3],
        "serves": statslst[5],
        "digs": skillslst[1],
        "receives": skillslst[3],
        "sets": skillslst[5]
    })

    print("match stats done scraping")

# Save results to CSV
df = pd.DataFrame(data)
df.to_csv("volleyball_stats.csv", index=False)

print("Scraping complete! Data saved to volleyball_stats.csv")

# Close browser
driver.quit()