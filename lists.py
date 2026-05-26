coins = ["BTC", "ETH", "SOL"]
print(coins[0])
print(coins[1])
print(coins[2])
coins.append("DOGE")
print(coins)
coins.remove("ETH")
print(coins)
coins[0]= "BTC_NEW"
print(coins)
print("DOGE" in coins)
for coin in coins:
    print("Монета:", coin)
new_coin = input("Добавь монету: ") 
coins.append(new_coin)
print(coins)   