from random import randint
random_number = randint(1, 100)
print('The random number is: {}'.format(random_number))
last_guess = 0
tries = 0
threshold = 10
end = False
while not end:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS")
        continue
    tries += 1
    if guess == random_number:
        end = True
        continue
    if tries == 1:
        if guess <= (random_number + threshold) and guess >= (random_number - threshold):
            print("WARM!")
        else:
            print("COLD!")
        last_guess = guess
        continue
    guess_closeness = abs(random_number - guess)
    last_guess_closeness = abs(random_number - last_guess)
    if guess_closeness < last_guess_closeness:
        print("WARMER!")
    else:
        print("COLDER")
    last_guess = guess
else:
    print('You guessed my number {} in {} tries!'.format(random_number, tries))