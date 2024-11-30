import random

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

def fizz_buzz_game():
    scor = 0
    
    while True:
        num = random.randint(1, 100)  
        correct_answer = fizz_buzz(num)
        
        player_answer = input(f"What's your answer for {num}? ")
        
        if player_answer.strip().lower() == correct_answer.lower():
            print("You are correct....")
            score += 1
        else:
            print(f"Sorry..., you lost. The correct answer is '{correct_answer}'.")
            break
    
    print(f"Your final scor is: {scor}")


fizz_buzz_game()
