import random

def game():
    user = input("What's your choice?\n's'for scissor,'r'for rock and 'p'for paper\nYour choice: ")  #we take user input i.e rock,paper or scissor
    pc = random.choice(['r','p','s'])  #The computer randomly chooses from one of the chice
    winner(user,pc)

def winner(user,pc):
    if (user=='r' and pc == 's') or (user=='p' and pc =='r') or (user=='s' and pc =='p'):  #we know how a player wins in the game 
        print("You won")
    
    elif (user == pc):
        print("It's a tie")
    
    else:
        print("you lost")

        
game()  #Calling thr function game
       
