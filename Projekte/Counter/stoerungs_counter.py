import tkinter as tk
from Projekte.Counter.git_functions import git_pull_db, git_push_db
from Projekte.Counter.under_functions_main import init_db, get_counter, get_counter_total, update_counter, update_labels
DB_PATH = "stoerungen.db"
Art_der_störung = ["technisch", "algemein"]

def beenden(root):
    """
    Beendet die Anwendung und führt einen Git-Push der Datenbank durch.
    Diese Funktion wird aufgerufen, wenn der Benutzer die Anwendung schließt.
    Sie stellt sicher, dass alle Änderungen in der Datenbank vor dem Beenden gespeichert werden.
    """
    git_push_db()  # Vor dem Beenden noch einmal pushen
    root.destroy()

def main_admin():
    """
    Hauptfunktion für die Admin-Ansicht des Störungs-Counters.
    Diese Funktion initialisiert die Datenbank, zieht die neuesten Änderungen von Git,
    und zeigt eine GUI an, in der Störungen gezählt werden können.
    """
    init_db()
    git_pull_db()   # DB beim Start als Admin sofort pullen
    git_push_db()   # und sofort pushen (z.B. falls lokale Änderungen)
    root = tk.Tk()
    root.title("Störungs Counter")
    root.attributes("-topmost", True)
    fenster_breite = 250
    fenster_hoehe = 200
    root.geometry(f"{fenster_breite}x{fenster_hoehe}+0+0")

    label = tk.Label(root, text="Fehlercounter für die Schulung", font=("Arial", 12, "bold"))
    label.pack(pady=10)


    button1 = tk.Button(root, text="technisch", command=lambda: [update_counter("technisch"), update_labels(counter_label, gesamt=True)])
    button1.pack(pady=5, fill='x', padx=10)

    button2 = tk.Button(root, text="algemein", command=lambda: [update_counter("algemein"), update_labels(counter_label, gesamt=True)])
    button2.pack(pady=5, fill='x', padx=10)

    button3 = tk.Button(root, text="beenden", command=lambda: beenden(root))
    button3.pack(pady=5, fill='x', padx=10)

    # Counter-Anzeige
    counter_label = tk.Label(root, text="", font=("Arial", 10))
    counter_label.pack(pady=10)

    update_labels(counter_label, gesamt=True)


    root.mainloop()

def main_view():
    """
    Hauptfunktion für die Anzeige des Störungs-Counters.
    Diese Funktion initialisiert die Datenbank, zieht die neuesten Änderungen von Git,
    und zeigt eine GUI an, die die aktuellen Störungen anzeigt.
    """
    init_db()
    root = tk.Tk()
    root.title("Störungs Counter (Anzeige)")
    root.attributes("-topmost", True)
    fenster_breite = 250
    fenster_hoehe = 180
    root.geometry(f"{fenster_breite}x{fenster_hoehe}+0+0")

    label = tk.Label(root, text="Fehlercounter für die Schulung", font=("Arial", 12, "bold"))
    label.pack(pady=10)

    counter_label = tk.Label(root, text="", font=("Arial", 10))
    counter_label.pack(pady=10)

    def periodic_pull():
        git_pull_db()
        update_labels(counter_label, gesamt=True)
        root.after(15000, periodic_pull)

    button3 = tk.Button(root, text="beenden", command=lambda: beenden(root))
    button3.pack(pady=5, fill='x', padx=10)

    update_labels(counter_label, gesamt=True)
    root.after(15000, periodic_pull)
    root.mainloop()



#fertig