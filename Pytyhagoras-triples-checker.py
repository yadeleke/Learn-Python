numbers = []
run = 'y'


def get_input():
    numbers.append(int(raw_input('Enter side a: ')))
    numbers.append(int(raw_input('Enter side b: ')))
    numbers.append(int(raw_input('Enter side c: ')))


def calculate():
    a = max(numbers)
    numbers.remove(a)

    if a ** 2 == (numbers[0] ** 2) + (numbers[1] ** 2):
        return True
    else:
        return False


def main():
    get_input()
    if calculate():
        print 'Pythagorean triple'
    else:
        print 'Not Pythagorean triple'


while(run != 'n' or run != 'N'):
    main()
    numbers = []
    run = raw_input('Continue? (y/n) ')
    print ''



