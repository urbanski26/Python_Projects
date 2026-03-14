import random

bazowy_portfel = ["Złoto", "Akcje", "Obligacje"]
inwestor_A = bazowy_portfel
inwestor_B = bazowy_portfel.copy()

inwestor_A.append("Kryptowaluty")
print(id(bazowy_portfel) == id(inwestor_A))
print(id(bazowy_portfel) == id(inwestor_B))
print(id(inwestor_A) == id(inwestor_B))
print(bazowy_portfel)
print(inwestor_A)
print(inwestor_B)

nowe = input("Podaj dodatkowe aktywa: ").title().split(",")
nowe_oczyszczone = [a.strip() for a in nowe]
inwestor_B = list(set(inwestor_B + nowe_oczyszczone))
print(inwestor_B)

wycena = {}

for key in inwestor_B:
    wycena[key] = str(random.randint(100, 1000))
for key, value in wycena.items():
    print(f"{key:<20} {value:>10}")

wycena = {aktywo: random.randint(100, 1000) for aktywo in inwestor_B}

print("\n" + "="*32)
print(f"{'AKTYWO':<20} | {'WYCENA':>10}")
print("-" * 32)

for aktywo, cena in wycena.items():
    print(f"{aktywo:<20} | {cena:>7} PLN")

print("="*32)