# Division in Python, returns decimal value
print(10/2)
print(11/2)

# Return the remainder
print(10 % 2)
print(11 % 2)

# return the largest whole number 
# (floor division -> returns the largest whole number <= normal division result)
print(10//2)
print(11//2)

print(100//4)
print(101//4)

# be careful with negative numbers, it still rounds down but -5 > -6
print(-10//2) # still -5, no remander
print(11//-2) # -6 because -5.5 rounded down -> -6