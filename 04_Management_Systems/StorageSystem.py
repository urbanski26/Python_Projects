nowe_dostawy = [
    ('Klawiatura Mechaniczna', 10, 250.00),
    ('Myszka Ergonomiczna', 25, 99.90),
    ('Klawiatura Mechaniczna', 5, 250.00),
    ('Monitor 27', 8, 850.00),
    ('Myszka Ergonomiczna', 15, 99.90),
]

magazyn = {}

for dostawa in nowe_dostawy:
    nazwa, ilosc, cena = dostawa
    if nazwa in magazyn:
        stara_ilosc, stara_cena = magazyn[nazwa]
        nowa_ilosc  = stara_ilosc + ilosc
        magazyn[nazwa] = (nowa_ilosc, stara_cena)
    else:
        magazyn[nazwa] = (ilosc, cena)
for produkt, (ilosc, cena) in magazyn.items():
    print(f"{produkt}: Ilość = {ilosc}, Cena = {cena:.2f} PLN")