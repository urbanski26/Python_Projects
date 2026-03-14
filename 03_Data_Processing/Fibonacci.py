limit_max = 100
a = 0
b = 1
ilosc_elementow = 15
licznik = 0

while licznik < ilosc_elementow:
    if a > limit_max:
        print("Limit przekroczony")
        break
    else:
        print(a)
        temp = a + b
        a = b
        b = temp
        licznik += 1
        continue
