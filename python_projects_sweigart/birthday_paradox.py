import random

# Структура кода:
# Генерация n дней рождения, где n вводится пользователем
# Вывод всех дней рождения и сколько совпало из n
# Спрашиваем, будем ли делать m итераций
# Если нет - выходим, если да - генерируем n дней рождения GENERATE_COUNT раз, логируя каждые 10,000
# Выводим результаты: в скольки итерациях хотя бы два дня рождения совпали и % от GENERATE_COUNT
# Спрашиваем, будем ли ещё раз играть

GENERATE_COUNT = 100000

def main():
    print('Birthday Paradox, by Dmitrii Dvoriashin ddvoryashin96@gmail.com')

    n = 0
    while True:
        n = input('Enter amount of birthdays: ')
        try:
            n = int(n)
            if n > 0:
                break
            else:
                print('Enter any number bigger than 0')
        except ValueError:
            print('Enter any positive integer number')
        
    msg = generate_birthdays(n)
    print(msg)
    
def generate_birthdays(n):
    dict_mth = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'June': 30, 
                'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
    
    msg = ''
    for b in range(n):
        rand_mth = random.randint(0, 11)
        print(dict_mth.keys())
        mth = dict_mth.keys[rand_mth]
        
        day = random.randint(1, dict_mth[mth])
        
        msg = msg + f'{mth} {day}'
        
    return msg
        
if __name__ == '__main__':
    main()
