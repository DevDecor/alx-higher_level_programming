#!/usr/bin/python3
for i in range(1, 90):
    for j in range(0, i):
        found = 0
        x = f"{i:0>2d}"
        y = f"{j:0>2d}"
        if (x[0] == y[1] and x[1] == y[0]) or x[0] == x[1]:
            found = 1
            break
    if found == 1:
        continue
    print(f"{i:0>2d}", end="")
    if i != 89:
        print(f", ", end="")
