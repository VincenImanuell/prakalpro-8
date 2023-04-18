nama_file = 'buah.txt'
handle = open(nama_file, 'a') # mode append (sambung di belakang)
nama_buah = input('Masukkan nama buah : ')
nama_buah = '\n' + nama_buah
handle.write(nama_buah)

handle.close()