cube = int(input("Enter a positive integer: "))

guess = 0

for guess in range ( 0, cube + 1):

    if guess**3 == cube:
        print(f"Cube root of {cube} is {guess}")
        break
else:
    print(f"{cube} is not a perfect cube")
    