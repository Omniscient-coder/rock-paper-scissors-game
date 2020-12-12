import random

def game():
    user = input("What's your choice?\n's'for scissor,'r'for rock and 'p'for paper\nYour choice: ")
    pc = random.choice(['r','p','s'])
    winner(user,pc)

def winner(user,pc):
    if (user=='r' and pc == 's') or (user=='p' and pc =='r') or (user=='s' and pc =='p'):
        print("You won")
    
    elif (user == pc):
        print("It's a tie")
    
    else:
        print("you lost")

