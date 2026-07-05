n= 5
for i in range(n):
    for j in range(n-i):
        char = chr(65+j)
        print(char,end="")
    
    print()