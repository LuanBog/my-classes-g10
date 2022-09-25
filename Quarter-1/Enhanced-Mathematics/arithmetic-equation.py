import time

def get_pattern_information(pattern):
    first_term = pattern[0]
    last_term = pattern[-1]
    last_term_n = len(pattern)
    common_difference = pattern[1] - pattern[0]

    print('\nPattern Information ({})'.format(', '.join(map(lambda x: str(x), pattern))))
    print(f'\na1 (first term): {first_term}')
    print(f'a{last_term_n} (last term): {last_term}')
    print(f'n (number of terms): {last_term_n}')
    print(f'd (common difference): {common_difference}')

def get_nth_term(pattern, n):
    first_term = pattern[0]
    common_difference = pattern[1] - pattern[0]

    return first_term + ((n - 1) * common_difference)

def get_arithmetic_means(pattern, n):
    common_difference = pattern[1] - pattern[0]
    new_pattern = []

    starting_value = pattern[0]

    for i in range(n):
        new_pattern.append(starting_value)
        starting_value += common_difference

    return ', '.join(map(lambda x: str(x), new_pattern))

def get_arithmetic_series(pattern, n):
    first_term = pattern[0]
    common_difference = pattern[1] - pattern[0]

    return int((n/2) * ((2*first_term) + ((n-1) * common_difference)))

def is_arithmetic_equation(pattern):
    common_difference = pattern[1] - pattern[0]

    for index, value in enumerate(pattern):
        if index == len(pattern) - 1:
            return True

        if value + common_difference != pattern[index + 1]:
            return False

def decode_input(pattern_input):
    return list(map(lambda x: int(x.strip()), pattern_input.split(',')))

if __name__ == '__main__':
    print('\nPattern Examples:')
    print('  - 2, 4, 6, 8')
    print('  - 5, 7, 9, 11, 13')
    print('  - 6, 10, 14, 18')
    pattern = decode_input(input('\nEnter your pattern: '))

    if not is_arithmetic_equation(pattern):
        print('\nPattern is not an Arithmetic Equation')

    while True:
        choice = input('\nOptions: \na) Get pattern information \nb) Find nth term \nc) Arithmetic means \nd) Arithmetic series \ne) Quit \n>').lower()

        if choice == 'a':
            get_pattern_information(pattern)
        elif choice == 'b':
            n = int(input('\nWhich term to find? (n): '))
            term_found = get_nth_term(pattern, n)

            print(f'a{n} = {term_found}')
        elif choice == 'c':
            n = int(input('\nTo until which term should I find? (n): '))
            result = get_arithmetic_means(pattern, n)

            print(result)
        elif choice == 'd':
            n = int(input('\nTo until which term should I sum? (n): '))
            result = get_arithmetic_series(pattern, n)

            print(result)
        else:
            break

        time.sleep(3)

# TODO: Add solution    
