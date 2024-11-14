import requests
response = requests.get("https://bank.gov.ua/NBU_Exchange/exchange_site?start=20241020&end=20241024&valcode=USD&sort=exchangedate&order=desc&json")
print(response)
print(response.content)
print(response.json())
response_dict = response.json()[0]
print(response_dict)
for item in response_dict:
    print(item)
print("---")
for item in response.json():
    print(item['exchangedate'], item['rate'])