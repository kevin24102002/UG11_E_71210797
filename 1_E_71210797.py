def Fungsipangkatakar():
    ap=print('Menu program yang Tersedia')
    ab=print('1. pangkat angka')
    ac=print('2. akarkan bilangan')

    pilihan=int(input('masukan pilihan yang diinginkan : '))
    if pilihan == 1:
        print('Masukan angka yang ingin di pangkatkan')
        b=int(input('Angka:'))
        e=print('ingin memodifikasi pangkat ?(yes/no)')
        c=input(':')
        if c == 'yes':
            f=int(input('Masukan nilai pangkat :'))
            hasil =b ** f
            r=float(b)
            s=float(f)
            t=float(hasil)
            print('Hasil dari',r,'^',s,' = ',t)
        elif c == 'no':
            hasol =b ** 2
            r=float(b)
            u=float(hasol)
            print('hasil dari',r,'^ 2 =',u)
    elif pilihan == 2:
        print('masukan angka yang ingin di akar')
        p=int(input('Angka :'))
        q=print('ingin memodifikasi akar?(yes/no)')
        r=input(':')
        if r == 'yes':
            t=int(input('masukan nilai akar:'))
            hasel = p ** (1.0/t)
            v=float(t)
            x=float(p)
            y=float(hasel)
            print('hasil akar pangkat',v,'dari',x,'=',hasel)
        elif r == 'no':
            hasal = p ** (1.0/2)
            x=float(p)
            z=float(hasal)
            re=round(z,2)
            print('hasil akar pangkat 2 dari',x,'=',re)
Fungsipangkatakar()





    

