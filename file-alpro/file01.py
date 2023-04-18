nama_file = 'data.txt'
handle = open(nama_file, 'r') # membuka dalam mode read only
isi_file = handle.read() # membuka isi keseluruhnan
print(isi_file)
handle.close() # Harus ditutup supaya file bebas dari pegangan program ini