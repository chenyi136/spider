import requests
import bs4
import csv

data=requests.get("http://fact.mycar168.com/")
soup=bs4.BeautifulSoup(data.text,"html.parser")
# print(soup.prettify())


areas=soup.find_all('strong',class_='area')
carCategory=soup.find_all('div',class_='brandList_')

# for datas in carCategory:
print(carCategory)


# brands1=carCategory[0].find_all('p',class_='p1')
# brands2=carCategory[1].find_all('p',class_='p1')
# brands3=carCategory[2].find_all('p',class_='p1')
# brands4=carCategory[3].find_all('p',class_='p1')
# brands5=carCategory[4].find_all('p',class_='p1')


with open('areaCar.csv','w') as f1:

    writer = csv.writer(f1)
    writer.writerow(['area', 'name'])
    i=0
    for datas in carCategory:
        data = datas.find_all('p', class_='p1')
        for brand in data:
            writer.writerow([areas[i].string,brand.a.strong.string])
        i+=1
