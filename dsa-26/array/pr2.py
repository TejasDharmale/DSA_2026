nums = [8,2,9,0,4]

result = sorted(set(nums))
for i in result:
    if len(set(nums)) == 1:
        print("-1")
        break
    else:
        ans = result[-2]
    
print(ans)


#optimal solution
nums = [8, 8, 8, 8, 8]
result = sorted(set(nums))
if len(result) == 1:
    print(-1)
else:
    print(result[-2])  # second largest
