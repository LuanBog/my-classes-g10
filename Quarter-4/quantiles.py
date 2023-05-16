import time
import sys

def get_given():
    # given = []

    # print('Enter "go" when the given is finished')
    # user_input = input("> ")

    # while True:
    #     if user_input.lower() != 'go':
    #         given.append(int(user_input))
    #         given = sorted(given)
    #     else:
    #         return given

    #     print(', '.join(map(lambda x: str(x), given)))
    #     print('Enter "go" when the given is finished')
    #     user_input = input("> ")

    print('\nSeparate with commas!')
    print('E.G: 42, 23, 21, 15, 3, 6, 12, 21 (This will automatically get sorted)')
    user_input = input("> ")

    separated = user_input.split(',')
    numbered = list(map(lambda x: int(x.strip()) , separated))

    return sorted(numbered)

def separate_decimals(float_val):
    splitted = str(float_val).split('.')

    if len(splitted) == 2:
        # There is a decimal
        return (int(splitted[0]), float(f'0.{splitted[1]}'))
    else:
        # There is no decimal
        return (int(splitted[0]), 0)

def solve(k, denominator, given):   
    class_ = (k * (len(given) + 1)) / denominator
    final_answer = 0
    whole, dec = separate_decimals(class_)

    letter = None
    if denominator == 4:
        letter = 'Q'
    elif denominator == 10:
        letter = 'D'
    else:
        letter = 'P'

    print('-'*50)

    print(f'\n{letter}{k} = k(n + 1) / {denominator}')
    print(f'{letter}{k} = {k}({len(given)} + 1) / {denominator}')
    print(f'{letter}{k} = {k}({len(given) + 1}) / {denominator}')
    print(f'{letter}{k} = {k * (len(given) + 1)} / {denominator}')
    print(f'{letter}{k} = {class_}th')

    if dec != 0.0:
        first_num = given[int(whole) - 1]
        second_num = given[int(whole)]

        final_answer = first_num + (dec * (second_num - first_num)) 

        print(f'\n{letter}{k} = {int(whole)}th + {dec}({int(whole + 1)}th - {int(whole)}th)')
        print(f'{letter}{k} = {first_num} + {dec}({second_num} - {first_num})')
        print(f'{letter}{k} = {first_num} + {dec}({second_num - first_num})')
        print(f'{letter}{k} = {first_num} + {dec * (second_num - first_num)}')
        print(f'{letter}{k} = {final_answer}')
    else:
        final_answer = given[int(whole) - 1]

        print(f'\nSince "Q{k} class" ({class_}) is a whole number. We can just get the position and we have our final answer')
        print(f'Q{k} = {final_answer}')    

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
