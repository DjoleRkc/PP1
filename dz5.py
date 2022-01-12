'''Napisati program koji vrši određenu obradu nad tekstualnom datotekom u Comma
Separated Values (.CSV) koja sadrži podatke o ATP teniskim mečevima u određenom
periodu prema prethodno opisanom formatu. Program treba da formira izlaznu datoteku
koja će za svakog tenisera odrediti tri najduža meča koja je igrao u zadatom periodu. Jedan
red izlazne datoteke treba da sadrži sledeća polja: string koji sadrži puno ime igrača
(player_name), listu sa dužinama tri najduža meča uređenu nerastuće po dužini meča i
razdvojenu znakom | (top_3_length), listu sa imenima protivničkih igrača u najdužim
mečevima razdvojenu znakom | u istom poretku kao u prethodnom polju
(top_3_length_opponents) i listu rezultata u obliku RRR, gde je R može biti W, ukoliko
je odgovarajući meč dobio, a L, ukoliko je izgubio, u istom poretku kao u prethodnom polju
(top_3_length_results). Ukoliko ima više protivničkih igrača sa istom najdužom
dužinom meča, ispisati ih po leksikografskom poretku, a najviše prva tri u listi. Izlazna
datoteka treba da bude u CSV formatu. U izlaznu datoteku na početku upisati zaglavlje. U
izlaznu datoteku ne upisivati podatke o igračima koji nisu odigrali barem tri meča u
periodu. Izlaznu datoteku urediti leksikografski rastuće prema imenu igrača.
Program treba da:
1) Učita imena ulazne i izlazne datoteke sa standardnog ulaza.
2) Učita dva datuma u formatu d.m koji predstavljaju vremenski period za koji se vrši
obrada. Svaki datum se unosi u posebnoj liniji teksta.
3) Izvrši zahtevanu obradu prema tekstu zadatka.
4) Formira izlaznu datoteku prema tekstu zadatka.
5) Vodi računa i obradi moguće izuzetke koji mogu nastati prilikom rada programa.
Ovakvo rešenje zadatka ne koristi csv i re module koji olakšavaju rad sa csv datotekama, pa je iz tog razloga malo komplikovanije. Za ovakvo rešavanje ovog zadatka potrebno je
izuzetno znanje metoda korišćenih za rešavanje prethodna 4 zadatka.
HVALA KOLEGINICI LANI JOVANOVIĆ NA USTUPLJENOM REŠENJU '''

def Sortiraj(recnik):
    finalRec = {}
    for i,val in recnik.items():
        list = sorted(val, key = lambda x: (-x[0],x[1]))
        recnik[i] = list[0:3]
        if len(recnik[i]) == 3:
            finalRec[i] = recnik[i]
    return finalRec


def upisi(f2,finalRec):
    with open(f2,"w") as file:
        file.write("player_name,top_3_length,top_3_length_opponents,top_3_length_results\n")
        for i, val in sorted(finalRec.items()):
            file.write("{},{}|{}|{},{}|{}|{},{}{}{}\n".format(i,val[0][0],val[1][0],val[2][0],val[0][1],val[1][1],val[2][1],val[0][2],val[1][2],val[2][2]))


def obrada(f1,f2,d1,m1,d2,m2):
    recnik = {}
    finalRec = {}
    try:
        with open(f1, "r") as file:
            niz = []
            file.readline()
            for line in file:
                niz = line.split(",")
                try:
                    m, d = int(niz[3][4:6]), int(niz[3][6:8])
                    float(niz[9])
                except:
                    print("PODACI_GRESKA")
                    break
                if (m < m2 and m > m1) or (m == m1 and d >= d1) or (m == m2 and d <= d2):
                    if niz[5] not in recnik:
                        recnik[niz[5]] = [(int(niz[18]), niz[11], "W")]
                    else:
                        recnik[niz[5]].append((int(niz[18]), niz[11], "W"))

                    if niz[11] not in recnik:
                        recnik[niz[11]] = [(int(niz[18]), niz[5], "L")]
                    else:
                        recnik[niz[11]].append((int(niz[18]), niz[5], "L"))
            finalRec = Sortiraj(recnik)
            upisi(f2, finalRec)
    except:
        print("DAT_GRESKA")


f1, f2 = input().split()
date= input().split(".")
d1, m1 = int(date[0]), int(date[1])
date= input().split(".")
d2, m2 = int(date[0]), int(date[1])
obrada(f1,f2,d1,m1,d2,m2)
