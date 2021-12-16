import copy
def ucitaj_red(broj_kolona):
    if broj_kolona == 0:
        exit()
    slova_u_vrsti = input().split(" ")
    red = []
    for k in range(len(slova_u_vrsti)):
        red.append(slova_u_vrsti[k])
    return red


def ucitaj_matricu(broj_redova, broj_kolona):
    matrica = []
    for j in range(broj_redova):
        matrica.append(ucitaj_red(broj_kolona))
    return matrica

temp = input()
broj_redova = temp[0]
broj_kolona = temp[2]
broj_redova = int(broj_redova)
broj_kolona = int(broj_kolona)
if broj_redova < 1 or broj_kolona < 1:
    exit(0)
matrica = ucitaj_matricu(broj_redova, broj_kolona)

def istampaj_matricu(matrica):
    for red in matrica:
        for j in range(len(red)):
            e = '\n' if j == len(red) - 1 else " "
            print(red[j], end=e)


def obrada(broj_redova, broj_kolona, matrica, matrica_kopija):
    for el in range(0, broj_redova):
        for m in range(0, broj_kolona):
            brojac_suseda_belog = 0
            if el == 0:
                nulta_vrsta = True
                poslednja_vrsta = False
            elif el == broj_redova - 1:
                nulta_vrsta = False
                poslednja_vrsta = True
            else:
                nulta_vrsta = False
                poslednja_vrsta = False

            if m == 0:
                nulta_kolona = True
                poslednja_kolona = False
            elif m == broj_kolona - 1:
                nulta_kolona = False
                poslednja_kolona = True
            else:
                nulta_kolona = False
                poslednja_kolona = False
            if not nulta_vrsta and broj_redova > 1:  # provera da li ima el iznad
                if matrica[el - 1][m] == "w":
                    brojac_suseda_belog += 1
            if not nulta_kolona and broj_kolona > 1:  # provera da li ima el levo
                if matrica[el][m - 1] == "w":
                    brojac_suseda_belog += 1
            if not poslednja_vrsta and broj_redova > 1:  # provera da li ima el ispod
                if matrica[el + 1][m] == "w":
                    brojac_suseda_belog += 1
            if not poslednja_kolona and broj_kolona > 1:  # provera da li ima el desno
                if matrica[el][m + 1] == "w":
                    brojac_suseda_belog += 1
            if not nulta_vrsta and not nulta_kolona and broj_redova > 1 and broj_kolona > 1:  # provera da li ima el gore levo
                if matrica[el - 1][m - 1] == "w":
                    brojac_suseda_belog += 1
            if not nulta_vrsta and not poslednja_kolona and broj_redova > 1 and broj_kolona > 1:  # provera da li ima el gore desno
                if matrica[el - 1][m + 1] == "w":
                    brojac_suseda_belog += 1
            if not nulta_kolona and not poslednja_vrsta and broj_redova > 1 and broj_kolona > 1:  # provera da li ima el dole levo
                if matrica[el + 1][m - 1] == "w":
                    brojac_suseda_belog += 1
            if not poslednja_vrsta and not poslednja_kolona and broj_redova > 1 and broj_kolona > 1:  # provera da li ima el dole desno
                if matrica[el + 1][m + 1] == "w":
                    brojac_suseda_belog += 1
            if matrica[el][m] == "w":
                if not (brojac_suseda_belog == 2 or brojac_suseda_belog == 3):
                    matrica_kopija[el][m] = "b"
            else:
                if brojac_suseda_belog == 3:
                    matrica_kopija[el][m] = "w"

    istampaj_matricu(matrica_kopija)
    return None

matrica_kopija = copy.deepcopy(matrica)
obrada(broj_redova, broj_kolona, matrica, matrica_kopija)



