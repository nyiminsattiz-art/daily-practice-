def decode(string_):
    string = False
    if isinstance(string_, str):
        string = True
    
    result = ""
    if string == True:
        for i in string_: 
            lower = "abcdefghijklmnopqrstuvwxyz"
            upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   
            if i.isalpha() and i.isupper():
                index = upper.find(i)
                result += upper[25 - index]
            elif i.isalpha() and i.islower():
                index = lower.find(i)
                result += lower[25 - index]
            else:
                result += i
        return result
    return "Input is not a string"
