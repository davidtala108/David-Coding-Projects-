# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in: str) -> list[str]:
    if str_in=='':
        return []
    elif len(str_in)==1:
        return [str_in]
    elif len(str_in)==2:
        new_string = str_in[1] +str_in[0]
        return [str_in, new_string]
    new_lst = []
    for i in range(len(str_in)):
        B = str_in[:i] + str_in[i+1:]
        C = perm_gen_lex(B)
        for C in C:
            new_lst.append(str_in[i]+C)
    return new_lst