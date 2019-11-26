#4 
def is_member (member : str, list :str):
    for i in list:
        if member == i:
            return True
    return False

print(is_member("z",["z","x","y"]))
print(is_member("a",["z","x","y"]))