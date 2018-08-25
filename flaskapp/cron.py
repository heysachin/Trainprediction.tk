

# Created by Sachin Dev on 29/06/18

import requests
from bs4 import BeautifulSoup
from models.trains.train import Train
from common.database import Database


Database.initialize()
Trains=Train.all()

for train in Trains[272:]:
    request = requests.post("https://trainstatus.info", data={'date':'today','train':train._id,'runningformsubmit':'1'})
    content=request.content
    soup = BeautifulSoup(content, "html.parser")
    soup.script.decompose()
    [s.extract() for s in soup('script')]
    [s.extract() for s in soup('td',{'colspan':'7'})]
    element = soup.find("tr", {"class":"success"})
    element2 = soup.find_all("tr")
    for n in element2[1:-1]:
        print(n.get_text(","))
        myData = n.get_text(",")
        if myData is not "":
            f = open('csvfile.csv', 'a')
            f.write(myData+','+train._id)
            f.write('\n')
            f.close()

    #Yesterday's Data
for train in Trains[272:]:
    request = requests.post("https://trainstatus.info", data={'date':'yesterday','train':train._id,'runningformsubmit':'1'})
    content=request.content
    soup = BeautifulSoup(content, "html.parser")
    soup.script.decompose()
    [s.extract() for s in soup('script')]
    [s.extract() for s in soup('td',{'colspan':'7'})]
    element = soup.find("tr", {"class":"success"})
    element2 = soup.find_all("tr")
    for n in element2[1:-1]:
        print(n.get_text(","))
        print(n)
        myData = n.get_text(",")
        if myData is not "":
            f = open('csvfile.csv', 'a')
            f.write(myData+','+train._id)
            f.write('\n')
            f.close()

   #2 Days Before Data
for train in Trains[272:]:
    request = requests.post("https://trainstatus.info", data={'date':'2daysago','train':train._id,'runningformsubmit':'1'})
    content=request.content
    soup = BeautifulSoup(content, "html.parser")
    soup.script.decompose()
    [s.extract() for s in soup('script')]
    [s.extract() for s in soup('td',{'colspan':'7'})]
    element = soup.find("tr", {"class":"success"})
    element2 = soup.find_all("tr")
    for n in element2[1:-1]:
        print(n.get_text(","))
        print(n)
        myData = n.get_text(",")
        if myData is not "":
            f = open('csvfile.csv', 'a')
            f.write(myData+','+train._id)
            f.write('\n')
            f.close()

   #3 Days Before Data
for train in Trains[272:]:
    request = requests.post("https://trainstatus.info", data={'date':'3daysago','train':train._id,'runningformsubmit':'1'})
    content=request.content
    soup = BeautifulSoup(content, "html.parser")
    soup.script.decompose()
    [s.extract() for s in soup('script')]
    [s.extract() for s in soup('td',{'colspan':'7'})]
    element = soup.find("tr", {"class":"success"})
    element2 = soup.find_all("tr")
    for n in element2[1:-1]:
        print(n.get_text(","))
        print(n)
        myData = n.get_text(",")
        if myData is not "":
            f = open('csvfile.csv', 'a')
            f.write(myData+','+train._id)
            f.write('\n')
            f.close()
            
   #4 Days Before Data
for train in Trains[272:]:
    request = requests.post("https://trainstatus.info", data={'date':'4daysago','train':train._id,'runningformsubmit':'1'})
    content=request.content
    soup = BeautifulSoup(content, "html.parser")
    soup.script.decompose()
    [s.extract() for s in soup('script')]
    [s.extract() for s in soup('td',{'colspan':'7'})]
    element = soup.find("tr", {"class":"success"})
    element2 = soup.find_all("tr")
    for n in element2[1:-1]:
        print(n.get_text(","))
        print(n)
        myData = n.get_text(",")
        if myData is not "":
            f = open('csvfile.csv', 'a')
            f.write(myData+','+train._id)
            f.write('\n')
            f.close()

print("Finished")
