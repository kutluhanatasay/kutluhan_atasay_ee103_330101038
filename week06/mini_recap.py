year = int(input("What year is this?"))
T = int(0)

while year > 0:
    x = year % 10
    T = T + x
    year = (year - x)/10

print(T)