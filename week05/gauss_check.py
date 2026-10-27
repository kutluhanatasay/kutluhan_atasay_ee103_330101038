
for D in range(1,28):
    E = D + 3
    F = D *3
    if (E + D + F) == 28 :
        print(D, E, F)


for D in range(1,28):
    for E in range(1,28):
        for F in range(1,28):
            if (E == D + 3) and (F == 3 * D) and (D + E + F == 28):
                print(D, E, F)
                print(f"David: {D}")
                print(f"Emma: {E}")
                print(f"Frank: {F}")                
