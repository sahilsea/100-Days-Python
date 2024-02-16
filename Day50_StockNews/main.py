import requests
from twilio.rest import Client
import os
from datetime import datetime as dt
# import datetime

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')

current_day = dt.now()
day = current_day.day - 1
month = current_day.month
# time = current_day.time
# print(day)

# Constants of the company.
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Parameters of the Stock and News
stock_params = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': 'TSLA',
    'interval': '60min',
    'apikey': 'D0WY8KRZDGV7J80W'
}
news_params = {
    'q': 'tesla, elon',
    # 'country': 'us',
    'sortBy': 'relevancy',
    'from': f'2024-02-{day-1}',
    'apikey': '78904f0541ad4d4cbec0619448c01f07',
    'language': 'en',
    
}

# API for the Stock and news and twilio
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "http://newsapi.org/v2/everything"

# News response
response = requests.get(url=NEWS_ENDPOINT, params= news_params)
# print(response.status_code)
response.raise_for_status()
news_data = response.json()

# Stock response
response2 = requests.get(url=STOCK_ENDPOINT, params= stock_params)
# print(response.status_code)
response2.raise_for_status()
stock_data = response2.json()
print(stock_data)

# Closing Price
# 2024-02-{day} 19:00:00
crnt_closing_price = stock_data['Time Series (60min)'][f'2024-02-{day} 19:00:00']['4. close']
ystrday_closing_price = stock_data['Time Series (60min)'][f'2024-02-{day-1} 19:00:00']['4. close']

print(f'{crnt_closing_price} and {ystrday_closing_price}')
# Price Change
price_chng = float(crnt_closing_price) - float(ystrday_closing_price)
percnt_pric_chng = int((float(crnt_closing_price)-float(ystrday_closing_price))/(float(ystrday_closing_price))*100)
print(f'percnt_pric_chng {percnt_pric_chng}')
print(f'The change in stock price of {COMPANY_NAME} from yesterday is: {price_chng}$')

# Symbol
symbol = ''
if percnt_pric_chng < 0 :
        symbol ='🔻'
else:
        symbol ='🔺'
        

# News Output
if price_chng > 5:
        client = Client(account_sid, auth_token,)
        message = client.messages \
        .create(
            body = f"TSLA: {symbol}{percnt_pric_chng}%\n 1.  {news_data['articles'][0]['title']}\n 2. {news_data['articles'][2]['title']}\n 3. {news_data['articles'][5]['title']}",
            from_= "+17622131855",
            to = "+917321843138"
        )
        print(message.status)
print("Some news on Tesla")

# print(news_data['articles'][0]['title'])
# print(news_data['articles'][2]['title'])
# print(news_data['articles'][3]['title'])
# print(news_data['articles'][8]['title'])
# print(news_data['articles'][5]['title'])

# stock_data['Time Series (60min)'][f'2024-02-{day-1} 19:00:00']['4. close']
# stock_data['Time Series (60min)'][f'2024-02-{day} 19:00:00']['4. close'] = data for the current closing day



## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

