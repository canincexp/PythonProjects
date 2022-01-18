import random




def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f'Guess a number between 1 and {x}'))
        print(guess)
        if guess < random_number:
            print('Sorry, guess again. Too Low.')
        elif guess> random_number:
            print('Sorry, guess again. Too High')

    print(f'Yes, you found the number {random_number}')

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback !='c' and low != high:
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        guess=random.randint(low,high)
        feedback= input(f'Is {guess} too high (H), too low (L), or correct(C) ?? \n').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1

    print(f'Yes, computer find the number {guess}, for you')


k = input('which game do you wanna play? for random guesser write (1), for computer guess write (2)... \n')
if k == '1':
    x=int(input('please enter the upper limit of the range for the guessing game: '))
    guess(x)
elif k == '2':
    x = int(input('please enter the upper limit of the range and \n hold a number in your mind. Computer will guess it.: \n'))
    computer_guess(x)

else:
    print('sorry')
