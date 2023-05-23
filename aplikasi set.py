aplikasi = {
    1:['A', 'B', 'D', 'E', 'F'],
    2:['B', 'D', 'G'],
    3:['C','F', 'G','B']
}

#Ubah ke set
setapk1 =[]
for keys in aplikasi.keys():
    setapk1.append(set(aplikasi[keys]))
#print(setapk1) 

#Tampilkan aplikasi di semua kategori tanpa duplikat.
union = setapk1[0] | setapk1[1] | setapk1[2]
print(f'Aplikasi yang ada: {union}')

#Aplikasi yang muncul di semua kategori
hasil = setapk1[0] & setapk1[1] & setapk1[2]        #union   #Harus dibuat dinamis(Perulangan, no index)
print(f'Aplikasi di semua kategori adalah {hasil}')