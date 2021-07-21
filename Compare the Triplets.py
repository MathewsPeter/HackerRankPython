AB=[0,0]
    for i in range(len(a)):
        if a[i] > b[i]:
            AB[0]+=1
        elif a[i] < b[i]:
            AB[1]+=1   
    return AB
