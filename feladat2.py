#2. feladat – Kérj be egy N számot, és számold ki az 1-től N-ig terjedő számok szorzatát (faktoriális ELLENTÉTE: itt nem csak N!, hanem általánosan 1·2·3…·N).

n=int(input("Kérek egy N számot: "))

f=1

for i in range(1, n+1):
    f = f * i

print(f"{n} faktoriálisa: {f}")