from envparse import env
import os
from run_game import lot

env.read_envfile('settings.env')
budget = int(os.getenv('MY_MONEY'))

while budget >= 0:
    will_play = input('Will you play?')
    if will_play.lower() == 'yes':
        x = int(input('Guess the number from 0 to 30:'))
        rate = int(input(f'You have{budget}in your budget , your rate:'))
        budget = lot(x, rate, budget)
    else:
        print(f'Results: {budget}')
        if budget >= 1000:
            print(f'You win {budget - 1000}$')
        else:
            print(f'You lose {1000 - budget}$')
        break