def mutate_string(string, position, character):
    s1 = string[:position] + character + string[position+1:]
    return s1
