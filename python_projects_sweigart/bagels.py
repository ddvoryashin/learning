import random

MAX_ITER = 10
NUM_DIGITS = 3
DIGITS = '0123456789'

def main():
    
    # info
    print(f'''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a{NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:

When I say:     That means:
Pico            One digit is correct but in the wrong position.
Fermi           One digit is correct and in the right position.
Bagels          No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.
This version of game supports repeating digits.''')
    
    # randomly get hidden number that user will need to guess
    hidden = ''
    for n in range(NUM_DIGITS):
        random_index = random.randint(0, 9)
        hidden = hidden + DIGITS[random_index]

    # main cycle
    for i in range(MAX_ITER):
        guess = str(input('Make a guess: '))
        print('guess type:', type(guess))
        
        msg = compare(hidden, guess)
        print(msg)
        
        if msg == 'You got it!':
            quit()
        



def compare(hidden_, guess_):
    if guess_ == hidden_:
        return 'You got it!'
    else:
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
            return 'Bagel'
        else:
            return ' '.join(list_values)
        
        
        
if __name__ == '__main__':
    main()