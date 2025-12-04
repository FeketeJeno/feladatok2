#6. feladat – Szótár gyakorlás. Kérj be 5 nevet és életkort, majd tárold őket egy dict-ben. Ezután írd ki a legidősebb személy nevét.

#emberek = {}
#kor = {}


#for i in range(3):
#    lista = []
#    nev = input(f"A(z) {i+1}. név: ")
#    ek= input(f"A(z) {i+1}. életkor: ")
#    lista.append(ek)
#    hsz = input("Hajszine: ")
#    emberek[nev] = lista
#max =0
#i=0
#for x in emberek:
#if int(emberek[x][0]) > int(max)
#max=int(emberek[x][0])
#i=x

emberek = {}


for i in range(2):
    nev = input(f"Add meg a(z) {i+1}. nevet: ")
    kor = int(input("Add meg az életkorát: "))
    emberek[nev] = kor

# Legidősebb személy meghatározása
legoregebb = max(emberek, key=emberek.get)

print("A legidősebb személy:", legoregebb)
