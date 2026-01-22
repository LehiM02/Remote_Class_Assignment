import random
from time import sleep

def main():
    done = True
    while done:
        print("Greetings user. I will attempt" \
        " to guess your age.")
        sleep(3)
        name = input('Please enter your name:')
        sleep(1)
        print("let's begin....")
        sleep(3)
        while True:
            guess = str(random.randrange(15, 30))
            response = input('Are you ' + guess + ' years old? ')
            if response == 'y':
                print(name + ' is ' + guess + ' years old.')
                break
            else:
                print('rats')
        replay = input('Would you like to play again? ')
        if replay == 'y':
            print('Here we go again....')
            sleep(3)
        else:
            print('Goodbye ' + name)
            done = False


main()