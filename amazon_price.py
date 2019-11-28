import requests
from bs4 import BeautifulSoup
import smtplib


def send_email(a):
    s = smtplib.SMTP("smtp.gmail.com", 587)

    s.starttls()

    s.login("lolturcia@gmail.com","mandarinele1234")

    message = 'Subject: {}\n\n{}'.format('Alert for reduced in price', "The price is: {}.{}$".format(str(a)[0:2],str(a)[2:4]))

    s.sendmail("lolturcia@gmail.com", "mtrifan10@gmail.com", message)

    s.quit()

page_url = "https://www.amazon.com/HyperX-Cloud-Gaming-Headset-KHX-HSCP-RD/dp/B00SAYCXWG/ref=sxin_2_ac_d_rm?ac_md=0-0-aHlwZXJ4IGNsb3VkIDI%3D-ac_d_rm&keywords=hyperx+cloud+2&pd_rd_i=B00SAYCXWG&pd_rd_r=1189b394-e14f-46d6-b6a6-1509ff7e2410&pd_rd_w=zOHEc&pd_rd_wg=Seexx&pf_rd_p=39892eb5-25ed-41d8-aff1-b659c9b73760&pf_rd_r=NB53DCKGGCM7FP0GFE06&psc=1&qid=1572950766"

browser_agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}

product_page = requests.get(page_url,headers=browser_agent)

soup = BeautifulSoup(product_page.content,'lxml')

page_title = soup.find(id="productTitle").get_text()

product_price = soup.find(id="priceblock_ourprice").get_text()

product_price = product_price.replace(".","")

final_price = float(product_price[1:5])

if final_price < 10000:
    send_email(final_price)

