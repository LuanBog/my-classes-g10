import time
import sys

def get_given():
    print('\nSeparate with commas!')
    print('E.G: 42, 23, 21, 15, 3, 6, 12, 21 (This will automatically get sorted)')
    user_input = input("> ")

    separated = user_input.split(',')
    numbered = list(map(lambda x: int(x.strip()) , separated))

    return sorted(numbered)

def ordinalize(number):    
    if number == 11 or number == 12 or number == 13:
        return str(number ) + 'th'

    last_number = str(number)[-1]

    if last_number == '1':
        return str(number) + 'st'
    elif last_number == '2':
        return str(number) + 'nd'
    elif last_number == '3':
        return str(number) + 'rd'
    else:
        return str(number) + 'th'

def separate_decimals(float_val):
    splitted = str(float_val).split('.')

    if len(splitted) == 2:
        # There is a decimal
        return (int(splitted[0]), int(splitted[1]))
    else:
        # There is no decimal
        return (int(splitted[0]), 0)

def custom_round(number):
    whole, dec = separate_decimals(number)
    first_dec = int(str(dec)[0])

    if first_dec >= 5:
        return whole + 1
    else:
        return whole

def linear_interpolation(k, denominator, given):
    first_answer = (k * (len(given) + 1)) / denominator
    final_answer = 0
    whole, dec = separate_decimals(first_answer)

    dec = float('0.' + str(dec))

    letter = None
    if denominator == 4:
        letter = 'Q'
    elif denominator == 10:
        letter = 'D'
    else:
        letter = 'P'

    print('-'*50)
    print('LINEAR INTERPOLATION METHOD')

    print(f'\n{letter}{k} = k(n + 1) / {denominator}')
    print(f'{letter}{k} = {k}({len(given)} + 1) / {denominator}')
    print(f'{letter}{k} = {k}({len(given) + 1}) / {denominator}')
    print(f'{letter}{k} = {k * (len(given) + 1)} / {denominator}')
    print(f'{letter}{k} = {ordinalize(first_answer)}')

    if dec != 0.0:
        first_num = given[int(whole) - 1]
        second_num = given[int(whole)]

        final_answer = first_num + (dec * (second_num - first_num)) 

        print(f'\n{letter}{k} = {ordinalize(int(whole))} + {dec}({ordinalize(int(whole + 1))} - {ordinalize(int(whole))})')
        print(f'{letter}{k} = {first_num} + {dec}({second_num} - {first_num})')
        print(f'{letter}{k} = {first_num} + {dec}({second_num - first_num})')
        print(f'{letter}{k} = {first_num} + {dec * (second_num - first_num)}')
        print(f'{letter}{k} = {final_answer}')
    else:
        final_answer = given[int(whole) - 1]

        print(f'\nSince "Q{k} class" ({first_answer}) is a whole number. We can just get the position and we have our final answer')
        print(f'Q{k} = {final_answer}')    

def general_method(k, denominator, given):
    letter = None
    if denominator == 4:
        letter = 'Q'
    elif denominator == 10:
        letter = 'D'
    else:
        letter = 'P'

    print('-'*50)
    print('GENERAL METHOD')

    first_answer = (k * len(given)) / denominator

    print(f'\n{letter}{k} = kn / {denominator}')
    print(f'{letter}{k} = ({k})({len(given)}) / {denominator}')
    print(f'{letter}{k} = {k * len(given)} / {denominator}')
    print(f'{letter}{k} = {ordinalize(first_answer)}')

    whole, dec = separate_decimals(first_answer)

    if dec != 0:
        rounded = custom_round(first_answer)

        print(f'{letter}{k} = {ordinalize(rounded)}')
        print(f'{letter}{k} = {given[rounded - 1]}')
    else:
        final_answer = (given[int(whole) - 1] + given[int(whole)]) / 2

        print(f'\n{letter}{k} = ({ordinalize(int(whole))} + {ordinalize(int(whole+1))}) / 2')
        print(f'{letter}{k} = ({given[int(whole) - 1]} + {given[int(whole)]}) / 2')
        print(f'{letter}{k} = {given[int(whole) - 1] + given[int(whole)]} / 2')
        print(f'{letter}{k} = {final_answer}')
        
        i, final_answer_dec = separate_decimals(final_answer)

        if final_answer_dec != 0:
            print(f'{letter}{k} = {custom_round(final_answer)}')

def mendenhall_sincich_method(k, denominator, given):
    first_answer = (k * (len(given) + 1)) / denominator
    whole, dec = separate_decimals(first_answer)

    letter = None
    round_up_down_median = ''
    if denominator == 4:
        letter = 'Q'
        
        if k == 2:
            round_up_down_median = 'median'
        elif k < 2:
            round_up_down_median = 'up'
        else:
            round_up_down_median = 'down'
    elif denominator == 10:
        letter = 'D'

        if k == 5:
            round_up_down_median = 'median'
        elif k < 5:
            round_up_down_median = 'up'
        else:
            round_up_down_median = 'down'
    else:
        letter = 'P'

        if k == 50:
            round_up_down_median = 'median'
        elif k < 50:
            round_up_down_median = 'up'
        else:
            round_up_down_median = 'down'

    print('-'*50)
    print('MENDELHALL AND SINCICH METHOD')

    print(f'\n{letter}{k} = k(n + 1) / {denominator}')
    print(f'{letter}{k} = {k}({len(given)} + 1) / {denominator}')
    print(f'{letter}{k} = {k}({len(given) + 1}) / {denominator}')
    print(f'{letter}{k} = {k * (len(given) + 1)} / {denominator}')
    print(f'{letter}{k} = {ordinalize(first_answer)}')

    if dec == 0:
        print(f'{letter}{k} = {given[int(whole) - 1]}')
        return

    if round_up_down_median == 'median':
        final_answer = (given[int(whole) - 1] + given[int(whole)]) / 2

        print(f'\n{letter}{k} = ({ordinalize(int(whole))} + {ordinalize(int(whole+1))}) / 2')
        print(f'{letter}{k} = ({given[int(whole) - 1]} + {given[int(whole)]}) / 2')
        print(f'{letter}{k} = {given[int(whole) - 1] + given[int(whole)]} / 2')
        print(f'{letter}{k} = {final_answer}')

        i, final_answer_dec = separate_decimals(final_answer)

        if final_answer_dec != 0:
            print(f'{letter}{k} = {custom_round(final_answer)}')

    elif round_up_down_median == 'up':
        next_number = int(whole) + 1

        print(f'{letter}{k} = {ordinalize(next_number)}')
        print(f'{letter}{k} = {given[next_number - 1]}')
    else:
        print(f'{letter}{k} = {ordinalize(int(whole))}')
        print(f'{letter}{k} = {given[int(whole) - 1]}')

def solve(k, denominator, given):   
    print('\nSelect method:')
    method_chosen = input('[a] General Method \n[b] Mendenhall and Sinchich Method \n[c] Linear Interpolation Method\n[d] All \n> ').lower()

    if method_chosen == 'a':
        general_method(k, denominator, given)
    elif method_chosen == 'b':
        mendenhall_sincich_method(k, denominator, given)
    elif method_chosen == 'd':
        general_method(k, denominator, given)
        mendenhall_sincich_method(k, denominator, given)
        linear_interpolation(k, denominator, given)
    else:
        linear_interpolation(k, denominator, given)

    print('-'*50)

def main():
    given = get_given()

    while True:
        print('\nYour given: ' + ', '.join(map(lambda x: str(x), given)))
        choice = input('[Q]uantile \n[D]ecile \n[P]ercentile \n[E]xit \n> ').lower()

        if choice == 'q':
            k = int(input('Input Qx = '))

            solve(k, 4, given)
            time.sleep(5)
        elif choice == 'd':
            k = int(input('Input Dx = '))

            solve(k, 10, given)
            time.sleep(5)
        elif choice == 'p':
            k = int(input('Input Px = '))

            solve(k, 100, given)
            time.sleep(5)
        elif choice == 'e':
            print('\nWag ka magpapahuli')
            time.sleep(3)
            sys.exit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nWag ka magpapahuli')
        time.sleep(3)
