# TUPLE
my_tuple = (10,20,30,40)

print("tuple element:" , my_tuple)

# ACCESSING ELEMENT
print("first element:", my_tuple[0] )
print("second element:", my_tuple[2] )
print("last element:", my_tuple[-1] )

# Nested tuple
# creating a tuple
nested_tuple = (1,2,(3,4,5))

print("inner tuple:", nested_tuple[2])
print("Element from inner tuple:", nested_tuple[2][1])

# REPETITION OF TUPLE
# Create a tuple
t = (5, 10)

# Repeat tuple
repeated_tuple = t * 3

print("Original tuple:", t)
print("Repeated tuple:", repeated_tuple)

# Concatenation
t3 = t + (4, 5)
print("Concatenated Tuple:", t3)
