from StackList import Stack

string =  input("Nhap bieu thuc can tinh toan ")

def tokenizer(string):
    Tokens=[]
    number=''
    for ch in string:
        if ch.isdigit() or ch == '.':
            number += ch
        else:
            if number:
                Tokens.append(number)
                number = ''
            if ch in '^+-*/()':
                Tokens.append(ch)
    if number:
        Tokens.append(number)
    return Tokens

def ToanTu(items):
    if items == '+' or items == '-':
        return 1
    if items == '*' or items == '/':
        return 2
    if items == '^':
        return 3
    return 0

def InfixToPostfix(Tokens):
    s = Stack()
    postfix=''
    for i,ch in enumerate(Tokens):
        if ch == '(':
            s.push(ch)
        elif ch.replace('.','',1).lstrip('-').isdigit():
            postfix += ch
            postfix += " "
        elif ch == ')':
            while (not s.isEmpty()) and s.top() != '(':
                postfix += s.top()
                postfix +=  " "
                s.pop()
            s.pop()
        else:
            if ch == '-' and (i == 0  or Tokens[i-1] in '^+-*/()'):
                postfix += '0' + ' '
            while(not s.isEmpty()) and (ToanTu(s.top()) > ToanTu(ch) or (ToanTu(s.top()) == ToanTu(ch) and ch != '^')):
                postfix += s.top()
                postfix += " "
                s.pop()
            s.push(ch)
    while not s.isEmpty():
        postfix += s.top()
        postfix += " "
        s.pop()
    return postfix
def tinhToan(postfix):
    s = Stack()
    for ch in postfix.split():
        if ch.replace('.','',1).lstrip('-').isdigit():
            s.push(float(ch))
        else:
            a = s.pop()
            b = s.pop()
            res = 0
            if ch == '+':
                res = a+b
            elif ch == '-':
                res = b-a
            elif ch == '*':
                res = a*b
            elif ch == '/':
                res = b/a
            else:
                res = b**a
            s.push(res)
    if s.size() != 1:
        print("Bieu thuc nay khong hop le")
    else:
        print(s.top())
Tokens=tokenizer(string)
postfix = InfixToPostfix(Tokens)
print(postfix)
tinhToan(postfix)