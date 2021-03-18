a = [] # untuk menampung character/huruf dalam input
def urai(x):#fungsi urai
    a.append([char for char in x])#memasukan huruf ke dalam list a
    b = [] #untuk menampung kata setelah di urai
    c = [] #untuk menggabungkan kata yang sudah diurai
    for i in range(len(x)):#function for i batasan nya sesuai dengan jumlah huruf, untuk menyimpan huruf yang sudah dipisah dan di tambahkan dengan kombinasi huruf berikutnya
        for j in range(i+1):#function for j batasann nya sesuai dengan index i supaya tidak looping ke semua huruf.
            b = a[0][j] #line ini berfungsi untuk menggabungkan huruf yang sudah dicacah dengan cacahan huruf berikutnya.
            c.append(b)
    return c #fungsi return berfungsi sebagai output ketika function urai dijalankan.
print(''.join(urai('Purwadhika'))) #menggunakan fungsi join untuk menyatukan huruf dalam list c