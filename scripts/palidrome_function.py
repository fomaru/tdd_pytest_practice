

def palidrome_function(arg1: str):
    if type(arg1) != str:
        raise ValueError('Not string value')
    if len(arg1) == 0:
        raise ValueError('Empty string')
    if len(arg1) != 1 and arg1[0] == arg1[-1]:
        return palidrome_function(arg1[1:-1])
    elif len(arg1) <= 1:
        return True
    return False
