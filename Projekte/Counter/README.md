## Störungs Counter

# Störungs Counter

Dieses Projekt ist ein einfacher Zähler für verschiedene Arten von Störungen (z. B. „technisch“ und „algemein“) mit grafischer Benutzeroberfläche (GUI) auf Basis von Python und Tkinter. Die gezählten Werte werden in einer SQLite-Datenbank gespeichert und können per Git synchronisiert werden.
zu beachten ist dabei das bei diesem program nur ein admin zur selben zeit arbeiten sollte da es sonst zu marge ereignissen kommt die das program "nicht alleine" lösen kann 

## Verzeichnisstruktur

- `stoerungs_counter.py` – Hauptdatei mit den GUI-Funktionen für Admin- und Viewer-Modus
- `under_funktions_main.py` – Alle Datenbank- und Hilfsfunktionen (z. B. Zähler aktualisieren, Labels updaten)
- `git_funktions.py` – Git-Funktionen zum Synchronisieren der Datenbankdatei
- `admin_start.py` – Startet das Programm im Admin-Modus (Zählen möglich)
- `viewer_start.py` – Startet das Programm im Viewer-Modus (nur Anzeige)
- `stoerungen.db` – SQLite-Datenbank mit den Zählerständen

## Voraussetzungen

- Python 3.x
- Die Pakete `tkinter` und `sqlite3` (bei Standard-Python meist schon enthalten)
- Git (für die Synchronisation der Datenbank)

## bei linux 

- könnte es nötig sein tkinter seperat zu instalieren 
(sudo apt install python3-tk)!


## Installation

1. Repository klonen oder herunterladen:
    ```sh
    git clone <REPO-URL>
    cd Counter
    ```

2. Stelle sicher, dass Python 3 installiert ist:
    ```sh
    python3 --version
    ```

3. (Optional) Virtuelle Umgebung anlegen:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

## Starten des Programms

### Admin-Modus (Zählen möglich)

Starte das Programm im Admin-Modus, um Störungen zu erfassen und zu zählen:

```sh
python3 admin_start.py
```

### Viewer-Modus (Nur Anzeige)

Starte das Programm im Viewer-Modus, um die aktuellen Zählerstände anzuzeigen:

```sh
python3 viewer_start.py
```

## Warum gibt es zwei Modi?

- **Admin-Modus:**  
  Hier können neue Störungen gezählt werden. Die Datenbank wird beim Start synchronisiert und Änderungen werden direkt gespeichert und per Git gepusht.
  soll immer nur von einer person genutzt werden bei wegsel des admin sollete manuel über das terminal geprüft werden ob alle daten korekt aktualisert wurden 

- **Viewer-Modus:**  
  Hier werden die aktuellen Zählerstände nur angezeigt. Die Datenbank wird regelmäßig per Git aktualisiert, aber es können keine Werte verändert werden.
  kann von vielen genutz werden ohne das es zu problehmen kommt

- **Folge:**
    das hat zu folge das eine marge strategie nicht nötig ist da dieser schwer um zusetzen ist 

**Fehlermeldungen:**
im terminal könnten fehler meldung auftretten wen:

-keine verbindung zu githaub besteht 
-ein marge konflickt auf getritten ist mit dem origin/main verzeichnis auf github 



## Fehlerbehandlung und Hinweise

- Bei gleichzeitiger Nutzung durch mehrere Admins kann es zu Git-Konflikten kommen, die manuell gelöst werden müssen.
- Bei Problemen mit Git (z. B. kein Remote `origin` oder kein Branch `main`) erscheinen Fehlermeldungen im Terminal.
- Unter Linux muss `tkinter` ggf. separat installiert werden:  
  `sudo apt install python3-tk`
- Das Programm ist plattformunabhängig und läuft unter Windows, macOS und Linux.
- das program ist erweiterbar was die störungsarten angeht in der under_funkttions_main.py !



