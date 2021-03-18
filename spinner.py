listAwal = [[1,2,3],[4,5,6],[7,8,9]] #list awal/input
print(listAwal) #untuk menampilkan input
def counterClockwise(x): #fungsi spinner
    listNew = [[x[0][2],x[1][2],x[2][2]],[x[0][1],x[1][1],x[2][1]],[x[0][0],x[1][0],x[2][0]]] #membuat list baru hasil setelah di spin
    print(listNew) # untuk menampilkan list setelah di spin
counterClockwise(listAwal) #running function