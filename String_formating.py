import re
s1 = '([<td class="nazev">Parcelní číslo:</td>, <td><a href="https://vdp.cuzk.cz/vdp/ruian/parcely/1797497608" rel="external" target="vdp" title="Informace o objektu z RÚIAN, externí odkaz">2773/1</a></td>, <td class="nazev">Obec:</td>, <td><a href="https://vdp.cuzk.cz/vdp/ruian/obce/577626" rel="external" target="vdp" title="Informace o objektu z RÚIAN, externí odkaz">Turnov [577626]</a></td>, <td class="nazev">Katastrální území:</td>, <td><a href="VyberKatastrInfo.aspx?encrypted=ia472NbH70PHO9A-OV5e4ibrIAYABhOsbIxbffnB44_n4NFFQJ6rZAwlcNDQ0TYOmbQB0wMO_5HYfTiuPmLR2B3kMojMLTxFphewi-iMMa50c4DLmCNivw==">Turnov [771601]</a></td>, <td class="nazev">Číslo LV:</td>, <td><a href="ZobrazObjekt.aspx?encrypted=Jj6gNsMEbov6CKFxiWLM0e1KFtH2hZVFnbViBKJeaVWw0NcIqQEFxeQ0PNbtmwVO-ERIztpcwZUyspLS-j-ZQ0jRB_AzgcKEQoYwtvIYEJIoK6yc5MVG3g==" title="Seznam nemovitostí na LV">7706</a></td>, <td class="nazev">Výměra [m<sup>2</sup>]:</td>, <td>816</td>, <td class="nazev">Typ parcely:</td>, <td>Parcela katastru nemovitostí</td>, <td class="nazev">Mapový list:</td>, <td>DKM</td>, <td class="nazev">Určení výměry:</td>, <td>Ze souřadnic v S-JTSK</td>, <td class="nazev">Druh pozemku:</td>, <td>zahrada</td>, <td>Kopal Petr, č. p. 257, 51101 Ohrazenice</td>, <td class="right"></td>, <td>zemědělský půdní fond</td>, <td>ochranné pásmo vodního zdroje 2.stupně</td>, <td><a alt="Odkaz na vysvětlení BPEJ" href="http://bpej.vumop.cz/55600">55600</a></td>, <td>816</td>, <td><a href="ZobrazObjekt.aspx?encrypted=nwCTc2u2YVqdpOdI72srgQuMjKlwKyOskbzS_6FLveaIQJBLa4EvJFhsFHG-vOZEwEpzRqH--Tvc7-NSvgntfbRaENA8WhQbwe0nhR1_fIo-g3XxaGVOGAWbECw3j8Wq">V-3183/2016</a></td>, <td>01.07.2016</td>])'
# regex = re.compile(r'>(.*)<')

# print(string.split(",", 1)[0])
# print(string.split("<td class="))
# adresa = string.split(",", 1)[1]
# print(string.lstrip())
#
# jedna cesta zatim nechám u ledu
# s1 = string.replace('<td class="nazev">', '')
# s2 = s1.replace('</td>','')
# s3 = s2.replace('<a href="https://vdp.cuzk.cz/vdp/ruian/', '')
# print(s3)

# celej string rozdělim timhle znakem na jednotlivý objekty
# print(string.split(", <"))
# for i in string.split(", "):
#     print(i)
# s1 = (string.split(", <")[1])

#pokus o implementace re
# s1 = 'input(<td><a href="https://vdp.cuzk.cz/vdp/ruian/parcely/1797497608" rel="external" target="vdp" title="Informace o objektu z RÚIAN, externí odkaz">73/1</a></td>)'
#
# s2 = re.compile(r'\d?\d?\d?\d/?\d?')
# s3 = s2.search(s1)
#
# print(s3.group())

# a teď každou tu solo část potřebuju okleštit o všechny expresions co začínají a končí "<"
# s2 = re.search(regex, s1)
print(s1)