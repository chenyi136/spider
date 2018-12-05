import requests
import bs4
import csv

# headers={'User-Agent':' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}

data=requests.get("http://mark.mycar168.com/")
soup=bs4.BeautifulSoup(data.text,"html.parser")
# print(soup.prettify())

carCategory=soup.find_all('div',class_='car_py_con')
# print(carCategory)
# with open('Europe.csv','w',encoding='utf-8') as f:
#     writer=csv.writer(f)
brands1=carCategory[0].find_all('p',class_='p1')
brands2=carCategory[1].find_all('p',class_='p1')
brands3=carCategory[2].find_all('p',class_='p1')
brands4=carCategory[3].find_all('p',class_='p1')
brands5=carCategory[4].find_all('p',class_='p1')

# print(brands1[1].a.children)
# for d in brands1[1].a.children:
#     print(d)
# print(brands2)

with open('Europe.csv','w') as f1:
     writer=csv.writer(f1)
     writer.writerow(['id', 'name'])
     i=1
     for data in brands1:

        writer.writerow([i,data.a.strong.string])
        i+=1

with open('Ameica.csv', 'w') as f2:
    writer = csv.writer(f2)
    writer.writerow(['id', 'name'])
    i = 1
    for data in brands2:
        writer.writerow([i, data.a.strong.string])
        i += 1

with open('japan.csv', 'w') as f3:
    writer = csv.writer(f3)
    writer.writerow(['id', 'name'])
    i = 1
    for data in brands3:
        writer.writerow([i, data.a.strong.string])
        i += 1

with open('Southkorea.csv', 'w') as f4:
    writer = csv.writer(f4)
    writer.writerow(['id', 'name'])
    i = 1
    for data in brands4:
        writer.writerow([i, data.a.strong.string])
        i += 1

with open('China.csv', 'w') as f5:
    writer = csv.writer(f5)
    writer.writerow(['id', 'name'])
    i = 1
    for data in brands5:
        writer.writerow([i, data.a.strong.string])
        i += 1
