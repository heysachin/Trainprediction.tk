
from datetime import timedelta, date
import requests
from bs4 import BeautifulSoup
from models.trains.train import Train
from common.database import Database


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(2018, 1, 1)
end_date = date(2018, 8, 6)

Database.initialize()
Trains = Train.all()

for single_date in daterange(start_date, end_date):
    date = single_date.strftime("%Y-%m-%d")
    print(date)
    request = requests.get("https://railenquiry.in/runningstatus/16343/"+date)
    content =request.content
    soup = BeautifulSoup(content, "html.parser")
    [s.extract() for s in soup('a')]
    [s.extract() for s in soup('input')]
    [s.extract() for s in soup('label')]
    [s.extract() for s in soup('small')]
    element = soup.find_all("tr" ,{"class" :"warning"})
    f = open('csv/16343.csv', 'a')
    for element in element:
        x=element.get_text(",")
        x = x.strip().split(',')
        x=filter(('').__ne__, x)
        x=filter(('\n').__ne__, x)
        x=filter((' ').__ne__, x)
        x=filter(('-').__ne__, x)
        str1 = ','.join(x)
        print(str1)
        str1=str1+',16343,'+date
        f.write(str1)
        f.write('\n')

    element = soup.find_all("tr",{"class" :"success "})
    for element in element:
        x=element . get_text(",")
        x = x.strip().split(',')
        x = filter(('').__ne__, x)
        x = filter(('\n').__ne__, x)
        x = filter((' ').__ne__, x)
        x = filter(('-').__ne__, x)
        str1 = ','.join(x)
        print(str1)
        str1 = str1 + ',16343'
        f.write(str1)
        f.write('\n')
        f.close()
