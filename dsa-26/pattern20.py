n= 5
for i in range(n):
    letter =65
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print(chr(letter), end="")
        if j<i:
            letter += 1      # Next letter
        else:
            letter -= 1  
    print()    

  #output:
  #    A
  #   ABA
  #  ABCBA
  # ABCDCBA
  #ABCEDCBA
  