import requests
import matplotlib.pyplot as plt
resp = requests.get("https://bank.gov.ua/NBU_Exchange/exchange_site?start=20241020&end=20241024&valcode=USD&sort=exchangedate&order=desc&json")
print(resp)
print(resp.content)
print(resp.json())
response_dict= resp.json()[0]
print(response_dict)
for iten in response_dict:
    print(iten)
print("----")
for iten in resp.json():
     print(iten['exchangedate'], iten['rate'])
dates = []
rates = []
for item in resp.json():
    dates.append(item['exchangedate'])
    rates.append(item['rate'])
plt.plot(dates, rates)
plt.xlabel('Дата')
plt.ylabel('Курс (UAH/USD)')
plt.title('Динамика курса доллара США')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()