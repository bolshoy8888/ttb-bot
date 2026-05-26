file = open("coins.txt", "r")
coins = file.read().splitlines()
file.close()
running = True
while running:
    print("1 - Показать монету")
    print("2 - Добавить монету")
    print("3 - Удалить монету")
    print("4 - Выход")
    choice = input ("Выбери действие: ")
    if choice == "1":
        print(coins)
    elif choice == "2":
        coin = input("Введите монету: ")
        coins.append(coin)
        file = open("coins.txt","w") 
        for coin in coins:
            file.write(coin + "\n") 
        file.close()      
    elif choice == "3":
        coin = input("Какую монету удалить: ")
        if coin in coins:
            coins.remove(coin)
            print("Монета удалена")
            file = open("coins.txt", "w")
            for coin in coins:
                file.write(coin +"\n")
            file.close()        
        else:
            print("Такой монеты нет")    
    elif choice == "4":
        running = False
    else:
        print("Неизвестная команда")            