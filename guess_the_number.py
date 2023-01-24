import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    """ Set the high and low values for the random number """
    return 1, 10 # Return range between 1-10


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high) 


def get_guess():
    """ get user's guess, as an integer number """
    while True: # Loop over code until user guesses a numeric value
        try:
            return int(input('Guess the secret number? ')) 
        except:
            print('Input must be a number.')


def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high

def counter(count):
    count += 1 # Count the number of guesses each time 
    return count

def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)
    count = 0

    while True: # Loop until user correctly guesses number
        guess = get_guess()
        result = check_guess(guess, secret)
        count = counter(count)
        print(result)

        if result == correct:
            break
    if count == 1: 
        print('You got it first try!') # Alert user if they guessed in one try
    else:
        print(f'Correct. You got it after {count} guesses.') # Tell user how many guesses they took
    print('Thanks for playing the game!')


if __name__ == '__main__':
    main()
