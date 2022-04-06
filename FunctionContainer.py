import os

#0 is A
def func_intToAlphabet(index):
    return chr(index - 1 + ord('A'))


#row_index is start with 1
#To do : 세자리수도 되게 
def func_IndexToColumnHeading(n):
    _out = ''
    if(n > 26):
        _out = _out + func_intToAlphabet((n-1) // 26 )
    
    if(n % 26 == 0):
        _out += func_intToAlphabet(26);
    else:
        _out += func_intToAlphabet(n % 26);
    return _out

def func_getBasefileName(file_name):
    base_filename = os.path.splitext(file_name)
    base_filename = os.path.split(base_filename[0])
    base_filename = base_filename[1]
    return base_filename