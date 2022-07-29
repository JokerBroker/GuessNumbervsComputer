import random
from turtle import up
def Input():
    guess_num=int(input("Insert a random number between 1 and 10 for the computer to guess:-"))
    computer_guess=random.randint(1,10)
    ul=10
    ll=1
    while computer_guess!=guess_num:
        if computer_guess>guess_num:
            ul=computer_guess-1
            print(computer_guess)
            computer_guess=random.randint(ll,ul)
        elif computer_guess<guess_num:
            ll=computer_guess+1
            print(computer_guess)
            computer_guess=random.randint(ll,ul)
    print(f"The number was {computer_guess}")
Input()