a=int(input())
b=int(input())
c=int(input())
tb=(a*2+b*3+c)/6
if tb<3:
    print('Kém')
elif 3<=tb<5:
    print('Yếu')
elif 5<=tb<6:
    print('Trung binh')
elif 6<=tb<7:
    print('Trung binh Kha')
elif 7<=tb<8:
    print('Kha')
elif 8<=tb<9:
    print('Gioi')
else:
    print('Xuat sac')
    