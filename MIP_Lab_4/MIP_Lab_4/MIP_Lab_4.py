#intersectie de multimi
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx & sety
print(setz)

#numar aparitii vocale in propozitii
voc="aeiou"
s=str(input())
d={}
for i in range(len(s)):
    a=s[i]
    if a in voc:
        if a in d:
            b=d[a]+1
        else:
            b=1
        d[a]=b
print(d)


#sortare lista tupluri dupa numarul zecimal
price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(price, key=lambda x: float(x[1]), reverse=False))