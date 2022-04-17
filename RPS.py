
dictionary = {
                1: 'Rock',
                2: 'Scissors',
                3: 'Paper'
} 
y = random.choice(list(dictionary))
print(dictionary)

x = input('Select your value:')
if x not in dictionary:
    x = input('Select a valid value:')

if y == x: 
    print('Tie')

if y == 1 and x == 2:
    print('You Lose') 

if y == 1 and x == 3:
    print('You Win!')

if y == 2 and x == 1:
    print('You Win!')

if y == 2 and x == 3:
    print('You Lose')

if y == 3 and x == 1:
    print('You Lose')

if y == 3 and x == 2:
    print('You Win!')