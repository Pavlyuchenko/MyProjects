
def catalogTheOldMess(names, owned, city, comment, years): # vraci slovnik, tzn. typ Dict
    dicti = dict()
    for i in range(len(names)):
        dicti[names[i]] = CityPin(names[i], owned[i], city[i], comment[i], years[i])

    return dicti


class CityPin:
    def __init__(self, name, owned, city, comment, year):
        self.name = name
        self.owned = owned
        self.city = city
        self.comment = comment
        self.year = year

    def how_old(self, year):
        return year - self.year

    def __repr__(self):
        return self.name + " | " + str(self.owned) + " | " + str(self.city) + " | " + str(self.comment) + " | " + str(self.year)

    def __str__(self):
        return self.name + " (" + str(self.year) + ")"

# verejne testy


test1_names = ["Brnensky orloj", "Ericsson Globe", "Fnatic"]
test1_owned = [True, False, True]
test1_city = ["Brno", "Stockholm", "Jonkoping"]
test1_comment = ["Tez znamy jako Onderkuv pomnik", "", "DreamHack Winter"]
test1_year = [2019, 2016, 2013]

catalog = catalogTheOldMess(test1_names, test1_owned, test1_city, test1_comment, test1_year)

print(catalog)
for key in sorted(catalog.keys()):
    print(catalog[key])
    print(catalog[key].how_old(2042))

# Predchozi radky by meli generovat nasledujici vystup
"""
{'Brnensky orloj': Brnensky orloj | True | Brno | Tez znamy jako Onderkuv pomnik | 2019, 'Ericsson Globe': Ericsson Globe | False | Stockholm |  | 2016, 'Fnatic': Fnatic | True | Jonkoping | DreamHack Winter | 2013}
Brnensky orloj (2019)
23
Ericsson Globe (2016)
26
Fnatic (2013)
29
"""

# tvoje testy: todo :)


