from secret_data import secret_year

ub = int(2026) # this is the upper boundary
lb = int(0) # lower bound
guess = 0


for i in range(1,2026):
    guess = (ub + lb) //2
    if (secret_year < guess):
        ub = guess
    elif ( guess < secret_year):
        lb = guess
    elif (guess == secret_year):
        print(f"secret number is: {guess} found in: {i} steps")
        break



# guess and check (brute force method) 1234 guesses:
# bisection search 6 gueses => way more optimized for this given example!