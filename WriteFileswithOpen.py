#File1 = open("C:\Users\irhan\OneDrive - grow distributed users\BelajarPython\Dataset\melata.txt","w")
#tutorial ini mengajarkan bagaimana menulis kedalam file dari perintah python
Lines = ["This is line A\n","This is line B\n","This is line C\n"]
with open(r"C:\Users\irhan\OneDrive - grow distributed users\BelajarPython\Dataset\melata.txt","w") as File1:
    for line in Lines:
        File1.write(line)
        
with open(r"C:\Users\irhan\OneDrive - grow distributed users\BelajarPython\Dataset\melata.txt","a") as File1: #append atau method "a" menambahkan data kepada file yg sudah ada
    File1.write("This is line C")
    
#Berikut contoh mengcopy isi dari satu file ke file yg baru
with open(r"C:\Users\irhan\OneDrive - grow distributed users\BelajarPython\Dataset\Example1","r") as readfiles:
    
    with open(r"C:\Users\irhan\OneDrive - grow distributed users\BelajarPython\Dataset\Example2","w") as writefile:
        
        for line in readfiles:
            writefile.write(line)
            