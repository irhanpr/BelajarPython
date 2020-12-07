#print Hello Python 101
print("Hello Python 101")
print("Hello\nWorld")

x= 43+60+16+41
print(x)
x=x/60
print(x)

total_min=43+42+57
print(total_min)
total_hr=total_min/60
print(total_hr)

name="Michael Jackson"

print(name[0:5]) #panggil indeks dari 0-5
print(name[0:5:2]) #panggil dari 0-5 dengan kelipatan 2
print(name[::2]) #panggil indeks kelipatan 2
print(name[0:2])

A="Thriller is the sixth studio album"
B=A.upper() #meerubah kalimat menjadi upper case
print(B)
C=name.replace('Michael','Janet') #mengganti nilai pada variabel
print(C)
print(name.find('el')) #mencari string dengan memberi nilai index awal dari huruf yang ditulis
print(name.find('Jack')) #kalau ada huruf yang tidak tercantum di string maka outputnya -1

print("0123456".find('1')) #cari angka satu lalu tampilkan

name = "Lizz"
print(name[0:2]) #tampilkan index 0 s/d 2

var= '01234567'
print(var[::2]) #tampilkan kelipatan genap

x = '1'+'2'
print(x) #hasilnnya adalah 12 karena dua inputa diatas berupa string yg ditandai dengan '' atau ""

#TUPPLE
#tuple immutable alias tidak bisa di tambah data

Tuple1 = ("disco" , 10 , 1.2)
print(Tuple1[0])
Tuple2 = Tuple1 + ("hard rock" , 10)
print(Tuple2)
print(Tuple2[3:5])
Ratings = (10,9,6,5,10,8,9,6,2)
Ratings1 = Ratings
RatingsSorted = sorted(Ratings)
print(RatingsSorted)

NT = (1,2,("pop,rock"),(3,4),("disco",(1,2))) #nesting tuple
print(NT[2]) #panggil secara index ke 2
print(NT[4][0]) #panggil dari tuple index ke 4 index 0
print(NT[4][0][3]) #panggil dari tuple index ke 4 index 1 lalu karakter index ke 1

#LIST
#list sama dengan tuple namun mutable alias bisa ditambah datanya

L = ["Michael Jackson", 10.1, 1982, [1,2], ('A',1)]
print(L[0]) #mengakses indeks ke 0
print(L[3][0]) #berikan keluaran berupa list index ke 3 bagian index 0
print(L[3:5])

    #tambah data
L1 = L+["pop", 10]
print(L1) #tampilkan data dari variabel baru

L.extend(["pop",10]) #tambah data ke variabel utama lewat fungsi extend dengan menambah index berdasar inputan
print(L)

L.append(["pop", 10]) #menambah 1 index pada variabel dengan isi berupa inputan
print(L)

#untuk mengganti isi dari index gunakan
A = ["disco",10,1.2]
A[0] = "Hardcore"
print(A)

#untuk hapus gunakan fungsi del(variabel[index]) contoh
del(A[0]) #hapus index  ke 0
print(A) 

del(A[1])
print(A)

#merubah dari string menjadi list, jadi setiap ada spasi dirubah menjadi index
print("hard rock".split())

#list dengan referensi yang sama disebut dengan aliasing contoh
C = ["Hardcore", 10, 1.2]
B = C
print(B)

C[0] = "Banana" #jika bagian C dirubah maka B akan ikut berubah karena refeensinya berubah
print(B)

#cara yang dapat dilakukan bila tidak ingin isi dari B tidak berubah adalah menggunakkan clone dari variabel utama yaitu menambha variabel[:]

D = ["Metalcore", 1.5, 20]
E = D[:] #ini adalah clone

D[0] = "Uchiha Sasuke"
print(E) # maka yang dihasilkan adalah ["Metalcore", 1.5, 20]
print(D)

help(A)

B=["a","b","c"]
print(B[1:])

#Membuat set, tidak ada urutan namun memiliki ciri unique
Set1 = {"pop","rock", "soul", "hardcore", "rock", "disco", "rock"} # ketika dibuat output maka duplikat tidak akan tampil
print(Set1)

#list dapat dirunah menjadi set yaitu dengan cara set()
album_list = ["Michael Jackson", "Thriller", "Thriller", 1982]
album_set = set(album_list)
print(album_set)

#Operasi pada set
A = {"Thriller", "Back in Black", "AC/DC"}
A.add("NSYNC") #menambah data kedalam sets
print(A)
A.remove("NSYNC") #menghapus data dari index
print(A)
print("AC/DC" in A) #untuk mengecek apakah AC/DC ada di variabel A, jika betul maka outputnya adalah True or False
print("Fall Out Boy" in A) #untuk mengecek apakah AC/DC ada di variabel A, jika betul maka outputnya adalah True or False
album_set_1 = {"AC/DC", "Back in Black", "Thriller"}
album_set_2 = {"AC/DC", "Back in Black", "The Dark Side of The Moon"}

album_set_3 = album_set_1 & album_set_2 #operasi intersection penggabuangan dari dua variabel yang memiliki inputan sama
print(album_set_3)

album_set_3 = album_set_1.union(album_set_2) #operasi union untuk menggabungkan seluruh anggota variabel
print(album_set_3)

album_set_3 = {"AC/DC", "Back in Black"}
print(album_set_3.issubset(album_set_1)) #untuk mengecek apakah album set 3 merupakan subset dari album set 1 nilainya akan boolen tru atau false

S={'A','B','C'}

U={'A','Z','C'}

print(U.union(S))

#Dictionaries
#ditandai dengan {} (Curly Bracket)
#the keys immutable and unique
#values bisa sama, tidak bisa dirubah atau bisa dirubah
#tiap key dan value dipisahkan dengan koma contoh "Key1": 1, "Key2": "2"
#contoh lengkap
{"Key1" : 1, "Key2" : "2", "Key3" : [3,3,3], "Keys4" : (4,4,4), ('key5'):5}
DICT = {"Thriller" : 1982,"Back in Black" : 1980, "The Dark Side of The Moon" : 1973, "The Bodyguard": 1992, "Bat Out of Hell" : 1977, 
"Their Greatest" : 1976, "Saturday Night Fever" : 1977, "Rumours" : 1977}

#untuk memanggil isi dari kamus caranya adalah NamaKamus["Kunci"]
print(DICT["Back in Black"]) #ambil nilai/value dari kunci back in black

#untuk menambah isi dari dictionaries tulis dengan NamaKamus["Kunci"] = "Nilai"
DICT["Graduation"] = 2007
print(DICT)

#untuk menghapus dari kamus gunakkan del(NamaKamus["Kunci"])
del(DICT["Thriller"])
print(DICT)

#untuk mengecek apakah ada kunci tersebut didalam kamus gunakkan "Kunci" in NamaKamus output berupa boolean yaitu True atau False
print(int("Thriller" in DICT))
print("Starboy" in DICT)

#untuk mengetahui seluruh keys yang ada NamaKamus.keys()
print(DICT.keys())
#untuk mengetahui seluruh value yg ada gunakkan NamaKamus.values()
print(DICT.values())

D={'a':0,'b':1,'c':2}
print(D['b'])

#Conditions and Branching
#Comparison Operator / Operator perbandingan

a = 6
print(a == 7)
print(a == 6) #operasi sama dengan

i=6 
print(i>5) #operasi lebih kurang dari
print(i>=5) #operasi lebih kurang dari sama dengan
print(i<6) #equality inequality
print(i!= 6) #inequality test

print("AC/DC" == "Michael Jackson")
print("AC/DC" != "Michael Jackson")

    #if else
age=19
#TYPE1 IF
#if(age>18):
 #   print("you can enter")
#print("Move on")

#TYPE2  IFELSE
#if(age>18):
    #print("you can enter")
#else:
    #print("go see Meat loaf")  
#print("move on")

#TYPE3 ELIF (Else IF)
#contoh 1
age = int(input("Please input your age: "))

if(age>18):
    print("You can enter AC/DC")
elif(age==18):
        print("Go and see Pink Floyd")
else:
        print("Go and see Meat Loaf")
print("Move On")

#contoh 2
amount = int(input("Enter amount: "))

if amount<1000:
   discount = amount*0.05
   print ("Discount",discount)
elif amount<5000:
   discount = amount*0.10
   print ("Discount",discount)
else:
   discount = amount*0.15
   print ("Discount",discount)
    
print ("Net payable:",amount-discount)

#LOGIC OPERATORS
# OR menghasilkan nilai false hanya jika semuua bagian false
# contoh kasus

album_year=1990
if(album_year<1980) or (album_year>1989):
    print("The album was mase in the 70's or 90's")
else:
    print("The album was made in 80's")

# AND menghasilkan nilai true hanya jika semua nilai true, jika ada satu false maka yg lain false
# output yang dihasilkan akan berupa boolean yaitu true atau false
# contoh kasus1

album_year = 1983

if(album_year > 1979)  and (album_year < 1990):
    print("This album was made in the 80's")


# Case
x='a'
if(x!='a'):
    print("this is not a")
else:
        print("this is a")

# LOOPS
# merupakan fungsi untuk menampilkan jarak dari 0 sampe N-1 syntaxnya range(N)

print(range(3))
print(range(10,15)) #jika nilai awal lebih besar, angka yg di tampilkan akan start dari 10 berakhir 15-1=14

#FOR LOOPS
square = ["red","yellow","green","purple","blue"]
for i in range(0,5):
    square[i]="white"
