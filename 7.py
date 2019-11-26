#7
def program(list : [str]):
    A: [int] = []
    for i in list: 
        A.append(len(i))
    return A

print(program(["Nicho","Arthur"]))