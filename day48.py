import operator

def arithmetic(a, b, op):
    opeDict = {
        "add" : operator.add,
        "subtract" : operator.sub,
        "multiply" : operator.mul,
        "divide" : operator.truediv
        
    }
    return opeDict[op](a, b)
