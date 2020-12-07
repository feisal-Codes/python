import random

count = 5


def main():
    playy()


def playy():
    global count
    print('Welcome to Guess The NUmber')
    while count > 0:
        print('you have '+str(count) + ' lives ')
        play = input("Enter A number between 1 and 20:or q to quit\n: ")

        if play == 'q':
            break
        w = game(int(play))
        if w == True:
            break
        if (count == 1) & (w != True):
            print('you ran out of lifes')
            pa = input('enter p if u want play again: ')
            if pa == 'p':
                count = 5
                playy()
                break
            else:
                break
        count -= 1


def game(play):
    r_number = random.randint(1, 20)
    guess = play
    win = compare(guess, r_number)
    return win


def compare(guess, r_number):
    if guess == r_number:
        print('You won ,the number is '+str(guess))
        return True
    elif guess > r_number:
        print('you lose ,the guess number  is greater ')
    elif guess < r_number:
        print('you lose ,the guess number  is smaller ')


main()
