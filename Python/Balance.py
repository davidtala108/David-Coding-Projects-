from stack import *

list_of_open = ['[','{','(']
list_of_close = [']','}',')']
check_dictorary = {'{':'}','[':']','(':')'}
def is_balance(string):
    Parker = Stack(len(string))

    for i in range(len(string)):
        if string[i] in list_of_open:
                Parker.push(string[i])
        elif string[i] in list_of_close:
            if Parker.is_empty():
                return False
            x = Parker.pop()
            if check_dictorary[x] != string[i]:
                return False
    return Parker.is_empty()



