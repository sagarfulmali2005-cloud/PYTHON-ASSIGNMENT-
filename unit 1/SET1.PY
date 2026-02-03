# SET
numbers = {10,20,30,40,50,60}

print("set element:", numbers)

# ACCESSING ELEMENT 

print("ACCESSING ELEMENT:")
for num in numbers:
 print(num)

# creating two set(union)
set1={1,2,3,6,7,4}
set2={8,9,10,3,5,3}

# union of  set
union_set = set1.union(set2)
print("union of set:", union_set)

# creating two set(intersection)
set1={10,20,30,40}
set2={30,40,20,10}

#intersection of set
intersection_set = set1.intersection(set2)
print("intersection of set:", intersection_set)

# Difference
print("Difference (Set1 - Set2):", set1 - set2)

