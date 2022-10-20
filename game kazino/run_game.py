from random import choice

list1 = [range(1, 31)]

def lot(x, rate, budget):
    if rate > 0:
        budget -= rate
    else:
        raise 'Rate should be more than 0 dollars'
    correct_number = choice(list1)
    if x == correct_number:
        rate *= 2
        budget += rate
        print(f'You won! Your budget {budget}')
    else:
        print(f'You lost! Your budget {budget}')
    return budget