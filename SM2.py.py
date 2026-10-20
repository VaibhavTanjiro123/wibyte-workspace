import random
def eoswap(x):
    if len(x)%2!=0:
        x=x +' '
    e_l=x[::2]
    o_l=x[1::2]
    s = ""
    for i in range(len(e_l)):
        s=s+o_l[i]
        s=s+e_l[i]

    return s
def rev(x):
    s = x[::-1]
    return s
def wr(x):
   words=x.split()
   s=''
   for kk in range (len(words)):
       s=s+rev(words[kk])
   return s
    
def swap_middle(x):
    
    if len(x)%2!=0:
            x = x + " "
    first_half = x[0:int(len(x)/2):1]
    second_half=x[int(len(x)/2)::1]
    s=''
    s=s+second_half
    s=s+first_half
    return s
def rfc(msg,N):
    M=2*N-2
    if len(msg)% M !=0:
        msg=msg+(M-len(msg)%M)*' '
    s=''
    for kk in range(N):
        temp=''
        if kk==0:
            temp=msg[kk::M]
        else:
            temp1=msg[kk::M]
            temp2=msg[M-kk::M]

            for jj in range(len(temp1)):
                temp=temp+temp1[jj]+temp2[jj]
        s=s+temp
    return s
letters='abcdefghijklmnopqrstuvwxyz'
ucl=letters.upper()
nums='0123456789'
def caesarciph(x,n):
    s=''
    for i in range(len(x)):
        if x[i]==' ':
            s=s+' '
        else:
            if x[i].islower():                
                idx=letters.find(x[i])
                newidx=(idx + n)%26
                s=s+letters[newidx]
            elif x[i].isupper():
                idx=ucl.find(x[i])
                newidx=(idx + n)%26
                s=s+ucl[newidx]
            elif x[i].isnumeric():
                idx=nums.find(x[i])
                newidx=(idx + n)%10
                s=s+nums[newidx]
    
    return s
def atbash_ciph(x):
    s=''
    for i in range(len(x)):
        if x[i]==' ':
            s=s+' '
        else:
            if x[i].islower():                
                idx=letters.find(x[i])
                newidx=25-idx
                s=s+letters[newidx]
            elif x[i].isupper():
                idx=ucl.find(x[i])
                newidx=25-idx
                s=s+ucl[newidx]
            elif x[i].isnumeric():
                idx=nums.find(x[i])
                newidx=10-idx
                s=s+nums[newidx]
    return s
def vigenereciph(x,key):
    s=''
    for i in range(len(x)):
        if x[i]==' ':
            s=s+' '
        else:
            if x[i].islower():                
                idx=letters.find(x[i])
                newidx=(idx + key[i%len(key)])%26
                s=s+letters[newidx]
            elif x[i].isupper():
                idx=ucl.find(x[i])
                newidx=(idx + key[i%len(key)])%26
                s=s+ucl[newidx]
            elif x[i].isnumeric():
                idx=nums.find(x[i])
                newidx=(idx + key[i%len(key)])%10
                s=s+nums[newidx]
    
    return s
x ="python is cool"
xeo=eoswap(x)
xrev=rev(x)
xwr=wr(x)
xsm=swap_middle(x)
print(xeo)
print(xrev)
print(xwr)
print(xsm)
print(rfc('hellomynamej',3))

x='Blox Fruits is Goated'
xencode=caesarciph(x,3)
print(xencode)
y= xencode
xdecode=caesarciph(y,-3)
input()
print(xdecode)


msg='python'
sc=''
for kk in range(10):
    n=random.randint(0,25)
    sc=sc+letters[n]
msg=msg+sc
print(msg)


enc=random.randint(0,4)
if enc==0:
    msgenc=msg
elif enc==1:
    msgenc=eoswap(msg)
elif enc==2:
    msgenc=rev(msg)
elif enc ==3:
    msgenc=wr(msg)
else:
    msgenc=swap_middle(msg)
print(msgenc)
msgenemy=caesarciph(msgenc,random.randint(1,25))
print(msgenemy)
for kk in range(1,26):
    dec=caesarciph(msgenemy,kk)
    deceo=eoswap(dec)
    decr=rev(dec)
    decwr=wr(dec)
    decsm=swap_middle(dec)
    print(kk,dec)


    if dec[0:6:1]=='python':
        print('code cracked')
        break
    elif deceo[0:6:1]=='python':
        print('code cracked')
        break
    elif decr[0:6:1]=='python':
        print('code cracked')
        break
    elif decwr[0:6:1]=='python':
        print('code cracked')
        break
    elif decsm[0:6:1]=='python':
        print('code cracked')
        break

print(caesarciph('Ice Fruit Is Really Good!!!',23))
print(atbash_ciph('Ice Fruit Is Really Good!!!'))
print(vigenereciph('Ice Fruit Is Really Good!!!',[1,2,3,4,5]))
input()
print('Ice Fruit Is Really Good!!!')