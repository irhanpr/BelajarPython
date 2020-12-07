#Method, sorting adalah conth dari beberapa metode untuk berinteraksi dengan data di dalam objek
#contoh

Ratings = [10, 9, 6, 5, 10, 8, 9, 6, 2]
Ratings.sort() #mengurutkan dari kecil ke besar
print(Ratings)
Ratings.reverse()
print(Ratings)

#Creating your own types:
#Defining classes
# Class terdiri dari Data Attributes, Methods dan kumpulan object
# class Circle (object): #struktur dari class adalah class nama_kelas (parent_class)

class Circle (object):
    def __init__(self, radius, color): # ----> baris ini merupakan data atribut sebagai bagian dari kelas
        self.radius = radius; # __init__ merupakan method special atau constructor yang digunakkan untuk menginisialisasi data atribut
        self.color = color; #sedangkan radius dan color digunakkan untuk inisialisasi jarak dan warna pada atribut di dalam class
        #self parameter diguankkan sebagai permulaan dari class
    def add_radius(self,r):
            self.radius = self.radius +r

class Rectangle (object):
    def __init__(self, color, height, width):
        self.height = height;
        self.width = width;
        self.color = color;

C1 = Circle(10, "red")
print(C1.radius)
print(C1.color)

C1.color = "blue"

print(C1.color)

C2 = Circle (2,'red')
C2.add_radius(8)

print(C2.radius)

dir (Circle):