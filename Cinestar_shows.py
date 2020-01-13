import requests
from bs4 import BeautifulSoup

movie_name = "jumanji"
day = "1"
wanted_time_start = "13:00"
wanted_time_end = "21:50"

url = 'https://www.cinestar.cz/cz/opava/program'

site = requests.get(url)
site.raise_for_status()

site.encoding = site.apparent_encoding

soup = BeautifulSoup(site.text, features="lxml")

search = '#ctab' + day +  ' .odd'
search2 = '#ctab' + day +  ' .even'

movies = soup.select(search)
movies2 = soup.select(search2)
movie_names_odd = soup.select(search + ' .title')
movie_names_even = soup.select(search2 + ' .title')

for name_o, name_e in zip(movie_names_odd, movie_names_even):
    print(name_e.text.replace("DABING", "").replace("TITULKY", "").replace("CZ", ""))
    print(name_o.text.replace("DABING", "").replace("TITULKY", "").replace("CZ", ""))


'''movie_name = input("Jméno filmu: ")
day = input("Den: ")
wanted_time_start = input("Čas začátku: ")
wanted_time_end = input("Čas konce: ")'''

'''for name in movie_names_even:
    print(name.text)'''

orig_div = None
for movie in movies:
    if movie_name.lower() in movie.text.lower():
        orig_div = movie
        print(movie_name)

for movie in movies2:
    if movie_name.lower() in movie.text.lower():
        orig_div = movie
        print(movie_name)

import re

pattern = re.compile('^[0-2][0-9]:[0-5][0-9]$')
start_times = []

if orig_div:
    time_a = orig_div.select('a')
    detail = orig_div.select('.detail em')
    counter = 0
    endtimes = []

    for endtime in detail:
        if counter % 3 == 2:
            endtimes.append(endtime.text)
        if counter % 3 == 1:
            length = endtime.text
        counter += 1


    for obj, endtime in zip(time_a, detail):
        time = pattern.match(obj.text)

        try:
            start_times.append(time.group())
        except:
            pass

movie_name = movie_name.capitalize()

for i,j in zip(start_times, endtimes):
    if (int(wanted_time_start[0:2]) <= int(i[0:2]) and int(wanted_time_start[3:5]) <= int(i[3:5]) and int(wanted_time_end[0:2]) >= int(j[0:2])):
        result = movie_name + " začíná v " + i + " a končí v " + j + " jeho délka je " + length
        print(result)