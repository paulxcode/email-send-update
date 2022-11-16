import requests
from bs4 import BeautifulSoup
import smtplib
from apscheduler.schedulers.blocking import BlockingScheduler
from hashlib import new

def data_scraping ():
    req=requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-14-128gb-5g-midnight-mpuf3rx-a/pd/DR2Y4LMBM/?X-Search-Id=2ec11881bf73df410e54&X-Product-Id=101075717&X-Search-Page=1&X-Search-Position=0&X-Section=search&X-MB=0&X-Search-Action=view")
    soup=BeautifulSoup(req.text, "html.parser")
    price=soup.find('p', attrs={'class': 'product-new-price'}).text
    new_price=price[0:5]
    new_price=new_price.replace(".", "")
    print(new_price)

def trimitere_email ():
    server = smtplib.SMTP('mail.x-it.ro', 26)
    server.starttls()
    server.login("data_scraping@coneasorin.ro","stiinte217_2022")
    server.sendmail("data_scraping@coneasorin.ro", "trifanpaul99@gmail.com", "UPDATE: AVEM O MODIFICARE DE PRET")
    print("Emailul a fost trimis cu succes")
    server.quit

data_scraping()
trimitere_email()
