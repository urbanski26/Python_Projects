liczba_wejsciowa = 422
liczba_binarna = liczba_wejsciowa
liczba_dziesietna = liczba_wejsciowa
liczba_jedynek_binarnych = 0
liczba_odwrocona = 0

kopia = liczba_wejsciowa

while liczba_binarna > 0:
    if liczba_binarna % 2 == 1:
        liczba_jedynek_binarnych += 1
    liczba_binarna //= 2

    if liczba_dziesietna > 0:
        ostatnia_cyfra = liczba_dziesietna % 10
        liczba_odwrocona = (liczba_odwrocona * 10) + ostatnia_cyfra
        liczba_dziesietna //= 10






print(liczba_binarna)
print(liczba_odwrocona)
print(liczba_jedynek_binarnych)