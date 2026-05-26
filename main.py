import random
play_again = "yes"
while play_again == "yes":

     secret = random.randint(1,100)
     guess = 0
     attempts = 0

     while guess != secret:

        guess = int(input("Угадай число от 1 до 100: "))
        attempts += 1
        if guess > secret:
            print("Слишком много братишка")
        elif guess < secret:
            print("Слишком мало братишка")   
        if attempts >= 5: 
            print("GAME OVER")  
            break
        if guess == secret:        
            print("Тигр!")    
            print("Количевство попыток:", attempts) 
     play_again = input("Еще попытку? yes/no: ")