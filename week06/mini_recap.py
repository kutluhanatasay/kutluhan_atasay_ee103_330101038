
x = float(0.1)
y = float(0.2)

result = x + y
if result == 0.3 :
    print(result)
elif (0.3-1e-4 <= result <= 0.3+1e-4):
    print(f"result is close enough{result}")
else:
    print(f"result is not == to 0.3{result}")