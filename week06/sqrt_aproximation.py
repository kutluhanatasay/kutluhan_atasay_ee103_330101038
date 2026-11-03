from secret_data import secret_number
i = int(0)
guess = 0
step = 0.01
epsion= 0.01

while True:
    i = i + 1
    if ( abs(secret_number - guess**2) < epsion):
        print(f"square root of the secret number is {guess} found in {i} steps.")
        break
    else:
        guess = guess + step
