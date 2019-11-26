#2

def Vowelscheck(C):
    vowels = ['a','i','u','e','o',' ']
    return C.lower() in vowels 
def translate(X):
    newText : str = ""
    for i in X: 
            if(Vowelscheck(i)):
                newText += i
            else: 
                newText += i+"o"+i
    return newText


print(translate("I am Bently"))