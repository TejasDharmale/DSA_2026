# nums = [1, 2, 2, 3, 3, 3, 4]

# size = len(nums)+1

# hash_list= [0]*size

# for i in nums:
#     hash_list[i]+=1

# res = []    
# for j in range(size):
#     if hash_list[j]>0:
#         res.append(hash_list[j])
#         highest = max(res)
# print(highest)        
    # ###########################################

######################Solution2  using hash table #####################

nums =[4, 4, 5, 5, 6]

size = len(nums)+1

hash_list= [0]*size

for i in nums:
    hash_list[i]+=1

highest = max(hash_list) 
print(highest) 