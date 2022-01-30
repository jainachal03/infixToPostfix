order = {'-':0, '+':1, '*':2, '/':3, '^':4, '(':0}

def convert(equation):
    equation = equation.lstrip().rstrip().replace(" ", "")
    def isOperator(char):
        if char == "-" or char == "+" or char =="/" or char == '*' or char == '^':
            return True
        return False

    output = []
    buffer = []
    operators = []
    for char in equation:
        if isOperator(char):
            while len(output)>0 and order[output[-1]] > order[char]:
                buffer.append(output[-1])
                output.pop()
            output.append(char)
        elif char == '(':
            output.append('(')
        elif char == ')':
            while output[-1] != '(':
                buffer.append(output[-1])
                output.pop()
            output.pop()
        else:
            buffer.append(char)
    
    while len(output)>0:
        buffer.append(output[-1])
        output.pop()
    return ' '.join(buffer)


def evaluate(stack):
    ans = 0 
    stack = [char for char in stack if char != ' ']
    while len(stack)>1:
        a, b = list(map(int, [stack[0], stack[1]])) 
        stack.pop(0)
        stack.pop(0)
        c = stack[0]
        stack.pop(0)
        if c == '+':
            stack.insert(0, a + b)
        elif c == '-':
            stack.insert(0, a - b)
        elif c == '*':
            stack.insert(0, a * b)
        elif c == '/':
            stack.insert(0, a/b)
        else:
            stack.insert(0, a**b)
    return stack[0]