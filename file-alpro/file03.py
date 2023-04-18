nama_file = 'transkrip.txt'
handle = open(nama_file, 'r')
no_baris = 1
totalsks = 0
totalbobot = 0
sks = 0
ulang = ''
print('Mata kuliah : ')
for baris in handle:
    if no_baris % 3 == 1:
        matkul = baris.strip()
        print(baris, end='')
    if no_baris % 3 == 2:
        sks = int(baris)
        totalsks = totalsks + int(baris)
    if no_baris % 3 == 0:
        if baris.strip() == 'A':
            totalbobot = totalbobot + sks * 4
        elif baris.strip() == 'B':
            totalbobot = totalbobot + sks * 3
        elif baris.strip() == 'C':
            totalbobot = totalbobot + sks * 2
        elif baris.strip() == 'D':
            totalbobot = totalbobot + sks * 1
        elif baris.strip() == 'E':
            ulang = ulang + matkul + '\n'
    no_baris = no_baris + 1
print('Total sks:', totalsks, 'sks')
print(f'IP Semester: {totalbobot/totalsks:.2f}')
print(f'Mata kuliah ini harus diulang: \n{ulang}')
handle.close()