import random

score = int(0)
computer_score = int(0)

engine = int(input('1 to start RPS and 0 to stop: '))
while 1 == 1:
    if engine != 1 and engine != 0:
        engine = input('Invalid input, try again: ')
    else:

        while engine == 1:
            weapons = ['Rock','Paper','Scissors']

            x = input('Select a weapon: ')

            while 1 == 1:
                if x not in weapons:
                    x = str(input('Select a valid weapon: '))
                else:
                    break
            y = random.choice(weapons)
            print('Computer chooses ' + y)

            if y == x: 
                print('Tie')

            if y == weapons[0] and x == weapons[1]:
                print('You Win')
                score += 1 

            if y == weapons[0] and x == weapons[2]:
                print('You Lose!')
                computer_score += 1 

            if y == weapons[1] and x == weapons[0]:
                print('You Lose!')
                computer_score += 1 

            if y == weapons[1] and x == weapons[2]:
                print('You Win')
                score += 1 

            if y == weapons[2] and x == weapons[0]:
                print('You Win')
                score += 1 

            if y == weapons[2] and x == weapons[1]:
                print('You Lose!')
                computer_score += 1 

            print('Score:\nYou: ' + str(score), 'Computer: ' + str(computer_score))
            engine = int(input('To continue input 1, to stop input 0: ' ))
            print(" ")
        else:
            print('Thanks for playing!')
            break