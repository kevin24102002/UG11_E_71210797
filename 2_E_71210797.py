def huruftengah(a):
    bagi=len(a)//2

    if (len(a)%2==0) and ((len(a)/2)%2==0):
        return a[(bagi)//2 : ((bagi)//2)*-1]
    elif(len(a)%2==0) and ((len(a)/2)%2!=0):
        return a[((bagi)//2)+1 : (((bagi)//2)+1)*-1]
    else:
        return a[(((bagi)+1)//2) : (((bagi)+1)//2)*-1]

a = str(input('masukan kata :'))
print('Huruf tengah pada kata',a,'adalah',huruftengah(a))
