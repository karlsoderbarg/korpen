CREATE TABLE hantverkare (
	email VARCHAR(64) PRIMARY KEY,
	name VARCHAR(128) NOT NULL,
	phone NUMERIC,
	password VARCHAR(64) NOT NULL,
	presentation VARCHAR(256),
	antalAnstallda NUMERIC NOT NULL,
	is_admin BOOLEAN NOT NULL DEFAULT FALSE,
	ratingSum NUMERIC,
	antalRatings NUMERIC
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


/* RATING måste vara ett annat bord som relaterar till en hantverkares mail och kunders betyg.
/* Lägg till profession som snickare:barber:arborist et cetera...

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