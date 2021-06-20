def swap_case(s):
    s1 = ''
    for c in s:
        if c.islower():
            s1+=c.upper()
        elif c.isupper():
            s1+=c.lower()
        else:
            s1+=c
    return s1
