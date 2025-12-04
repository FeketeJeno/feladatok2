#4. feladat – Számjegyek összege. Kérj be egy számot, majd számold ki a számjegyeinek összegét.

n = (input("Kérek egy számot: "))

ossz = 0


for i in range(len(n)):
    ossz = ossz + int(n[i])

print(f"A számjegyek összege: {ossz}")

