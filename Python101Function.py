#function atau fungsi merupakan suatu kumpulan perintah, kita dapat
#membuat fungsi kita sendiri, atau menggunakkan fungsi yg sudah disediakan orang untuk kita
#contoh

def function(a):
    """add 1 to a"""
    b=a+1;

    print(a, "+1=",b)
    return b

#fungsi built in python
#contoh
#len digunakkan untuk mengukur panjang dari sebuah list
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
print(len(album_ratings))
#sum, menjumlah seluruh elemen yg ada di list
S = print(sum(album_ratings))
#sorted digunakkan untuk mengurutkan element dari list
sorted_album_ratings  = print(sorted(album_ratings))

album_ratings.sort()
print(album_ratings)

#membuat fungsi, fungsi yang dapat kita buat disesuaikan untuk case atau penggunaan
# contoh1
def add1(a): # (a) adalah paramter, jangan lupa tambahkan : (colon). secara umum syntaxnya adalah deff namafungsi(paramenter) isi return 
    """
    add 1 to a
    """
    b=a+1
    return b

c = add1(5)
print(c)
d = add1(8)
print(d)

# contoh2 penambahan dokumentasi, ditujukan untuk memudahkan penggunaan fungsi dengan cara dipanggil melalui help. yaitu dengan syntax """dokumentasi"""
help(add1)

#multiple parameter, setiap fungsi bisa memiliki banyak parameter
def Mult(a,b):
    """
    perkalian dua angka
    """
    c = a*b
    return c

e = Mult(2,3)
print(e)

f = Mult(10,3.14)
print(f)

g = Mult(2, "Michael Jackson\n")
print(g)

# contoh 3
def MJ():
    print("Michael Jackson")
 
# contoh 4
def NoWork():
    pass #digunakkan ketika ada body yg ingin di beri tempat kosong atau fungsi tanpa perintah
print(NoWork())

#contoh 5
def add1(a):
    b = a+1
    print(a, "plus 1 equals", b)
    return b
print(add1(2))

#contoh ke 6 menggunakkan loop pada fungsi
def printStuff(Stuff):
    for i,s in enumerate(Stuff): #dari parameter Stuff ambil jummmlah indexnya menggunakkan fungsi enumerate
        print("Album", i+1, "Rating is", s)

album_ratings = [10.0, 8.5, 9.5]
print(printStuff(album_ratings))

#contoh ke 7 menggunakkan asterisk (*) pada parameter
def ArtistNames (*names):
    for name in names:
        print(name)

ArtistNames("Michael Jackson", "AC/DC", "Pink Floyd")
ArtistNames("Michael Jackson", "AC/DC")

#contoh ke 7, global scope merupakan variable yg berada di luar fungsi dan dapat diakses dari manapun

def AddDC(y):
    global x #penambahan kalimat global menyatakan bahwa variabel ini global loh gan jadi bisa di akses dibagaian codemanapun
    x=x+"DC"
    print(x)
    return(x)

x = "AC"
z = AddDC(x)

#Contoh ke 8, local variabel. variabel yg hanya bisa di akses lewat fungsi saja
def Thriller():
    Date = 1982
    return Date

print(Thriller())

# Contohe ke 9, rubah menjadi variabel global
def Thriller():
    Date = 1982
    return (Date)

Date = 2017 #ini merupakan variabel global
print(Thriller()) #output scope yaitu 1982
print(Date)

#Contoh ke 10, apabila pada body fungsi tidak ada value, maka yg digunakkan adalah variabel global
def ACDC(y):
    print(Rating)
    return(Rating+y)

Rating = 9
Z=ACDC(1)
print(Rating)

# Contoh ke 11, global scope lagi


a=1
def add(b):
    return a+b
c=add(10)