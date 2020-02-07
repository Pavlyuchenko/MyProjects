'''
Prvni uloha z Matematicke Olympiady kat. P
http://mo.mff.cuni.cz/p/69/p1.pdf

    Mame za ukol spocitat moznosti vyjiti schodu pri zadane vysce jednoho kroku a listu vsech schodu.

    Zaciname na nultem schode, ktery není zahrnut ve funkci pocet_kroku

'''

def pocet_kroku(schody, krok, vysky_schodu): # Pro zacatecni schod ("Nulty" schod) zavola pro kazdou moznost funkci pokus
    reseni = 0 # Pocet reseni
    curr_dist = 0 # Jak velky krok jsme udelali

    for i in range(len(vysky_schodu)): # Pro kazde i v listu vysky_schodu
        curr_dist += vysky_schodu[i] # Zvysi jak velky krok jsme usli

        if curr_dist > krok: # Pokud jsme udelali vetsi krok nez je povoleno, vyjede ze smycky
            break

        reseni += pokus(krok, vysky_schodu, i, 1) # Pro kazdou moznost zvysi reseni

    return reseni # Vrati vysledek


def pokus(krok, schody, curr_schod,first_run=False):

    reseni = 0
    curr_dist = 0

    for i in range(curr_schod+1, len(schody)):
        curr_dist += schody[i]

        if curr_dist > krok:
            break

        reseni += pokus(krok, schody, i, first_run+1)

    if curr_schod == len(schody)-1:
        reseni += 1

    if schody[curr_schod] == 4:
        print("----")
    return reseni

print(pocet_kroku(4, 100, [20, 30, 50, 30]))
