import re

cuzk = 'Informace o pozemku | Nahlížení do katastru nemovitostí Přeskočit na obsah | Přeskočit na navigaci Nahlížení do katastru nemovitostí Hlavní navigace Parcela Stavba Jednotka Právo stavby Řízení Mapa LV Kat. území Probíhá zpracování ... Informace o pozemku Ukázka mapy se zobrazenou nemovitostí Parcelní číslo:2773/1 Obec:Turnov [577626] Katastrální území:Turnov [771601] Číslo LV:7706 Výměra [m2]:816 Typ parcely:Parcela katastru nemovitostí Mapový list:DKM Určení výměry:Ze souřadnic v S-JTSK Druh pozemku:zahrada Sousední parcely Vlastníci, jiní oprávnění Vlastnické právoPodíl Kopal Petr, č. p. 257, 51101 Ohrazenice Způsob ochrany nemovitosti Název zemědělský půdní fond ochranné pásmo vodního zdroje 2.stupně Seznam BPEJ BPEJ Výměra 55600 816 Omezení vlastnického práva Nejsou evidována žádná omezení. Jiné zápisy Nejsou evidovány žádné jiné zápisy. Řízení, v rámci kterých byl k nemovitosti zapsán cenový údaj V-3183/201601.07.2016 Více informací k cenovým údajů naleznete v nápovědě k aplikaci. Nemovitost je v územním obvodu, kde státní správu katastru nemovitostí ČR vykonává Katastrální úřad pro Liberecký kraj, Katastrální pracoviště SemilyZobrazené údaje mají informativní charakter. Platnost k 11.04.2020 21:00:00. Koupit el. listinu Výpis z KN (LV) Cena 50,- Kč/A4 Částečný výpis z KN (LV) Cena 50,- Kč/A4 Informace o pozemku Cena 50 Kč/A4 Kopie katastrální mapy Cena 50 Kč/A4 © 2004 - 2020 Český úřad zeměměřický a katastrální , Pod sídlištěm 1800/9, Kobylisy, 18211 Praha 8Podání určená katastrálním úřadům a pracovištím zasílejte přímo na jejich e-mail adresu.Uživatelská podpora: https://helpdesk.cuzk.cz, tel. +420 284 044 455 Verze aplikace: 5.6.1 build 0 Prohlášení o přístupnosti Podmínky užívání aplikace'


parcela = re.compile(r'Parcelní číslo:\d+\S?\d+')
obec = re.compile(r'Obec:\w+')
katastr = re.compile(r'Katastrální území:\w+')
lvcislo = re.compile(r'LV:\d+')
vymera = re.compile(r'Výměra \[m2\]:\d+')
druhpozemku = re.compile(r'Druh pozemku:\w+')
# obec1 = obec.search(cuzk)
# obec1 = obec.findall(cuzk)
# print(obec1.group())

# obec1 = obec.search(cuzk)
# obec1 = obec.findall(cuzk)
print((parcela.search(cuzk)).group())
print((obec.search(cuzk)).group())
print((katastr.search(cuzk)).group())
print((lvcislo.search(cuzk)).group())
print((vymera.search(cuzk)).group())
print((druhpozemku.search(cuzk)).group())
