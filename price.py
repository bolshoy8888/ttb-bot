import requests
coin = input("Введите монету: ")
url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
response = requests.get(url)
data = response.json()
if "symbol" in data:
    print("____________________")
    print(f"Монета: {data['symbol']}")
    print(f"Цена: {data['price']}$")
    print("____________________")
else:
    print("Такой монеты нет")    