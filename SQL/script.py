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
for i in range(100):
	k = str(i)
	phone = random.randint(1000000000,9999999999)
	password = hash_func("pass"+k)
	query = query + "INSERT INTO "+table+" VALUES('user"+k+"@gmail.com', 'user"+k+"', "+str(phone)+", '"+password+"', 'Benkes bygg är en snickare fran Roslagen', 2);\n"

f.write(query)
