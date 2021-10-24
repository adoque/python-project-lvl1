import prompt
import random


def check_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        number = random.randint(1, 100)
        even = number % 2 == 0
        odd = number % 2 != 0

        print('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')

        if (even and answer == 'yes') or (odd and answer == 'no'):
            print('Correct!')
            if i == 2:
                print('Congratulations, {}!'.format(name))
                break
        elif even and answer != 'yes':
            print("'{}' is wrong answer ;(. "
            "Correct answer was 'yes'.".format(answer))
            print("Let's try again, {}!".format(name))
            break
        elif odd and answer != 'no':
            print("'{}' is wrong answer ;(. "
            "Correct answer was 'no'.".format(answer))
            print("Let's try again, {}!".format(name))
            break
