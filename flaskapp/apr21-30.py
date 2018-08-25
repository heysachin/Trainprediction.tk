
# Created by Sachin Dev on 29/06/18


from datetime import timedelta, date
import requests
from bs4 import BeautifulSoup
from models.trains.train import Train
from common.database import Database


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(2018, 4, 21)
end_date = date(2018, 4, 30)

Database.initialize()
Trains = Train.all()

for single_date in daterange(start_date, end_date):
    date = single_date.strftime("%Y-%m-%d")
    print(date)
    for train in Trains[1:]:
        train._id=train._id.zfill(5)
        print(train._id)
        request = requests.get("https://railenquiry.in/runningstatus/ " +train._id +"/"+date)
        content =request.content
        soup = BeautifulSoup(content, "html.parser")
        [s.extract() for s in soup('a')]
        [s.extract() for s in soup('input')]
        [s.extract() for s in soup('label')]
        [s.extract() for s in soup('small')]
        element = soup.find_all("tr" ,{"class" :"warning"})
        f = open('csv/apr3.csv', 'a')
        for element in element:
            x=element.get_text(",")
            x = x.strip().split(',')
            x=filter(('').__ne__, x)
            x=filter(('\n').__ne__, x)
            x=filter((' ').__ne__, x)
            x=filter(('-').__ne__, x)
            str1 = ','.join(x)
            print(str1)
            str1=str1+','+train._id+','+date
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
            str1 = str1 + ',' + train._id
            f.write(str1)
            f.write('\n')

        f.close()
