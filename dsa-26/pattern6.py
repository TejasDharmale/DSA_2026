n = 5
for row in range(n):
    for col in range(0, row+1):
        print("*", end=" ")
    print()
for row in range(n):
    for col in range(n-row-1):
        print("*", end=" ")
    print()
