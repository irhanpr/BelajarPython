#for loops
square = ["red", "yellow", "green", "purple", "blue"]
for i in range(0, 5):
    square[i] = "white"
    print(square[i])

squares= ["red", "yellow", "green"]

for square in squares:
    print(square)

squares = ["red", "yellow", "green"]
for i,square in enumerate(squares): #enumerate digunakkan untuk mendapatkan index dan elemen dari list
    print(square)
    print(i)

#while loops
squares = ['orange', 'orange', 'purple', 'blue']
Newsquares = []
i = 0
while(squares[i] == 'orange'):
    Newsquares.append(squares[i])
    print(Newsquares[i])
    i= i+1

#CASE FOR 1
A = [3,4,5]
for a in A:
    print(a)
#CASE WHILE 1
x=3
y=1
while(y!=x):
    print(y)
    y=y+1