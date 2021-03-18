import math #berfungsi untuk import fungsi pembulatan
seconds = input('Masukkan Detik : ') #user input untuk jumlah detik
listAlfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
'o','p','q','r','s','t','u','v','w','x','y','z','.',',',' '] #listAlfabet berfungsi untuk validasi string dan decimal('.') input
def timeConverter(seconds):#fungsi timeconverter
    d = [char for char in seconds] #untuk memisahkan karakter dalam user input, tujuannya untuk validasi string dan decimal ('.') input
    def cek(x): #fungsi untuk cek string dan decimal ('.')  input
        if x in listAlfabet: # jika character di user input ada di listalfabet maka function cek akan mengeluarkan value Yes
            return 'Yes'
    e = list(map(cek,seconds)) #jika user input ada di alfabet maka tampil 'Yes' dan di konversi menjadi list
    if 'Yes' in e or int(seconds) >359999 or int(seconds)<0 :#validasi string,decimal, max, negatif input
        print('Invalid Input !') # error message
    else : #jika lolos validasi maka program akan menjalankan syntax dibawah
        seconds=(int(seconds)) #konversi user input menjadi integer
        hh = math.floor(seconds/3600) #untuk menghitung jumlah jam
        mm = math.floor((seconds%3600)/60)#untuk menghitung jumlah menit
        ss = (seconds%3600)%60 #untuk menghitung jumlah detik
        def digit(x): #function ini berfungsi agar yang di print bisa 2 digit, 
            if x <= 9: #jika jumlah hh/mm/ss <= 9 maka akan ditambahkan 0 di depannya sehingga menjadi 09
                a = '0',str(x)
            else:#jika jumlah jam tidak <= 9 maka akan mencetak jumlah jam apa adanya karena sudah 2 digit
                a = str(x)
            return a
        print('Konversi : ',(''.join(digit(hh))),':',(''.join(digit(mm))),':',(''.join(digit(ss))))
timeConverter(seconds)