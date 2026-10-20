a = int(0)
b = int(0)
c = int(0)

for a in range(1,1001):
            b = a - 20
            c = a * 2
            if a + b + c == 1000:
                print(a)
                break

print(a, b, c)
# A = 255