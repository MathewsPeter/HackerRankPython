s1=""
hh=(int)(s[0:2])
mm = s[3:5]
ss = s[6:8]
AP = s[-2]

if AP == 'P':
    if hh==12:
        hh = 0
    s1+= (str)(hh + 12)
else:
    if hh==12:
        hh = 0
    if hh<10:
        s1+='0'
    s1+= (str)(hh)
s1+=":" + mm + ":" + ss 
return s1
