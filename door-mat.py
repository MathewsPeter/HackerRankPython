# Enter your code here. Read input from STDIN. Print output to STDOUT

i = input()

n = (int)(i.split(" ")[0])
m = (int)(i.split(" ")[1])

p=''
for l in range(n//2):
    p=''
    for j in range(m//2 - 3*l-1):
        p+='-'
    for j in range(2*l+1):
        p+='.|.'
    for j in range(m//2 - 3*l-1):
        p+='-'
    print(p)
    
p=''
for i in range(m//2-3):
    p += '-'
p+='WELCOME'
for i in range(m//2-3):
    p += '-'
print(p)

p=''
for l in reversed(range(n//2)):
    p=''
    for j in range(m//2 - 3*l-1):
        p+='-'
    for j in range(2*l+1):
        p+='.|.'
    for j in range(m//2 - 3*l-1):
        p+='-'
    print(p)
