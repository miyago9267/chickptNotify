from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests, json, time, os

def get_cases(filterlist, processedlist):
    processedlist = processedlist

    res = requests.get('https://www.chickpt.com.tw/cases')
    soup = BeautifulSoup(res.text,'html.parser')
    jobs = soup.find("ul", {"id": "job-list"}).find_all('li')
    for job in jobs:
        jobsName = job.find("h2", {"class": "ellipsis-job-name"}).text.strip()
        for filtername in filterlist:
            if filtername in jobsName and jobsName not in processedlist:
                processedlist.append(f'{jobsName}\nhttps://www.chickpt.com.tw/{job.find("a", {"class": "job-list-item"}).get("href")}')
    
    return processedlist