import random 


def play():
    
  while True:
    play=input('press enter to play :or any key quit ')
    
    
    if play=='':
        roll(play)
    else:
        print('goobye')
        break

def roll(userinput):
    dice=random.randint(1,6)
    print('the dice number is ' + str(dice))
    return dice

play()