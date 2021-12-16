nova_lista = []
#broj_elemenata = int(input())
#for j in range(0, broj_elemenata):
    #element_liste = int(input())
    #lista_brojeva.append(element_liste)
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
#if len(nova_lista) == 0:
    #print("Nova lista je prazna. ", nova_lista)
#else:
    #print("Nova lista je: ", nova_lista)

#print("Broj izbacenih elemenata je: ", broj_izbacenih_elemenata)