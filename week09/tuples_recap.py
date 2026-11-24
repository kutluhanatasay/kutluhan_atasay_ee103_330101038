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


def analyze_numbers(L):
    squares = [x**2 for x in L]
    return (len(L), sum(L), squares )

print(analyze_numbers(data))

numbers = [3, 6, 9, 12, 15, 18]
evens = [n for n in numbers if (n%2 == 0)]
print(f"evens = {evens}")

odds_squares = [n**2 for n in numbers if (n % 2 == 1)]

print(f"odd_squares = {odds_squares}")


for idx, val in enumerate(numbers):
    print(idx, val)



L1 = [1, 2, 3]
L2 = L1        # L2 points to L1's list
L3 = L1[:]     # L3 is a separate copy of [1, 2, 3]
L2[0] = 100    # mutates shared list -> L1 is now [100, 2, 3], L2 is [100, 2, 3]
L3[1] = 200    # mutates only L3 -> L3 is [1, 200, 3], L1 stays [100, 2, 3]

