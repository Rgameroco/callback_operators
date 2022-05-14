OPS = {
    "+": (lambda x,y: y+x), 
    "-": (lambda x,y: y-x),
    "*": (lambda x,y: y*x),
    "/": (lambda x,y: -1 if x==0 else int(y/x))
}

def zero(operator=None,cb=None) -> int:
    return validateOperation(operator,cb,0)

def one(operator=None,cb=None) -> int:
    return validateOperation(operator,cb,1)

def two(operator=None,cb=None) -> int:
    return validateOperation(operator,cb,2)

def three(operator=None,cb=None) -> int:
    return validateOperation(operator,cb,3)

def four(operator=None,cb=None) -> int:
    return validateOperation(operator,cb,4)

def five(operator=None,cb=None) -> int:
    return validateOperation(operator,cb,5)

def six(operator=None,cb=None) -> int:
    return validateOperation(operator,cb,6)

def seven(operator=None,cb=None) -> int:
    return validateOperation(operator,cb,7)

def eight(operator=None,cb=None) -> int:
    return validateOperation(operator,cb,8)

def nine(operator=None,cb=None) -> int:
    return validateOperation(operator,cb,9) 

def plus(number=0) -> list:
    operator= '+'
    return [operator,number]
    
def minus(number=0) -> list:
    operator= '-'
    return [operator,number]
    
def times(number=1) -> list:
    operator= '*'
    return [operator,number]
    
def divided_by(number=1) -> list:
    operator= '/'
    return [operator,number]

def result(listOperation,number2) -> int:
    return OPS[listOperation[0]](listOperation[1],number2) 

def validateOperation(listOperation,callback, numberCallback) -> int:
    return numberCallback if listOperation == None else result(listOperation,numberCallback)
