from secret_data import secret_number

ub = max(0.1, secret_number) # this is the upper boundary
lb = 0.0 # lower bound
guess = (ub + lb) / 2
epsilon = 0.01

num_guesses = 0

while abs(guess**2 - secret_number) >= epsilon:
    num_guesses += 1
    if guess**2 > secret_number:
        ub = guess
    else:
        lb = guess
    guess = (ub + lb) / 2

print(f"square root is: {guess} found in: {num_guesses} steps")
