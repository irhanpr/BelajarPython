class Circle (object):
    def __init__(self, radius = 3, color = 'red'): # ----> baris ini merupakan data atribut sebagai bagian dari kelas
        self.radius = radius; # __init__ merupakan method special atau constructor yang digunakkan untuk menginisialisasi data atribut
        self.color = color; #sedangkan radius dan color digunakkan untuk inisialisasi jarak dan warna pada atribut di dalam class
        #self parameter diguankkan sebagai permulaan dari class
    def add_radius(self,r):
            self.radius = self.radius +r
    def drawCircle(self):