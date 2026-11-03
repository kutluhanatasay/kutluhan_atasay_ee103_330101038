from secret_data import secret_number

ub = max( 0.1, secret_number) # this is the upper boundary
lb = 0.0 # lower bound
guess = 0
range = int(ub)


for i in range(1, range):

    guess = (ub + lb)/2

    if (secret_number < guess**2):
        ub = guess
    elif ( guess**2 < secret_number):
        lb = guess
    elif (guess**2 == secret_number):
        print(f"square root is: {guess} found in: {i} steps")
        break

