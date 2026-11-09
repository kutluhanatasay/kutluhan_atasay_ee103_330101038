n = int(input("Enter n: "))
total = 0.0
for i in range(0, n):
    total = total + 0.1
print(f"Total: {total}")

if  total == n/10:
    print("Equal: True")
else :
    print("Equal: False")
    
if abs(total- n/10) < 1e-9:
    print("Close enough: True")
else :
    print("Close enough: False")
