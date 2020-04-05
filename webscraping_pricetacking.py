import requests #pull data form website
import smtplib #for email protocol
import time #for delay
from bs4 import BeautifulSoup #parse elements from website

#URL of the product
URL = 'https://www.amazon.de/Samsung-RU7179-Fernseher-Triple-Modelljahr/dp/B07PQ8VKWX/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=samsung+curved+tv&qid=1586094144&sr=8-5'
#search for 'my user agent'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser') #start parser
    #try parsing the title
    try:
        title = soup.find(id="productTitle").get_text()
    except AttributeError:
        print("Product Title unknown")
    #try parsing the price and convert it to a number
    try:
        price = soup.find(id="priceblock_ourprice").get_text()
    except AttributeError:
        print("price unknown")
    converted_price = float(price[0:3])

    print(title.strip()) #print the title of the product
    print(converted_price) #print the price

    if(converted_price < 400): #send mail if price is lower thana 400
        send_mail()

def send_mail(): #build connection to the gmail server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('eren.uslu94@gmail.com', 'insert_password_here')
    #content of the sent email
    subject = "Price fell down"
    body = "The price of the item fell. Check Amazon: https://www.amazon.de/Samsung-RU7179-Fernseher-Triple-Modelljahr/dp/B07PQ8VKWX/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=samsung+curved+tv&qid=1586094144&sr=8-5"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'eren.uslu94@gmail.com',
        msg
    )
    print("Email has been sent")

    server.quit() #disconnect from server

    while(true): #check for price once daily
        check_price()
        time.sleep(86400) #sleep for a day
