# Given integer num and base b, converts num to a string representation in base b
def convert(num: int, b: int, final_str ='') -> str:
    if b < 2 or b > 16:
        raise ValueError("Not in Range")
    quotient = num // b
    remainder = num % b
    if remainder > 9:
        New_character= chr(remainder + 55)
        final_str = New_character + final_str
    else:
        num_string = f'{remainder}'
        final_str = num_string + final_str
    if quotient == 0:
        return final_str
    return convert(quotient, b, final_str)
