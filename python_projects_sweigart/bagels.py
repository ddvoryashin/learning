import random

MAX_ITER = 10
NUM_DIGITS = 3
DIGITS = '0123456789'

# TODO: add bad input handling (less/more digits, alphabetical symbols)

def main():
    
    # info
    print(f'''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:

When I say:     That means:
Pico            One digit is correct but in the wrong position.
Fermi           One digit is correct and in the right position.
Bagels          No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Pico Fermi.
This version of game supports repeating digits.''')
    while True:
        # randomly get hidden number that user will need to guess
        hidden = ''
        for n in range(NUM_DIGITS):
            random_index = random.randint(0, 9)
            hidden = hidden + DIGITS[random_index]

        # main cycle
        for i in range(MAX_ITER):
            while True:
                guess = str(input('Make a guess: '))
                if len(guess) == NUM_DIGITS:
                    break
                elif len(guess) < NUM_DIGITS:
                    print('Too short number. Try again')
                elif len(guess) > NUM_DIGITS:
                    print('Too long number. Try again')
            
            print('guess type:', type(guess))
            
            msg, flag_win = compare(hidden, guess)
            if i == (MAX_ITER - 1) and flag_win == 0:
                msg = f'You lost! Hidden number is {hidden}'
            
            print(msg)
            if flag_win == 1:
                break
                
        flag_repeat = ''
        while flag_repeat.lower() not in ['y', 'n']:
            flag_repeat = str(input('Do you want to repeat? (y/n): '))
            
        if flag_repeat.lower() == 'n':
            break
        
        

def compare(hidden_, guess_):
    if guess_ == hidden_:
        return 'You got it!', 1
    
    d = {}
    # Find all 'Fermi' and put theirs indeces to d
    for i in range(len(guess_)):
        for j in range(len(hidden_)):
            if hidden_[j] == guess_[i] and j == i:
                d[j] = 'Fermi'
    
    # Find all 'Pico', but don't check indeces of 'Fermi' in both hidden_ and guess_
    for i in range(len(guess_)):
        if d.get(i, 'Empty') == 'Empty': # find g in d
            for j in range(len(hidden_)):
                if d.get(j, 'Empty') == 'Empty': # find index of h in d
                    if hidden_[j] == guess_[i] and j != i:
                        d[i] = 'Pico'
    
    # Combine dict into msg in ascending order by key
    list_values = dict(sorted(d.items())).values()
    if len(list_values) == 0:
        return 'Bagel', 0
    else:
        return ' '.join(list_values), 0
        
        
        
if __name__ == '__main__':
    main()