import random
from time import sleep

def main():
    print("Greetings user. I will attempt" \
    " to guess your age.")
    sleep(3)
    name = input('Please enter your name:')
    sleep(3)
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

main()