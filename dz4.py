'''
Napisati program koji vrši određenu obradu nad stringom u prvoj zadatoj liniji na
standardnom ulazu na osnovu stringa zadatog u drugoj liniji. Drugi string treba razdvojiti na
reči (reči su razdvojene tačno jednim blanko znakom) i umetati ih redom (svaku reč tačno
jedanput) u prvi string počevši od njegovog početka, ukoliko je to moguće. Reč je moguće
umetnuti u string ukoliko se sva slova od mesta umetanja u prvom stringu poklapaju sa
slovima reči koja se umeće, u dužini reči koja se umeće. Smatrati da se drugi zadati string
sastoji samo iz slova engleskog alfabeta (malih i velikih) i blanko znakova, a prvi zadati
string sadrži dodatno i znak ?, koji menja bilo koji karakter. Ukoliko neki od učitanih
stringova ne sadrži dozvoljene znakove, korektno prekinuti program.
Program treba da:
1) Učita zadate stringove.
2) Obradi prvi string koristeći drugi u skladu sa navedenim zahtevom.
3) Ispiše izmenjeni prvi string.
'''
string = input()
lista = input().split()

dozvoljeni_znakovi_prve_linije = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '?', ' ']

for s in string:
    if s not in dozvoljeni_znakovi_prve_linije:
        quit()
dozvoljeni_znakovi_druge_linije = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for elem in lista:
    for i in range(len(elem)):
        if elem[i] not in dozvoljeni_znakovi_druge_linije:
            quit()
if "?" not in string:
    quit()


pozicija = 0
while pozicija < len(string):
    for rec in lista:
        b = True
        pom_pozicija = pozicija
        for i in range(len(rec)):
            if rec[i] != string[pom_pozicija] and string[pom_pozicija] != "?":
                b = False
                break
            else:
                pom_pozicija += 1
                if pom_pozicija == len(string) and len(rec) - 1 > i:
                    b = False
                    break
        if b:
            str_list = list(string)
            for i in range(len(rec)):
                str_list[pozicija + i] = rec[i]
            string = "".join(str_list)
            lista.remove(rec)
            pozicija = pom_pozicija - 1
            break
    pozicija += 1

print(string, end="")