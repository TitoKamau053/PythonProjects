import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} congrats')


guess(100)


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low == high:
            guess = low  # could also be high b/c low = high
        else:
            guess = random.randint(low, high)
        feedback = input(f'is {guess} too high (H), too low (L), or correct(C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! the computer guessed your number,{guess}, correctly!')


computer_guess(50)
