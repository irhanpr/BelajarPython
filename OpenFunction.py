File1 = open("/resources/data/Example2.txt","w")
# file1 = file object
# digunakkan sebagi langkah utuk mencari informasi dari file
# open merupakan method untuk membuka file diikuti dengan tujuan(file_path) dengan syntax(/direktori/nama_file.apa,mode)
# mode merupakan value diantaranya adalah r (read)untuk membaca, w untuk writing dan a untuk appending
# File1.name di gunakkan untuk mengetahui nama file yg dibuka
# File1.mode digunakkan untuk mengetahui mode yg digunakkan
# File1.close() diguanakkan untuk menutup file

with  open(r"C:\Users\irhan\OneDrive - grow distributed users\BelajarPython\Dataset\COVID_INDONESIA\cases.csv") as File1:
    
    file_stuff = File1.readlines(5) #memberikan output berupa list, jika menggunakkan File1.read saja maka hasilnnya akan berupa string biasa
    print(file_stuff) #angka di dalam kurung menunjukkan berapa karakter yang ingin di outputkan
    
