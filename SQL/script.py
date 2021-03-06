#!/usr/bin/env python			Maria
# -*- coding: utf-8 -*-

def hash_func(password):
	import hashlib
	return hashlib.sha256(password).hexdigest()

import random
table = "hantverkare"
filename = table+".sql"
f = open(filename, 'w')
query = ""

kommunLista = ['Ale', 'Alingsås', 'Alvesta', 'Aneby', 'Arboga', 'Arjeplogs', 'Arvidsjaurs', 'Arvika', 'Askersunds', 'Avesta', 'Bengtsfors', 'Bergs', 'Bjurholms', 'Bjuvs', 'Bodens', 'Bollebygds', 'Bollnäs', 'Borgholms', 'Borlänge', 'Borås', 'Botkyrka', 'Boxholms', 'Bromölla', 'Bräcke', 'Burlövs', 'Båstads', 'Dals-Eds', 'Danderyds', 'Degerfors', 'Dorotea', 'Eda', 'Ekerö', 'Eksjö', 'Emmaboda', 'Enköpings', 'Eskilstuna', 'Eslövs', 'Essunga', 'Fagersta', 'Falkenbergs', 'Falköpings', 'Falu', 'Filipstads', 'Finspångs', 'Flens', 'Forshaga', 'Färgelanda', 'Gagnefs', 'Gislaveds', 'Gnesta', 'Gnosjö', 'Gotlands', 'Grums', 'Grästorps', 'Gullspångs', 'Gällivare', 'Gävle', 'Göteborgs', 'Götene', 'Habo', 'Hagfors', 'Hallsbergs', 'Hallstahammars', 'Halmstads', 'Hammarö', 'Haninge', 'Haparanda', 'Heby', 'Hedemora', 'Helsingborgs', 'Herrljunga', 'Hjo', 'Hofors', 'Huddinge', 'Hudiksvalls', 'Hultsfreds', 'Hylte', 'Håbo', 'Hällefors', 'Härjedalens', 'Härnösands', 'Härryda', 'Hässleholms', 'Höganäs', 'Högsby', 'Hörby', 'Höörs', 'Jokkmokks', 'Järfälla', 'Jönköpings', 'Kalix', 'Kalmar', 'Karlsborgs', 'Karlshamns', 'Karlskoga', 'Karlskrona', 'Karlstads', 'Katrineholms', 'Kils', 'Kinda', 'Kiruna', 'Klippans', 'Knivsta', 'Kramfors', 'Kristianstads', 'Kristinehamns', 'Krokoms', 'Kumla', 'Kungsbacka', 'Kungsörs', 'Kungälvs', 'Kävlinge', 'Köpings', 'Laholms', 'Landskrona', 'Laxå', 'Lekebergs', 'Leksands', 'Lerums', 'Lessebo', 'Lidingö', 'Lidköpings', 'Lilla Edets', 'Lindesbergs', 'Linköpings', 'Ljungby', 'Ljusdals', 'Ljusnarsbergs', 'Lomma', 'Ludvika', 'Luleå', 'Lunds', 'Lycksele', 'Lysekils', 'Malmö', 'Malung-Sälens', 'Malå', 'Mariestads', 'Marks', 'Markaryds', 'Melleruds', 'Mjölby', 'Mora', 'Motala', 'Mullsjö', 'Munkedals', 'Munkfors', 'Mölndals', 'Mönsterås', 'Mörbylånga', 'Nacka', 'Nora', 'Norbergs', 'Nordanstigs', 'Nordmalings', 'Norrköpings', 'Norrtälje', 'Norsjö', 'Nybro', 'Nykvarns', 'Nyköpings', 'Nynäshamns', 'Nässjö', 'Ockelbo', 'Olofströms', 'Orsa', 'Orusts', 'Osby', 'Oskarshamns', 'Ovanåkers', 'Oxelösunds', 'Pajala', 'Partille', 'Perstorps', 'Piteå', 'Ragunda', 'Robertsfors', 'Ronneby', 'Rättviks', 'Sala', 'Salems', 'Sandvikens', 'Sigtuna', 'Simrishamns', 'Sjöbo', 'Skara', 'Skellefteå', 'Skinnskattebergs', 'Skurups', 'Skövde', 'Smedjebackens', 'Sollefteå', 'Sollentuna', 'Solna', 'Sorsele', 'Sotenäs', 'Staffanstorps', 'Stenungsunds', 'Stockholms', 'Storfors', 'Storumans', 'Strängnäs', 'Strömstads', 'Strömsunds', 'Sundbybergs', 'Sundsvalls', 'Sunne', 'Surahammars', 'Svalövs', 'Svedala', 'Svenljunga', 'Säffle', 'Säters', 'Sävsjö', 'Söderhamns', 'Söderköpings', 'Södertälje', 'Sölvesborgs', 'Tanums', 'Tibro', 'Tidaholms', 'Tierps', 'Timrå', 'Tingsryds', 'Tjörns', 'Tomelilla', 'Torsby', 'Torsås', 'Tranemo', 'Tranås', 'Trelleborgs', 'Trollhättans', 'Trosa', 'Tyresö', 'Täby', 'Töreboda', 'Uddevalla', 'Ulricehamns', 'Umeå', 'Upplands Väsby', 'Upplands-Bro', 'Uppsala', 'Uppvidinge', 'Vadstena', 'Vaggeryds', 'Valdemarsviks', 'Vallentuna', 'Vansbro', 'Vara', 'Varbergs', 'Vaxholms', 'Vellinge', 'Vetlanda', 'Vilhelmina', 'Vimmerby', 'Vindelns', 'Vingåkers', 'Vårgårda', 'Vänersborgs', 'Vännäs', 'Värmdö', 'Värnamo', 'Västerviks', 'Västerås', 'Växjö', 'Ydre', 'Ystads', 'Åmåls', 'Ånge', 'Åre', 'Årjängs', 'Åsele', 'Åstorps', 'Åtvidabergs', 'Älmhults', 'Älvdalens', 'Älvkarleby', 'Älvsbyns', 'Ängelholms', 'Öckerö', 'Ödeshögs', 'Örebro', 'Örkelljunga', 'Örnsköldsviks', 'Östersunds', 'Österåkers', 'Östhammars', 'Östra Göinge', 'Överkalix', 'Övertorneå']
for j in kommunLista:
	#kommun = kommunLista[j]
	query = query + "INSERT INTO region VALUES('"+j+"');\n"


for i in range(100):
	k = str(i)
	phone = random.randint(1000000000,9999999999)
	password = hash_func("pass"+k)
	randRate = random.randint(1,6)
	randAntal = random.randint(0,30)

	query = query + "INSERT INTO "+table+" VALUES('user"+k+"@gmail.com', 'user"+k+"', "+str(phone)+", '"+password+"', 'Benkes bygg är en snickare fran Roslagen', 2, FALSE, "+str((randAntal*randRate))+", "+str(randAntal)+");\n"


	if i < 40:
		query = query + "INSERT INTO snickare VALUES('user"+k+"@gmail.com');\n"
	elif i < 48:
		query = query + "INSERT INTO snickare VALUES('user"+k+"@gmail.com');\n"
		query = query + "INSERT INTO barber VALUES('user"+k+"@gmail.com');\n"
	elif i < 50:
		query = query + "INSERT INTO snickare VALUES('user"+k+"@gmail.com');\n"
		query = query + "INSERT INTO barber VALUES('user"+k+"@gmail.com');\n"
		query = query + "INSERT INTO arborist VALUES('user"+k+"@gmail.com');\n"
		query = query + "INSERT INTO gardener VALUES('user"+k+"@gmail.com');\n"
	elif i < 60:
		query = query + "INSERT INTO barber VALUES('user"+k+"@gmail.com');\n"
	elif i < 70:
		query = query + "INSERT INTO arborist VALUES('user"+k+"@gmail.com');\n"
	elif i < 90:
		query = query + "INSERT INTO gardener VALUES('user"+k+"@gmail.com');\n"
	elif i < 100:
		query = query + "INSERT INTO snickare VALUES('user"+k+"@gmail.com');\n"
		query = query + "INSERT INTO barber VALUES('user"+k+"@gmail.com');\n"
		query = query + "INSERT INTO gardener VALUES('user"+k+"@gmail.com');\n"

"""
for k in range(200):
	randKom = random.randint(0,285)
	hantN = randKom%100
	kommun = str(kommunLista[randKom])
	query = query + "INSERT INTO operatingRegion VALUES('user"+str(hantN)+"@gmail.com', '"+kommun+"');\n"
"""

for k in range(100):
	randKom = random.randint(0,285)
	kommun = str(kommunLista[randKom])
	randKom1 = random.randint(0,285)
	if randKom1 == randKom:
		randkom1 = random.randint(0,285)
	kommun1 = str(kommunLista[randKom1])

	randKom2 = random.randint(0,285)
	if randKom2 == randKom or randKom2 == randKom1:
		randkom2 = random.randint(0,285)
	kommun2 = str(kommunLista[randKom2])

	randKom3 = random.randint(0,285)
	if randKom3 == randKom or randKom3 == randKom1 or randKom3 == randKom2:
		randKom3 = random.randint(0,285)
	kommun3 = str(kommunLista[randKom3])
	query = query + "INSERT INTO operatingRegion VALUES('user"+str(k)+"@gmail.com', '"+kommun+"');\n"
	query = query + "INSERT INTO operatingRegion VALUES('user"+str(k)+"@gmail.com', '"+kommun1+"');\n"	
	query = query + "INSERT INTO operatingRegion VALUES('user"+str(k)+"@gmail.com', '"+kommun2+"');\n"
	query = query + "INSERT INTO operatingRegion VALUES('user"+str(k)+"@gmail.com', '"+kommun3+"');\n"

f.write(query)


"""
filename = "yrken.sql"
f = open(filename, 'w')
query = ""
for i in range(100):	#Snickare, barber, arborist, garderner
	
	if i%3 = 0:
		query = query + "INSERT INTO snickare VALUES('user"+k+"@gmail.com');\n"
	if i%7 = 0:

	if i%9 = 0:

	else:



	x = random.randint(0,99)
	capacity = random.randint(1,4)
	k = str(i)
	query = query + "INSERT INTO "+table+" VALUES('car"+k+"', 'model"+k+"', 'color"+k+"', "+str(capacity)+", 'user"+str(x)+"@gmail.com');\n"
f.write(query)
"""

