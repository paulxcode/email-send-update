import requests
from bs4 import BeautifulSoup
import smtplib
from apscheduler.schedulers.blocking import BlockingScheduler
from hashlib import new

def data_scraping ():
    req=requests.get("LINK TO PRODUCT")
    soup=BeautifulSoup(req.text, "html.parser")
    price=soup.find('p', attrs={'class': 'product-new-price'}).text
    new_price=price[0:5]
    new_price=new_price.replace(".", "")
    print(new_price)

def trimitere_email ():
    server = smtplib.SMTP('mail.x-it.ro', 26)
    server.starttls()
    server.login("*","stiinte217_2022")
    server.sendmail("*", "trifanpaul99@gmail.com", "UPDATE: AVEM O MODIFICARE DE PRET")
    print("Emailul a fost trimis cu succes")
    server.quit

data_scraping()
trimitere_email()
