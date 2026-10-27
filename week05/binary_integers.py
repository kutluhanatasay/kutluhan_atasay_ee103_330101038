X = int(input("Enter any integer number: "))
i = 1
binary = 0
while X > 0:
    digit = X % 2
    X = X//2
    binary = binary + i * digit
    i = i *10

print(binary)