lb = int(input("Enter an integer lower bound: "))
ub = int(input("Enter an integer upper bound: "))

reusult_for = 1
for i in range(lb, ub + 1):
    reusult_for = reusult_for * i

reusult_while = 1
curr = lb
while ub >= curr:
    reusult_while = reusult_while * curr
    curr = curr + 1

print(f"For loop result: {reusult_for}")
print(f"While loop result: {reusult_while}")

if reusult_for == reusult_while:
    print("results are same")
else:
    print("results are not same")
