sum = int(0)
start = int(input("enter an integer lowerbound"))
stop = int(input("enter and integer upperbound"))

stop = stop + 1
for i in range (start, stop):
    sum = sum + i
    print(sum)

print(sum)