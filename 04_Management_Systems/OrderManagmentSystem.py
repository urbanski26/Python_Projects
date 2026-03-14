
dane_zamowien = [
    ('ID1001', 'Monitor', 450.00, 'Niski'),
    ('ID1002', 'Klawiatura', 120.00, 'Średni'),
    ('ID1003', 'Procesor', 1500.00, 'Wysoki'),
    ('ID1004', 'Myszka', 75.50, 'Niski'),
    ('ID1005', 'Klawiatura', 120.00, 'Wysoki'),
    ('ID1006', 'Monitor', 450.00, 'Wysoki'),
]

pilne_zamowienia = []
historia_cen = set()

for dana in dane_zamowien:
    id, nazwa, cena, pilnosc = dana
    if pilnosc == "Wysoki":
        pilne_zamowienia.append((id, nazwa, cena))
    historia_cen.add((nazwa, cena))

print(pilne_zamowienia)
print(historia_cen)