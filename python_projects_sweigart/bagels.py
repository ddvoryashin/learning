import random

MAX_ITER = 10

def main():
    # randomly get hidden number that user will need to guess
    hidden = random.randint(0, 999)
    hidden = str(hidden)
    hidden = '0' * (3 - len(hidden)) + str(hidden)
    hidden = '110'
    print(f'hidden type: {hidden}')

    for i in range(MAX_ITER):
        guess = str(input('Make a guess: '))
        print('guess type:', type(guess))
        
        msg = compare(hidden, guess)
        print(msg)



def compare(hidden_, guess_):
    if guess_ == hidden_:
        return 'You got it!'
    else:
        d = {}
        # Find all 'Fermi' and put theirs indeces to d
        for g in guess_:
            for h in hidden_:
                if h == g and hidden_.index(h) == guess_.index(g):
                    fermi_ix = guess_.index(h)
                    d[fermi_ix] = 'Fermi'
        
        # Find all 'Pico', but don't check indeces of 'Fermi' in both hidden_ and guess_
        # TODO: учесть, что .index() ищет первое совпадение в списке #
        for g in guess_:
            if d.get(guess_.index(g), 'Empty') == 'Empty': # find index of g in d
                for h in hidden_:
                    if d.get(hidden_.index(h), 'Empty') == 'Empty': # find index of h in d
                        if h == g and hidden_.index(h) != guess_.index(g):
                            pico_ix = guess_.index(h)
                            d[pico_ix] = 'Pico'
        
        # Combine dict into msg in ascending order by key
        list_values = dict(sorted(d.items())).values()
        if len(list_values) == 0:
            return 'Bagel'
        else:
            return ' '.join(list_values)
        
        
        
if __name__ == '__main__':
    main()


# обработать случай, когда в загаданном числе две одинаковых цифры
# (+) hidden = 110, guess = 210, должно вывести Fermi Fermi
# (+) hidden = 110, guess = 114, должно вывести Fermi Fermi
# (+) сделать через макс уровень: Piko - 1, Fermi - 2, выводить макс из них
# (+) hidden.index() возвращает первое совпадение
# hidden = 110, guess = 121, должно вывести Fermi Pico. Сделать через функцию