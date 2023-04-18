# read file sedikit"
nama_file = 'data.txt'
handle = open(nama_file, 'r') # membuka dalam mode read only
for baris in handle:
    if baris[0] == 'b':
        print(f'{baris}', end='')
handle.close()

print('\n == \n') # atau

nama_file = 'data.txt'
handle = open(nama_file, 'r') # membuka dalam mode read only
for baris in handle:
    if baris.startswith('b'):
        print(f'{baris}', end='')
handle.close()