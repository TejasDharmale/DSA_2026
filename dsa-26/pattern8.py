for i in range(1, 6):
    for j in range(1, 10):
        if j >= i and j <= 8-i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
