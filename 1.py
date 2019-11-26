#1 
A = "3, 5, 7, 23"
A = A.replace(","," ")
newA = A.split()

print("List:" + str(newA))
print("Tuple:" + str(tuple((newA))))


