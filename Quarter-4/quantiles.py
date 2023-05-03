import time
import sys

def get_given():
    given = []

    print('Enter "go" when the given is finished')
    user_input = input("> ")

    while True:
        if user_input.lower() != 'go':
            given.append(int(user_input))
            given = sorted(given)
        else:
            return given

        print(', '.join(map(lambda x: str(x), given)))
        print('Enter "go" when the given is finished')
        user_input = input("> ")

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

    print(f'\n{letter}{k} class = k(n + 1) / {denominator}')
    print(f'{letter}{k} class = {k}({len(given)} + 1) / {denominator}')
    print(f'{letter}{k} class = {k}({len(given) + 1}) / {denominator}')
    print(f'{letter}{k} class = {k * (len(given) + 1)} / {denominator}')
    print(f'{letter}{k} class = {class_}th')

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
        choice = input('[A] Quantile \n[B] Decile \n[C] Percentile \n[D] Exit \n> ').lower()

        if choice == 'a':
            k = int(input('Input variable "k": '))

            solve(k, 4, given)
            time.sleep(5)
        elif choice == 'b':
            k = int(input('Input variable "k": '))

            solve(k, 10, given)
            time.sleep(5)
        elif choice == 'c':
            k = int(input('Input variable "k": '))

            solve(k, 100, given)
            time.sleep(5)
        elif choice == 'd':
            print('\nWag ka magpapahuli')
            time.sleep(3)
            sys.exit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nWag ka magpapahuli')
        time.sleep(3)