#5. feladat – Lista elemeinek négyzetre emelése. Adott egy lista, készíts új listát, amely minden elem négyzetét tartalmazza.
nlista =[]
lista = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(lista)):
    nlista.append(lista[i]**2)

print(f"A lista tartalma: {lista}")
print(f"A listában szereplő számok négyzetei: {nlista}")

