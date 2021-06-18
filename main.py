from bs4 import BeautifulSoup
import requests,json,time

token = 'kKRfOPZm8fPlxbTuqI05FD8eG7VJJ4PWZPFmT3D6ZOj'
def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code


with open('filter.json' , 'r', encoding="utf-8") as reader:
    filterlist = json.loads(reader.read())
processedlist =  []


while(1):
    res = requests.get('https://www.chickpt.com.tw/cases')
    soup = BeautifulSoup(res.text,'html.parser')
    jobs = soup.find("ul", {"id": "job-list"}).find_all('li')
    for job in jobs:
        jobsName = job.find("h2", {"class": "ellipsis-job-name"}).text.strip()
        for filtername in filterlist:
            if filtername in jobsName and jobsName not in processedlist:
                processedlist.append(jobsName)
                lineNotifyMessage(token,jobsName+'\n'+'https://www.chickpt.com.tw/'+job.find("a", {"class": "job-list-item"}).get('href'))
    
    time.sleep(600)
