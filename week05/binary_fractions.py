X = float(input("enter any number to find its binary representaion"))
i = 1
binary = "0."
original_x = X
epsilon = 0.0001
reconstructed_val = 0.0
power = 0.5

while X > 0:
    X = (X * 2)
    bit = int(X)
    binary += str(bit)
    X = X - bit
    if abs(float(binary) - original_x) >= epsilon:
        break

print(binary)