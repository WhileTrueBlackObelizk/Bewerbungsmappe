CREATE TABLE Mitarbeiter (
id INTEGER PRIMARY KEY AUTOINCREMENT,
abteilung TEXT NOT NULL,
telefonnummer TEXT
, vorname TEXT NOT NULL DEFAULT "NO NAME GIVEN", nachname TEXT NOT NULL DEFAULT "NO NAME GIVEN");
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE Material (
id INTEGER PRIMARY KEY AUTOINCREMENT,
typ TEXT NOT NULL,
seriennummer TEXT NOT NULL, -- warum nicht unique?
kaufdatum DATE
, zustand TEXT);
CREATE TABLE Materialausgabe (
id INTEGER PRIMARY KEY AUTOINCREMENT,
mitarbeiter_id INTEGER NOT NULL,
material_id INTEGER NOT NULL,
ausgabedatum DATE NOT NULL, zustand TEXT,
FOREIGN KEY (mitarbeiter_id) REFERENCES Mitarbeiter(id),
FOREIGN KEY (material_id) REFERENCES Material(id)
);
CREATE TABLE Materialrueckgabe (
id INTEGER PRIMARY KEY AUTOINCREMENT,
ausgabe_id INTEGER NOT NULL UNIQUE,
rueckgabedatum DATE NOT NULL,
FOREIGN KEY (ausgabe_id) REFERENCES Materialausgabe(id)
);
