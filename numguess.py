#nathan broadbent, Kaleb Beck
#11/18
import random
def check_int(message="enter a number",c=0,d=0):
    x=1
    while x==1:
        check=input(message)
        if check.isdigit() :
            check=int(check)
            if c==0:
                break
            if  check>=c and check<=d:
                break
            
    return check
   

def random_game(a=1, b=100, c=5):
    print(" \nguess a number between",a,"and",b,"if you can figure it out within",c,"guesses you win")
    number= random.randint(a,b)
    guess_count=0
    win=0
    while guess_count <c:
        guess= check_int("guess a number", a,b)
        guess_count+=1
        if guess == number:
            print("You win! it took you",guess_count,"guesses")
            win=1
            break
        else:
            if guess > number:
                print("You guessed too high, guess again")
            elif guess<number:
                print("You guessed too low, guess again")
    if guess_count>=c and win!=1:
        print("you lose the number was ",number)
    main_menu()
                
            

def game_credits():
    print("created by Nathan Broadbent, Kaleb Beck")
    main_menu()

def options():
    print("\nWe have a few more games for you one is the main random game that you choose the parameters\n one is where the computer guesses your number\n and the last is a coin flip game")
    game_choice=check_int("computer guess(1), flip coin(2), main(3), quit(4)")
    if game_choice==1:
        comp_guess()
    elif game_choice==2:
        flip_coin()
    elif game_choice==3:
        a=check_int("enter the lower number")
        b=check_int("enter the higher number")
        c=check_int("enter the guess  number")
        random_game(a, b, c)
    else:
        main_menu()
    
    
    
def comp_guess():
    print("\nenter a number between 1 and 100 and the computer will guess that number")
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
    main_menu()
        
    
    
    
def flip_coin():
    print("\ni will flip a coin try to guess correctly best 3 out of 5 wins")
    win=0
    loss=0
    while win<3 and loss<3:
        flip=random.randint(1,2)
        guess=check_int("heads (1) or  tails (2) ",1,2)
        if flip==1:
            face="heads"
        else:
            face="tails"
            
        if guess==flip:
            print("that is correct it was",face)
            win+=1
        else:
            print("wrong it was",face)
            loss+=1
    if win>=3:
        print("good job you win you guessed three of the five correctly")
    else:
        print("you lost you got three of the five wrong")
    main_menu()

        

def main_menu():
    print("\nWelcome to random number guess game")
    while True :
        game = input("where would you like to go: Credits, Play, Options, Quit?")
        if  game.lower()=="play":
            random_game()
            break
        elif game.lower() == "options":
            options()
            break
        elif game.lower() == "credits":
            game_credits()
            break
        elif game.lower() == "quit":
            print("Goodbye then!")
            break
        else:
            print("We didn't  get that try again")

main_menu()
        
    
    
    
