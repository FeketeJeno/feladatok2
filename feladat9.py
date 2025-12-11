"""
9. feladat – OOP + lista: Tanulók kezelése

Student osztály: név, életkor, átlag.
Kérj be 3 tanulót, tedd őket listába, majd írd ki annak a nevét, akinek a legjobb az átlaga.
"""

class Student:
    
    
    def __init__(self, nev, eletkor, atlag):
        self.name = nev
        self.age = eletkor
        self.avg = atlag
        
students = []

for i in range(3):
    nev = input(f"Kérem a(z) {i+1}. diák nevét: ")
    eletkor = int(input("Kérem a diák életkorát:"))
    atlag = float(input("Kérem a diák átlagát: "))
    students.append(Student(nev,eletkor,atlag))

best = max(students, key=lambda s: s.avg)
print("A legjobb átlagú tanuló:")
print(best.name)

