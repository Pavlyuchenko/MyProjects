'''
Prvni uloha z Matematicke Olympiady kat. P
http://mo.mff.cuni.cz/p/69/p1.pdf

    Mame za ukol spocitat moznosti vyjiti schodu pri zadane vysce jednoho kroku a listu vsech schodu.

    Zaciname na nultem schode a pokazde muzeme udelat krok rovny maximalne promenne krok. Nasim ukolem je najit vsechny moznosti k dosazeni posledniho schodu v listu schody[].

    Autor: Michal Pavlíček
'''

def pocet_kroku(pocet_schodu, krok, schody, curr_schod=0): # pocet_schodu = n; krok = d; schody = h1...hn
    reseni = 0 # Pocet vsech reseni
    curr_dist = 0 # Dosavadni vyska naseho kroku

    for i in range(curr_schod+1, len(schody)): # Pro i v rozsahu od momentalniho schodu + 1 az do delky schodu
        curr_dist += schody[i] # Zvys dosavani vysku kroku

        if curr_dist > krok: # Pokud jsme prekrocili vysku kroku, nepokracuj dal a rozbij smycku
            break

        reseni += pocet_kroku(pocet_schodu, krok, schody, i) # Rekurzivně zavolej tuto funkci s parametrem momentalniho schodu a jeji return pricti k promenne reseni

    if curr_schod == len(schody)-1: # Pokud jsme se dostali az nakonec, zvetsi reseni o jedno
        reseni += 1

    return reseni # Vrat reseni


print(pocet_kroku(4, 100, [155]))
