import random
# Dictionary for statistics
user : dict = {'in_game': False,
              'secret_number': None,
              'attempts': None,
              'total_games': 0,
              'wins': 0}

def get_random_number() -> int:
    """give random numbers from 1 to 100"""
    return random.randint(1, 100)