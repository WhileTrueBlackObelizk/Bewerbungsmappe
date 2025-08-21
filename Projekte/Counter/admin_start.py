import tkinter as tk
from stoerungs_counter import main_admin

if __name__ == "__main__":
    """Hauptfunktion für die Admin-Ansicht des Störungs-Counters.
    Diese Funktion initial
    isiert die Datenbank, zieht die neuesten Änderungen von Git,
    und zeigt eine GUI an, die die aktuellen Störungen anzeigt und ermöglicht,
    Störungen zu aktualisieren.
    """
    main_admin()

    # fertig