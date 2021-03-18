jmlMahasiswa = int(input('Jumlah Mahasiswa : ')) #user input
b = [] #untuk menampung data seluruh mahasiswa
c = [] #list c-f untuk temporary list dalam perhitungan beasiswa
d = []
e = []
f = []
siTi20 = [] #list untuk mahasiswa SI dan TI yang menerima beasiswa 20%
siTi30 = [] #list untuk mahasiswa SI dan TI yang menerima beasiswa 30%
dkvIndus25 = [] #list untuk mahasiswa DKV dan indus yang menerima beasiswa 25%
dkvIndus35 = [] #list untuk mahasiswa DKV dan indus yang menerima beasiswa 35%
print (' ')
for i in range (jmlMahasiswa): # untuk looping user input sejumlah jmlMahasiswa
    for j in range(1):
        nim = input('Nim : ')
        nama = input('Nama : ')
        alamat = input('Alamat : ')
        sekolah = input('Asal Sekolah : ')
        prodi = input('Kode Prodi : ')
        ipkAwal = int(input('Nilai IPK Awal : '))
        uts = float(input('Nilai UTS : '))
        uas = float(input('Nilai UAS : '))
        tm = float(input('Nilai TM : '))
        a = [nim,nama,alamat,sekolah,prodi,ipkAwal,uts,uas,tm] #menyimpan data mahasiswa setiap kali looping
        b.append(a) #memasukan data setiap mahasiswa ke list seluruh data mahasiswa
        print(' ') # untuk spasi antar looping fungsi user input 
for i in range (len(b)):
    b[i].append((0.3*b[i][6]+0.3*b[i][8]+0.4*b[i][7])) #perhitungan IPK baru
    if (b[i][4] == 'TI' or b[i][4] == 'SI') and (b[i][9] > 75 and b[i][9]<85): #kondisi untuk beasiswa 20% prodi SI dan TI
        b[i].append('20%') # jika lolos validasi maka akan diberikan keterangan 20% pada data set mahasiswa tersebut
        c = [b[i][0],b[i][1]] #memindahkan data mahasiswa yang menerima beasiswa ke temporary list
        siTi20.append(c) #memindahkan data penerima beasiswa dari temporary list ke list utama
    elif (b[i][4] == 'TI' or b[i][4] == 'SI') and (b[i][9] > 85 and b[i][9]<=100): #kondisi untuk beasiswa 30% prodi SI dan TI
        b[i].append('30%') # jika lolos validasi maka akan diberikan keterangan 30% pada data set mahasiswa tersebut
        d = [b[i][0],b[i][1]] #memindahkan data mahasiswa yang menerima beasiswa ke temporary list
        siTi30.append(d) #memindahkan data penerima beasiswa dari temporary list ke list utama
    elif (b[i][4] == 'DKV' or b[i][4] == 'Teknik Industri') and (b[i][9] > 75 and b[i][9]<85):
        b[i].append('25%') # jika lolos validasi maka akan diberikan keterangan 25% pada data set mahasiswa tersebut
        e = [b[i][0],b[i][1]] #memindahkan data mahasiswa yang menerima beasiswa ke temporary list
        dkvIndus25.append(e)#memindahkan data penerima beasiswa dari temporary list ke list utama
    elif (b[i][4] == 'DKV' or b[i][4] == 'Teknik Industri') and (b[i][9] > 85 and b[i][9]<100): #kondisi untuk beasiswa 35% prodi DKV dan Teknik Industri
        b[i].append('35%') # jika lolos validasi maka akan diberikan keterangan 35% pada data set mahasiswa tersebut
        f = [b[i][0],b[i][1]] #memindahkan data mahasiswa yang menerima beasiswa ke temporary list
        dkvIndus35.append(f)#memindahkan data penerima beasiswa dari temporary list ke list utama
    else:
        b[i].append('No Beasiswa') #jika tidak lolos validasi apapun maka diberi keterangan no beasiswa
#syntax dibawah ini untuk menampilkan output
print ('Seluruh data mahasiswa \n')
for index, value in enumerate(b):
        print(value)
print()
print('Penerima Beasiswa SI dan TI 20% \n')
for index, value in enumerate(siTi20):
        print(value)
print()
print('Penerima Beasiswa SI dan TI 30% \n')
for index, value in enumerate(siTi30):
        print(value)
print()
print('Penerima Beasiswa DKV dan Teknik Industri 25% \n')
for index, value in enumerate(dkvIndus25):
        print(value)
print()
print('Penerima Beasiswa DKV dan Teknik Industri 35% \n')
for index, value in enumerate(dkvIndus35):
        print(value)
print()