import random

if hasattr(random, 'SystemRandom'):
    randrange = random.SystemRandom().randrange
    randchoice = random.SystemRandom().choice
else:
    randrange = random.randrange
    randchoice = random.choice


def generate_code(length=5):
    ALPHABET = ('a', 'b', 'c', 'd', 'e', 'f', 'h',
                'j', 'k', 'm', 'n', 'p', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z',
                '2', '3', '4', '5', '6', '7', '9')
    code = ''.join([randchoice(ALPHABET) for i in range(length)])
    return code
