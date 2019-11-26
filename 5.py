#5 

def overlapping (list1: [str], list2: [str]):
    for a in list1: 
        for b in list2: 
            if a == b: 
                return True
    return False
print(overlapping(["a","b","c"],["a","b","c"]))
print(overlapping(["a","b","c"],["d","e","f"]))