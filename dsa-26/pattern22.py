n= 5
for i in range(2*n-1):
    for j in range(2*n-1):
        top = i
        left = j
        bottom = (2*n-2)-i
        right = (2*n-2)-j

        layer = min(left,right,bottom,top)
        answer = n-layer
        print(answer,end=" ")
    print()
        #output:
        #1 1 1 1 1
        #1 2 2 2 1
        #1 2 3 2 1
        #1 2 2 2 1
        #1 1 1 1 1
            