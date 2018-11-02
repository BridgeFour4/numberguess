#nathan broadbent, Kaleb Beck
#11/18
import random
def check_int(message="enter a number",a,b):
    x=1
    while x==1:
        check=input(message)
        if check.isdigit() :
            check=int(check)
            if  check>a and check<b:
                break
    return check
   

def random_game(a=1, b=100, c=5):
    print(" guess a number between",a,"and",b,"if you can figure it out within",c,"guesses you win")
    number= random.randint(a,b)
    guess_count=0
    while guess_count <c:
        guess= check_int("enter a number", a,b)
        guess_count+=1
        if guess == number:
            print("You win! it took you",guess_count,"guesses")
            break
        else:
            if guess > number:
                print("You guessed too high, guess again")
                if guess>b:
                    print("that's not even a option you just wasted a guess")
            elif guess<number:
                print("You guessed too low, guess again")
                if guess<a:
                    print("that's not even a option you just wasted a guess")
    if guess_count>=c:
        print("you lose the number was ",number)
    main_menu()
                
            

def game_credits():
    print("created by Nathan Broadbent, Kaleb Beck")

def options():
    print("We have a few more games for you one is the main random game that you choose the parameters\n one is where the computer guesses your number\n and the last is a coin flip game")
    game_choice=check_int("computer guess(1), flip coin(2), main(3), quit(4)",0,5)
    if game_choice==1:
        comp_guess()
    elif game_choice==2:
        flip_coin()
    elif game_choice==3:
        a=check_int("enter the lower number",0,500)
        b=check_int("enter the higher number",0,500)
        c=check_int("enter the guess  number",0,50)
        random_game(a, b, c)
    else:
        main_menu()
    
    
    
def comp_guess():
    print("enter a number between 1 and 100 and the computer will guess that number")
    number=check_int("enter a number between 1 and 100",1,100)
    compGuess=0
    a=1
    b=100
    guess_count=0
    while number !=compGuess:
        compGuess= random.randint(a,b)
        print(compGuess)
        guess_count+=1
        if compGuess== number:
            print("The computer guessed your number it took ",guess_count, "tries ")
        else:
            if compGuess> number:
                b=compGuess
            elif compGuess< number:
                a=compGuess
        
    
    
    
#def flip_coin

def main_menu():
    print("\nWelcome to random number guess")
    while True :
        game = input("were would you like to go: Credits, Play, Options, Quit?")
        if  game.lower()=="play":
            random_game()
        elif game.lower() == "options":
            options()
        elif game.lower() == "credits":
            game_credits()
        elif game.lower() == "quit":
            print("Goodbye then!")
            break
        else:
            print("We didn't  get that try again")

main_menu()
        
    
    
    
