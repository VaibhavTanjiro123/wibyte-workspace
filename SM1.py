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
x ="python is cool"
xeo=eoswap(x)
xrev=rev(x)
xrw=wr(x)
xsm=swap_middle(x)
print(xeo)
ans=input('What is your guess?')
if ans==x:
    print('You did it!!!')
else:
    print('Try again')
print(xrev)
ans=input('What is your guess?')
if ans==x:
    print('You did it!!')
else:
    print('Try again')
print(xrw)
ans=input('What is your guess?')
if ans==x:
    print('You did it!!!')
else:
    print('Try again')
print(xsm)
ans=input('What is your guess?')
if ans==x:
    print('You did it!!!')
else:
    print('Try again')



print(rfc('hellomynamej',3))