X = float(input("enter any number to find its binary representaion"))
i = 1
binary = "0."
while X > 0:
    X = (X * 2)
    bit = int(X)
    binary += str(bit)
    X = X - bit
print(binary)