import random

values ={'R':"Rock", 'P':"Paper", 'S': "Scissors"}
winner = False

while winner != True :
        user=input("Please select a mode: R P S: \n")
        if user not in list(values.keys()):
            print("Please ensure you selected an option from the first letters: R, P or S")
        else:
            computer=random.choice(list(values.keys()))
            print(f'Player({values[user]}) : CPU ({values[computer]})')
            if computer == user:
                continue
            elif computer == 'R' and user == 'P':
                print("User won")
                winner = True
            
            elif computer == 'P' and user == 'S':
                print('User won')
                winner = True
                
            elif computer == 'S' and user == 'R':
                print('User won')
                winner = True
            
            else:
                print('Computer won')
                winner = True

