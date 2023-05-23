en = int(input("Masukan n:"))       #Input user as usual
bilangan_input = set()              #Siapkan set kosong

#Minta input n bilangan, masukan ke set
for i in range(en):
    bilangan = int(input("Masukan bilangan:"))

print(f'Bilangan unik yang anda miliki sebesar: {len(bilangan_input)} bilangan unik')
print(f'Bilangan unik yang anda masukan adalah: {bilangan_input}')
print(f'Bilangan terbesar yang anda masukan adalah: {max(bilangan_input)}')
print(f'Bilangan terkecil yang anda masukan adalah: {min(bilangan_input)}')
