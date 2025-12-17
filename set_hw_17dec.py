 # union --->sets returns all unique elements from all sets.  No duplicate values, Order does not matter
s1={1,2,3,4,5,6,3}
s2={2,3,6,9,11,22,44,66,}
union_set=s1.union(s2)
print("Union of s1 and s2 is:",union_set)   # {1, 2, 3, 4, 5, 6, 66, 9, 11, 22, 44}

 #intersection ---> sets returns only common elements from all sets. No duplicate values, Order does not matter
itersection_set=s1.intersection(s2)
print("Intersection of s1 and s2 is:",itersection_set)   # {2, 3} 

# Remove duplicates from list using set 
list=[1,4,6,8,2,3,11,1,4,7,6] 
unique_num=set(list)
print(unique_num)  

#count duplicate element from set 

l=[5,2,7,8,2,9,3,2,5,5] 
duplicate_num=len(l)-len(set(l))
print("The count of duplicate elements in list is:",duplicate_num)



for num in set(l):
    count=l.count(num)
    if count>1:

     print(f"{num} removed {count-1} times")
