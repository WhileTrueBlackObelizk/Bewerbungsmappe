PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE Mitarbeiter (
id INTEGER PRIMARY KEY AUTOINCREMENT,
abteilung TEXT NOT NULL,
telefonnummer TEXT
, vorname TEXT NOT NULL DEFAULT "NO NAME GIVEN", nachname TEXT NOT NULL DEFAULT "NO NAME GIVEN");
INSERT INTO Mitarbeiter VALUES(1,'Sales','123','Horst','Maier');
INSERT INTO Mitarbeiter VALUES(2,'HR','400','Ilse','Fuß');
INSERT INTO Mitarbeiter VALUES(3,'HR','100','Kurt','Schmidt');
INSERT INTO Mitarbeiter VALUES(4,'Hausmeisterei','101','Franz','Speck');
INSERT INTO Mitarbeiter VALUES(5,'Buchhaltung','890','Anneliese','Friedrich');
INSERT INTO Mitarbeiter VALUES(6,'HR','12','Gerhard','Schröder');
INSERT INTO Mitarbeiter VALUES(7,'HR','4','Bernhard','Karsubke');
INSERT INTO Mitarbeiter VALUES(8,'Hausmeisterei','13','Dorothee','Bär');
INSERT INTO Mitarbeiter VALUES(9,'Hausmeisterei','1','Friedrich','Merz');
INSERT INTO Mitarbeiter VALUES(12,'Sales','14','Captain','Kirk');
INSERT INTO Mitarbeiter VALUES(15,'Hausmeisterei','3','Hans','Hansen');
INSERT INTO Mitarbeiter VALUES(16,'Sales','10','Annemarie','Schnabel');
INSERT INTO Mitarbeiter VALUES(24,'HR','3','Anneliese','Schmidt');
INSERT INTO Mitarbeiter VALUES(25,'Hausmeisterei','12','Hannelore','Kohl');
INSERT INTO Mitarbeiter VALUES(26,'Hausmeisterei','12','Hannelore','Kohl');
INSERT INTO Mitarbeiter VALUES(27,'HR','12','Hubertus','Schmidt');
INSERT INTO Mitarbeiter VALUES(28,'HR','12','Hubertus','Schmidt');
INSERT INTO Mitarbeiter VALUES(29,'HR','12','Hubertus','Schmidt');
INSERT INTO Mitarbeiter VALUES(30,'HR','12','Hubertus','Schmidt');
INSERT INTO Mitarbeiter VALUES(31,'HR','12','Hubertus','Schmidt');
INSERT INTO Mitarbeiter VALUES(32,'HR','238','Bernhard','Karsubke');
INSERT INTO Mitarbeiter VALUES(33,'HR','122','Marianne','Meyer');
INSERT INTO Mitarbeiter VALUES(34,'Hausmeisterei','400','Hermann','Hermann');
INSERT INTO Mitarbeiter VALUES(35,'Hausmeisterei','400','Hermann','Hermann');
INSERT INTO Mitarbeiter VALUES(36,'Hausmeisterei','400','Hermann','Hermann');
INSERT INTO Mitarbeiter VALUES(37,'Sales','435','Franziskus','von Schwarzach');
INSERT INTO Mitarbeiter VALUES(38,'Hausmeisterei','444','Martha','Argerich');
CREATE TABLE Material (
id INTEGER PRIMARY KEY AUTOINCREMENT,
typ TEXT NOT NULL,
seriennummer TEXT NOT NULL, -- warum nicht unique?
kaufdatum DATE
, zustand TEXT);
INSERT INTO Material VALUES(1,'Laptop','100001','2025-01-01',NULL);
INSERT INTO Material VALUES(2,'Maus','100002','2025-01-01',NULL);
INSERT INTO Material VALUES(3,'Laptop','100003','2025-01-01',NULL);
INSERT INTO Material VALUES(4,'Monitor','100003','2025-01-01',NULL);
INSERT INTO Material VALUES(5,'Graftiktablet','900-900-1','2025-05-26',NULL);
INSERT INTO Material VALUES(6,'Monitor','34909-93490394','2025-01-16',NULL);
INSERT INTO Material VALUES(7,'Aktenvernichter','Vernichter-2000','2025-04-03',NULL);
INSERT INTO Material VALUES(17,'Tastatur','123','2025-04-01',NULL);
INSERT INTO Material VALUES(18,'Korkenzieher','42','2025-05-01',NULL);
INSERT INTO Material VALUES(19,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(20,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(21,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(22,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(23,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(24,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(25,'Mac Mini','438','2025-05-01',NULL);
INSERT INTO Material VALUES(26,'Mac Mini','438','2025-05-01',NULL);
INSERT INTO Material VALUES(27,'Mac Mini','438','2025-05-01',NULL);
INSERT INTO Material VALUES(28,'Mac Mini','500','2025-05-01',NULL);
INSERT INTO Material VALUES(29,'Mac Mini','500','2025-05-01',NULL);
INSERT INTO Material VALUES(30,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(31,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(32,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(33,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(34,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(35,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(36,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(37,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(38,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(39,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(40,'Schlüssel','101','2023-07-01',NULL);
INSERT INTO Material VALUES(41,'Schlüssel','101','2023-07-01',NULL);
INSERT INTO Material VALUES(42,'Schlüssel','101','2023-07-01',NULL);
INSERT INTO Material VALUES(43,'Schlüssel','25002','2025-06-05',NULL);
INSERT INTO Material VALUES(44,'Schlüssel','25002','2025-06-05',NULL);
INSERT INTO Material VALUES(45,'Schlüssel','25002','2025-06-05',NULL);
INSERT INTO Material VALUES(46,'Schlüssel','25003','2025-06-05',NULL);
INSERT INTO Material VALUES(47,'Schlüssel','25003','2025-06-05',NULL);
INSERT INTO Material VALUES(48,'Schlüssel','25003','2025-06-05',NULL);
INSERT INTO Material VALUES(49,'Schlüssel','25003','2025-06-05',NULL);
INSERT INTO Material VALUES(50,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(51,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(52,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(53,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(54,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(55,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(56,'Korkenziehe','777555333','2025-01-01',NULL);
INSERT INTO Material VALUES(57,'Schlüssel','25003','2025-06-05',NULL);
INSERT INTO Material VALUES(58,'Schlüssel','25003','2025-06-05',NULL);
INSERT INTO Material VALUES(59,'iPhone','543','2025-06-04',NULL);
INSERT INTO Material VALUES(60,'iPhone','543','2025-06-04',NULL);
INSERT INTO Material VALUES(61,'Konzertflügel','8954','2025-06-05',NULL);
INSERT INTO Material VALUES(62,'Kartoffelpresse','43','2025-06-24',NULL);
INSERT INTO Material VALUES(63,'Kaffeetasse','345','2025-06-24',NULL);
CREATE TABLE Materialausgabe (
id INTEGER PRIMARY KEY AUTOINCREMENT,
mitarbeiter_id INTEGER NOT NULL,
material_id INTEGER NOT NULL,
ausgabedatum DATE NOT NULL, zustand TEXT,
FOREIGN KEY (mitarbeiter_id) REFERENCES Mitarbeiter(id),
FOREIGN KEY (material_id) REFERENCES Material(id)
);
INSERT INTO Materialausgabe VALUES(1,1,1,'2025-05-01','wie neu');
INSERT INTO Materialausgabe VALUES(2,15,6,'2025-05-22','fast wie neu für den Herrn Hansen');
INSERT INTO Materialausgabe VALUES(3,3,7,'2025-05-22','jaha');
INSERT INTO Materialausgabe VALUES(4,2,2,'2025-05-07','sehr gute maus');
INSERT INTO Materialausgabe VALUES(5,9,4,'2025-05-15','a');
INSERT INTO Materialausgabe VALUES(8,12,5,'2025-05-22','asef');
INSERT INTO Materialausgabe VALUES(10,1,3,'2025-05-14','sjdfkjsdf');
INSERT INTO Materialausgabe VALUES(12,2,1,'2025-02-02','gut');
INSERT INTO Materialausgabe VALUES(13,8,34,'2025-01-01','gut');
INSERT INTO Materialausgabe VALUES(14,8,29,'2025-06-04','hjkhakjsdhfasd');
INSERT INTO Materialausgabe VALUES(15,34,40,'2025-06-24','Ausgezeichnet, wie neu');
INSERT INTO Materialausgabe VALUES(16,35,41,'2025-06-24','Ausgezeichnet, wie neu');
CREATE TABLE Materialrueckgabe (
id INTEGER PRIMARY KEY AUTOINCREMENT,
ausgabe_id INTEGER NOT NULL UNIQUE,
rueckgabedatum DATE NOT NULL,
FOREIGN KEY (ausgabe_id) REFERENCES Materialausgabe(id)
);
INSERT INTO Materialrueckgabe VALUES(1,1,'2025-02-02');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('Mitarbeiter',38);
INSERT INTO sqlite_sequence VALUES('Material',63);
INSERT INTO sqlite_sequence VALUES('Materialausgabe',16);
INSERT INTO sqlite_sequence VALUES('Materialrueckgabe',1);
COMMIT;
