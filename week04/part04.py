a = int(0)
b = int(0)
c = int(0)

for a in range(1,11):
    for b in range(1, 11):
        for c in range(1,11):
            if a == b + 2 :
                if c == 2 * a:       
                    if a + b + c == 10:
                        print(a)
                        break


# a = 3
# b = 1
# c = 6
# a + b + c = 3 + 1 + 6  = 10