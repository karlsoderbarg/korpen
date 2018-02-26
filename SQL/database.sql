CREATE TABLE hantverkare (
	email VARCHAR(64) PRIMARY KEY,
	name VARCHAR(128) NOT NULL,
	phone NUMERIC,
	password VARCHAR(64) NOT NULL,
	presentation VARCHAR(256),
	antalAnstallda NUMERIC NOT NULL,
	is_admin BOOLEAN NOT NULL DEFAULT FALSE,
	ratingSum NUMERIC DEFAULT 0,
	antalRatings NUMERIC DEFAULT 0
);

CREATE TABLE snickare (
	email VARCHAR(128) PRIMARY KEY,
	FOREIGN KEY(email) REFERENCES hantverkare(email) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE barber (
	email VARCHAR(128) PRIMARY KEY,
	FOREIGN KEY(email) REFERENCES hantverkare(email) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE arborist (
	email VARCHAR(128) PRIMARY KEY,
	FOREIGN KEY(email) REFERENCES hantverkare(email) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE gardener (
	email VARCHAR(128) PRIMARY KEY,
	FOREIGN KEY(email) REFERENCES hantverkare(email) ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE region (
	name VARCHAR(256) PRIMARY KEY
);

CREATE TABLE operatingRegion (
	hantverkare VARCHAR(128) REFERENCES hantverkare(email) ON UPDATE CASCADE ON DELETE CASCADE,
	region VARCHAR(256) REFERENCES region(name) ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY(hantverkare,region),
	UNIQUE(hantverkare,region)
);



/* RATING måste vara ett annat bord som relaterar till en hantverkares mail och kunders betyg.
/* Lägg till profession som snickare:barber:arborist et cetera...


HUR SKA VI GÖRA MED STAD/PLATS/ verksamhetsområde?
Mata in en lista med alla sveriges landskap?
Kommuner? tätorter? Lanskap blir för stort antar jag.

Till en början kan de få specificera lite mer i sin egna 'presentation'.

*/



/*
CREATE TABLE projekt (
	hantverkare VARCHAR(128) REFERENCES person(email) ON UPDATE CASCADE ON DELETE CASCADE,
	client VARCHAR(128) REFERENCES person(email) ON UPDATE CASCADE ON DELETE CASCADE,
	proejktID NUMERIC PRIMARY KEY,

)

CREATE TABLE avslutadeProjekt (
	startDate TIMESTAMP,
	slutDate TIMESTAMP,
	proejktID NUMERIC PRIMARY KEY,
	client VARCHAR(128) REFERENCES user(email) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(proejktID,client) REFERENCES bid(proejktID,client) ON UPDATE CASCADE ON DELETE CASCADE

)

CREATE TABLE user (
	email VARCHAR(128) PRIMARY KEY,
	username VARCHAR(128) NOT NULL,
	isHantverkare BOOLEAN NOT NULL,

)
*/