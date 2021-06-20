def count_substring(string, sub_string):
    c = 0
    for i in range(len(string) - len(sub_string) + 1):
        match = 1
        for j in range(len(sub_string)):
            if string[i+j] != sub_string[j]:
                match = 0
                break
        if match:
            c+=1
    return c
