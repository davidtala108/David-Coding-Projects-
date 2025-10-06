from stack_array import *

# You do not need to change this class
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '**': lambda x, y: x ** y,
    '/': lambda x, y: x / y,
    '<<': lambda x, y: x << y,
    '>>': lambda x, y: x >> y,
}
valid_operator = {'+','-','*','**','/','<<','>>'}
special_operator ={'(',')'}

class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str: str) -> float:
    '''Evaluates a postfix expression
    
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    stack = Stack (10)
    List_items = input_str.split(' ')
    for val in List_items:
        if any(char.isalpha() for char in val):
            raise PostfixFormatException('Invalid token')
        else:
            if val in valid_operator:
                try:
                    x = stack.pop()
                    y = stack.pop()
                    if val == '/':
                        if float(x) == 0:
                            raise PostfixFormatException('Division by zero is not allowed')
                    if val in {'<<','>>'}:
                        Value = operations[val](int(y), int(x))
                        stack.push(Value)
                    else:
                        Value = operations[val](float(y),float(x))
                        stack.push(Value)
                except:
                    raise PostfixFormatException ('Insufficient operands')
            else:
                stack.push(float(val))
    if stack.size() == 1:
        Final_sun = stack.pop()
        return Final_sun
    else:
        raise PostfixFormatException ('Too many operands')



def infix_to_postfix(input_str: str) -> str:
    '''Converts an infix expression to an equivalent postfix expression

    Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    valid_operator = ['+', '-', '*','**','/', '<<', '>>']
    special_operator = ['(', ')']
    stack = Stack(10)
    list_str = input_str.split(' ')
    low =['+', '-']
    medium = ['*','/']
    high = ['**']
    highest = ['>>','<<']
    Post_list =[]
    for val in list_str:
        if val not in valid_operator and val not in special_operator:
            Post_list.append(val)
        else:
            if stack.is_empty():
                stack.push(val)
            else:
                if val == '(':
                    stack.push(val)
                elif val ==')':
                    y = 1
                    while y == 1:
                        x = stack.pop()
                        if x != '(':
                            Post_list.append(x)
                        else:
                            y = 2
                else:
                    y = 1
                    o1 = val
                    while y == 1:
                        if stack.is_empty():
                            stack.push(o1)
                            break
                        o2 = stack.pop()
                        if o2 == '(':
                            stack.push(o2)
                            stack.push(o1)
                            break
                        elif o2 in highest:
                            Post_list.append(o2)
                        elif o2 in high and o1 not in highest:
                            if o1 in high:
                                stack.push(o2)
                                stack.push(o1)
                                break
                            else:
                                Post_list.append(o2)
                        elif o2 in medium and o1 not in high and o1 not in highest:
                            Post_list.append(o2)
                        elif o1 in low:
                            Post_list.append(o2)
                        else:
                            stack.push(o2)
                            stack.push(o1)
                            break


    while stack.is_empty() == False:
        x = stack.pop()
        Post_list.append(x)
    RPN = ' '.join(Post_list)
    return RPN


def prefix_to_postfix(input_str: str) -> str:
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << or numbers
    Returns a String containing a postfix expression (tokens are space separated)'''
    stack = Stack(10)
    list_str = input_str.split(' ')
    rev_list_str= list_str[::-1]

    for val in rev_list_str:
        if val not in valid_operator and val not in special_operator:
            stack.push(val)
        else:
            o1 = stack.pop()
            o2 = stack.pop()
            string = o1 + ' ' + o2 + ' ' + val
            stack.push(string)
    RPN = stack.pop()
    return RPN


