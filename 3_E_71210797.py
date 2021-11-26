print('====program manipulasi string===')
print('pilihan menu')
print('1. hitung kata')
print('2. cek angka')
print('3. ubah kata')

opsi = input('pilihan anda :')
kata = input('masukan sebuah kalimat/kata:')
hasil = (kata.lower())

if opsi =='1':
    w = input('masukan kata yang ingin dihitung :')
    x = hasil.count(w)

    print('terdapat sebanyak', x , 'kata',w,'didalam string')

if opsi =='2':
    w=input('masukan kata yang ingin di cek:')
    x=w.upper()
    y = hasil.replace(w,x)

    print('kata',w,'terdapat di dalam string')
    print('stinrg diubah menjadi :')
    print(y)

if opsi =='3':
    a = input('masukan kata yang ingin diubah:')
    b= input ('masukan kata pengganti:')

    print('anda akan mengubah kata',a,' menjadi',b,'sebanyak 1X')
    ubah = input('apakah anda ingin mengubah jumlah total pengganti kata ?(yes/no)')

    if ubah =='yes':
        x = int (input('masukan jumlah total penggantian:'))
        print('string berhasil diubah menjadi :')
        y= hasil.replace(a, b, x)
        print (y)

    elif ubah =='no':
        x=1
        print('string berhasil diubah menjadi :')
        y = hasil.replace(a, b, x)
        print (y)
