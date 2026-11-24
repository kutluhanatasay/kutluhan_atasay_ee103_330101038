data = (10, 20, (30, 40), 50, 60)
print(len(data))
print(data[2][1])
print(data[-3][1])

a = data[0]
b = data[1]
print(a, b)
a, b = b, a
print(a, b)


data = [5, 10, 15, 20, [9,7], 25]
print(len(data))
data.append(30)
print(len(data))
data.insert(2, 12)            # c. inserts 12 at index 2
data.remove([9, 7])           # d. removes nested list [9, 7]
data[0] = 100                 # e. replaces index 0 with 100
removed = data.pop()          # f. removes & stores last item (30)