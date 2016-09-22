'''
Created on May 4, 2015

@author: Shiv Sharma
'''
from ds.Stack import Stack

def baseConverter(decNumber, base):
    '''
    Method to convert decimal to any base
    '''
    digits = "0123456789ABCDEF"
    
    remStack = Stack()
    
    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base
    
    baseString = ""
    while not remStack.isEmpty():
        baseString = baseString + digits[remStack.pop()]
    return baseString

print(baseConverter(28, 16))

def parChecker(symbolString):
    '''
    General Balanced Symbol Problem
    '''
    s = Stack()
    index = 0
    balanced = True
    
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        
        if symbol in "[{(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
        
    if balanced and s.isEmpty():
        return True
    else:
        return False
    
def matches(openSymbol, closeSymbol):
    opens = "[{("
    closers = "]})"
    
    return opens.index(openSymbol) == closers.index(closeSymbol)

print(parChecker('{{([][])}()}'))
print(parChecker('[{()}'))
    
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    opstack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYYZ" or token in "123457890":
            postfixList.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            topToken = opstack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opstack.pop()
        else:
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
                postfixList.append(opstack.pop())
            opstack.push(token)
    
    while not opstack.isEmpty():
        postfixList.append(opstack.pop())
    return " ".join(postfixList)
    
    
print (infixToPostfix("A * B + C * D"))
print (infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
    
print (postfixEval('7 8 + 3 2 + /'))

def infixToPrefix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    infixexpr = infixexpr[::-1];
    
    opStack = Stack()
    prefixList = []
    tokenList = infixexpr.split()
    
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            prefixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                prefixList.append(token)
                topToken = opStack.pop()
    
    
                
            
    
    
    
    
    
    
    
    