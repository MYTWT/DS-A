
from Stack.StackList import Stack

def KiemTraNgoac(string):
    s = Stack()
    for ch in string:
        if ch in ['{','(','[']:
            s.push(ch)
        elif ch in [')',']','}']:
            if s.isEmpty():
                return False
            k = s.pop()
            if (ch == ')' and k != ')') or (ch == '[' and k != ']') or (ch == '{' and k != '}'):
                return False
    if s.isEmpty():
        return True
    else:
        return False
