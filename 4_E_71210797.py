import random
print ('=======Program test aritmatika dasar=======')
print('pilihan level yang tersedia :')
print('1. easy')
print('2. medium')
print('3. Hard')
def aritmatika():
    operasi = ['+','-','/','*']
    operator = random.choice(operasi)
    a= int(input('Masukan tingkatan yang ingin anda coba:'))
    if a == 1:        
        
        import os
        soal_ke= 1
        soal_jumlah =10
        score = 0
        if soal_ke <= soal_jumlah :
             os.system('cls')
             a= random.randint(20,50)
             b= random.randint(20,50)
             operator = random.choice(operasi)
             hasil=eval( str(a)+(operator)+str(b))
             hasil=round(hasil,3)
             print('berapakah hasil dari ',a,operator,b)
             jawab = int(input(' '))
             if jawab ==hasil:
                 print('jawaban anda benar!')
             else:
                 print('jawaban anda masih salah!')
                 
                
    elif a ==2:
        
        import os
        soal_ke=1
        soal_jumlah =10
        score = 0
        if soal_ke <= soal_jumlah :
             os.system('cls')
             a= random.randint(20,70)
             b= random.randint(20,70)
             c= random.randint(20,70)
             operator = random.choice(operasi)
             hasil=eval( str(a)+(operator)+str(b)+(operator)+str(c))
             hasil=round(hasil,3)
             print('berapakah hasil dari ',a,operator,b,operator,c)
             jawab = int(input(' '))
             if jawab ==hasil:
                 print('jawaban anda benar!')
             else:
                 print('jawaban anda masih salah!')
    elif a ==3:
       
        import os
        soal_ke=1
        soal_jumlah =10
        score = 0
        if soal_ke <= soal_jumlah :
             os.system('cls')
             a= random.randint(20,100)
             b= random.randint(20,100)
             c= random.randint(20,100)
             d= random.randint(20,100)
             operator = random.choice(operasi)
             hasil=eval( str(a)+(operator)+str(b)+(operator)+str(c)+(operator)+str(d))
             hasil=round(hasil,3)
             print('berapakah hasil dari ',a,operator,b,operator,c,operator,d)
             jawab = int(input(' '))
             if jawab ==hasil:
                 print('jawaban anda benar!')
             else:
                 print('jawaban anda masih salah!')
            

aritmatika()
             
         
         
