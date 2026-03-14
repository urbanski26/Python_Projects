dane_logowania = [
    ('U101', 'OK', 45),
    ('U205', 'BŁĄD', 0),
    ('U101', 'OK', 60),
    ('U307', 'OK', 30),
    ('U205', 'BŁĄD', 0),
    ('U410', 'OK', 90)
]

sesje_ok = []
bledne_id = set()
suma = 0
for logowanie in dane_logowania:
    id, status, czas = logowanie
    if status == "OK":
        sesje_ok.append((id, czas))
    else:
        bledne_id.add(id)
    suma += czas
if len(sesje_ok) > 0:
    srednia = round(suma / len(sesje_ok))
print("Sesje poprawne ", end="")
for sesja in sesje_ok:
    print(f"User: {sesja[0]} Czas: {sesja[1]} sekund", end=" | ")

print()
print("Błędne id: ", end="")
for blad in bledne_id:
    print(f"ID: {blad}", end="")
print()
print(f"Średnia udanych sesji: {srednia}")


