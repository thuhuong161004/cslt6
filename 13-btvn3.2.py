m1=int(input('M1='))
m2=int(input('M2='))
m3=int(input('M3='))
S=int(input('S='))
if S<=100:
    print('Phai tra=',S*m1,sep='')
if 101<=S<=150:
    print('Phai tra=',100*m1+(S-100)*m2,sep='')
if 151<=S:
    print('Phai tra=',100*m1+m2*50+(S-150)*m3,sep='')
        