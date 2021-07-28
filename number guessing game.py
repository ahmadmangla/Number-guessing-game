num = 20
guess = 5
print('Welcome to number guessing game, Lets start!')
print('You have ' + str(guess) + ' guesses to use during the game!')

while guess>=1:
    user_num = int(input('Please enter a number : '))
    if user_num == num:
        print('Congratulations you have won the game!')
        print('You took ' + str(guess) + ' guesses to win the game')
        break
    else:
        guess = guess-1
        print('You have ' + str(guess) + ' guess left')
        if user_num < num and user_num >= 15:
            print('The number you entered is lower and very close to the secret number, keep trying\n')
        elif user_num > num and user_num <= 25:
            print('The number you entered is higher and very close to the secret number, keep trying\n')
        elif user_num > num and user_num > 25:
            print('The number you entered is very high than the secret number, keep trying\n')
        elif user_num < num and user_num < 15:
            print('The number you entered is very low than the secret number, keep trying\n')

if guess==0:
    print('Game over!')




