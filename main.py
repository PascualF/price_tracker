import requests
from bs4 import BeautifulSoup as bs
import smtplib



def check_price():
    base_url = 'https://www.olx.pt/'
    url = 'https://www.olx.pt/lazer/bilhetes-espectaculos/q-olivia-rodrigo/?search%5Border%5D=created_at:desc'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    print(res)

    soup = bs(res.text, 'html.parser')


    title = soup.find(class_="css-16v5mdi er34gjf0").get_text()
    date = soup.find(class_="css-1a4brun er34gjf0").get_text().split(' - ')
    price = soup.find(class_='css-tyui9s er34gjf0').get_text()
    tickets_quantity = title.count('2')

    if tickets_quantity == 1:
        price = int(price[:4])
        price = int(price / 2)
        price = str(price) + ' €'


    #price_all = soup.find_all(class_='css-tyui9s er34gjf0')
    #print(price_all)
    print(title)
    print(date[-1])
    print(price)
    print(type(price))
    print(tickets_quantity)



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('pascualfelicio@gmail.com', 'oezr amuo wkno auzn')    

    subject = 'Checka o Preço!!!'
    body = 'Vai ver '

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'pascualfelicio@gmail.com',
        msg
    )

    server.quit()


check_price()