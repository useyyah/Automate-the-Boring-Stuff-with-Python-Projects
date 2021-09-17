import random
import logging

logging.disable(logging.CRITICAL) # Disable if you debug the program.

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Start of program")
guess = ''
while guess not in ('heads', 'tails'):
    logging.debug("Start of guess")
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()

logging.debug("Start of coin toss")
toss = random.randint(0, 1) # 0 is tails, 1 is heads

# Start of the debugging code.
if toss == 0:
    toss = 'tails'
if guess == 1:
    guess = 'heads'
# End of the debugging code.

logging.debug(f"Is {guess}(guessed) equal to {toss}(tossed)?")
if toss == guess:
    print("You got it!")
else:
    print("Nope! Guess again!")
    guess = input()
    if toss == guess:
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")