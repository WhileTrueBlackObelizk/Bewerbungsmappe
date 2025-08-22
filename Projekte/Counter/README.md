# Counter

## Störungs-Counter

Dieses Projekt bietet eine einfache grafische Oberfläche (GUI) zum Zählen verschiedener Störungsarten (z. B. „technisch“ und „allgemein“) mit Python und Tkinter. Die Zählerstände werden in einer SQLite-Datenbank gespeichert und per Git synchronisiert. **Wichtig:** Das Programm sollte jeweils nur von einer Person im Admin-Modus genutzt werden, da parallele Nutzung zu Git-Konflikten führen kann, die manuell gelöst werden müssen.

## Verzeichnisstruktur

- `stoerungs_counter.py` – Hauptdatei mit den GUI-Funktionen für Admin- und Viewer-Modus
- `under_functions_main.py` – Alle Datenbank- und Hilfsfunktionen (z. B. Zähler aktualisieren, Labels updaten)
- `git_functions.py` – Git-Funktionen zum Synchronisieren der Datenbankdatei
- `admin_start.py` – Startet das Programm im Admin-Modus (Zählen möglich)
- `viewer_start.py` – Startet das Programm im Viewer-Modus (nur Anzeige)
- `stoerungen.db` – SQLite-Datenbank mit den Zählerständen

## Voraussetzungen

- Python 3.x
- Die Pakete `tkinter` und `sqlite3` (bei Standard-Python meist schon enthalten)
- Git (für die Synchronisation der Datenbank)

## Hinweise für Linux

- Es kann nötig sein, `tkinter` separat zu installieren:
  ```sh
  sudo apt install python3-tk
  ```

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
  Der Admin-Modus sollte immer nur von einer Person genutzt werden. Beim Wechsel des Admins sollte manuell über das Terminal geprüft werden, ob alle Daten korrekt aktualisiert wurden.

- **Viewer-Modus:**  
  Hier werden die aktuellen Zählerstände nur angezeigt. Die Datenbank wird regelmäßig per Git aktualisiert, aber es können keine Werte verändert werden.
  Der Viewer-Modus kann von mehreren Personen gleichzeitig genutzt werden, ohne dass es zu Problemen kommt.

- **Folge:**  
  Dadurch ist keine Merge-Strategie nötig, da diese schwer umzusetzen wäre.

**Fehlermeldungen:**  
Im Terminal können Fehlermeldungen auftreten, wenn:

- keine Verbindung zu GitHub besteht
- ein Merge-Konflikt mit dem `origin/main`-Branch auf GitHub aufgetreten ist

## Fehlerbehandlung und Hinweise

- Bei gleichzeitiger Nutzung durch mehrere Admins kann es zu Git-Konflikten kommen, die manuell gelöst werden müssen.
- Bei Problemen mit Git (z. B. kein Remote `origin` oder kein Branch `main`) erscheinen Fehlermeldungen im Terminal.
- Unter Linux muss `tkinter` ggf. separat installiert werden:  
  `sudo apt install python3-tk`
- Das Programm ist plattformunabhängig und läuft unter Windows, macOS und Linux.
- Das Programm ist erweiterbar, was die Störungsarten angeht (siehe `under_functions_main.py`).

