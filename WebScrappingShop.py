import bs4
import urllib.request
import smtplib
import time

prices_list=[] # every time we call check_price we will add the new price to the list 

def check_price():
    url="https://www.flipkart.com/apple-macbook-air-m1-8-gb-256-gb-ssd-mac-os-big-sur-mgn63hn-a/p/itmde54f026889ce?pid=COMFXEKMGNHZYFH9&lid=LSTCOMFXEKMGNHZYFH9EOWT4E&marketplace=FLIPKART&q=macbook&store=6bo%2Fb5g&spotlightTagId=BestsellerId_6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=4fb39a2c-d8e7-43fb-826e-7d7393b7164e.COMFXEKMGNHZYFH9.SEARCH&ppt=sp&ppn=sp&ssid=uxnhq2ea4g0000001635765595057&qH=864faee128623e2f"
    sauce =urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce,"html.parser")

    #get price as a string
    price = soup.find(class_="_30jeq3 _16Jk6d").get_text()
    #convert string to float
    price = float(price.replace(",","").replace("₹","")) 
    print(price)
    prices_list.append(price)
    print(prices_list)
    return price

def send_mail(message):
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("mainak21.das@gmail.com","9233400128")
    s.sendmail("mainak21.das@gmail.com","mainak04.das@gmail.com",message)
    s.quit()

def check_price_decrease(prices_list):
    if prices_list[-1] < prices_list[-2]:
        return True
    else:
        return False

count=1
while True:
    current_price = check_price()
    if count > 1:
        flag = check_price_decrease(prices_list)
        if flag:
            reduced_price=prices_list[-1]-prices_list[-2]
            message=f"PRICE DROP ALERT!!!!\nHey Mainak!!HURRY UP!!\nYour Product(APPLE MacBook Air M1 - (8 GB/256 GB SSD/Mac OS Big Sur) MGN63HN/A  (13.3 inch, Space Grey, 1.29 kg))price has been reduced by ₹{reduced_price}."
            send_mail(message)
    time.sleep(3600)
    count+=1