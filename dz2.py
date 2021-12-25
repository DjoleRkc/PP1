'''
Lista celih brojeva se unosi sa standardnog ulaza. Ako se neki broj pojavljuje više od jednom (nezavisno od +/- predznaka), izbaciti
sva pojavljivanja tog broja. Na izlazu ištampati novoformiranu listu i broj izbačenih elemenata.
'''
nova_lista = []
niz = input()
lista_brojeva = [int(b) for b in niz.split(" ")]
duzina_niza = len(lista_brojeva)

for k in lista_brojeva:
    k = abs(k)
    if k not in nova_lista:
        nova_lista.append(k)

for e in nova_lista:
    if e in lista_brojeva:
        lista_brojeva.remove(e)

for b in lista_brojeva:
    apsolutna = abs(b)
    if apsolutna in nova_lista:
        nova_lista.remove(apsolutna)

broj_izbacenih_elemenata = duzina_niza - len(nova_lista)

print(nova_lista)
print(broj_izbacenih_elemenata)
