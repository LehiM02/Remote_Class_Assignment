import random

def main():
    print("Greetings user. I will attempt" \
    " to guess your age.")
    name = input('Please enter your name:')
    print("let's begin....")
    while True:
        guess = str(random.randrange(15, 30))
        response = input('Are you ' + guess + ' years old? ')
        if response == 'y':
            print(name + ' is ' + guess + ' years old.')
            break
        else:
            print('rats')

main()