number = 50
guess = int(input('Enter a number : '))

while guess :
    if guess < number :
        print('Too low')

    elif guess > number : 
        print('Too high')

    elif guess == number :
        print('correct')
        break

    guess = int(input('Enter a number : '))

print('Out of loop')