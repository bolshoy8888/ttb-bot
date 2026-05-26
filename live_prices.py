import requests
import time
import os 
file = open("coins.txt", "r")
coins = file.read().splitlines()
file.close()
while True:
    os.system("clear")
    print("===== LIVE CRYPTO PRICES =====")
    for coin in coins:
        url =f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
        response = requests.get(url)
        data = response.json()
        print("____________________")
        print(f"Монета:{data['symbol']}")
        print(f"Цена:{data['price']}$")
        print("____________________")
    time.sleep(10)    