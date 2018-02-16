#!/usr/bin/env python
# -*- coding: utf-8 -*-

def hash_func(password):
	import hashlib
	return hashlib.sha256(password).hexdigest()

import random
table = "hantverkare"
filename = table+".sql"
f = open(filename, 'w')
query = ""
query2 = ""
query3 = ""
query4 = ""
query5 = ""
for i in range(100):
	k = str(i)
	phone = random.randint(1000000000,9999999999)
	password = hash_func("pass"+k)
	query = query + "INSERT INTO "+table+" VALUES('user"+k+"@gmail.com', 'user"+k+"', "+str(phone)+", '"+password+"', 'Benkes bygg är en snickare fran Roslagen', 2, FALSE, 0, 0);\n"


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


f.write(query)

