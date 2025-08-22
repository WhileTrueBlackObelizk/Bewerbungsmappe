import sqlite3
from flask import render_template, request

from app import app
from app import forms
from app import get_data_for_forms

if app.config["DATABASE_TYPE"] == "mysql":
    from app import db_mysql as db
else:
    from app import db_sqlite as db


def get_employees_with_material():
    """

    Returns: 
        list: Liste der Mitarbeiter-IDs von Mitarbeitern, die gerade Material in ihrem Besitz haben
    """
    mitarbeiterlist2 = list()
    try:
        rows = db.execute_select("SELECT DISTINCT mitarbeiter_id FROM Materialausgabe m LEFT JOIN Materialrueckgabe mr ON mr.ausgabe_id = m.id WHERE mr.id IS NULL ")
        for row in rows:
            mitarbeiterlist2.append(row[0])
        return mitarbeiterlist2
    except:
        pass

    """
    Unübersichtliche, schwer veständliche Lösung in einem Statement: 
        SELECT
        m.id,
        m.vorname,
        m.nachname,
        CASE
            WHEN EXISTS (
            SELECT 1
            FROM Materialausgabe a
            LEFT JOIN Materialrueckgabe r ON a.id = r.ausgabe_id
            WHERE a.mitarbeiter_id = m.id AND r.id IS NULL
            )
            THEN 0
            ELSE 1
        END AS has_material
        FROM Mitarbeiter m;
    """


class Mitarbeiter:
    def __init__(self, id, vorname, nachname, abteilung, telefonnummer, has_material = False):
        self.id             = id
        self.vorname        = vorname
        self.nachname       = nachname
        self.abteilung      = abteilung
        self.telefonnummer  = telefonnummer
        self.has_material   = has_material

    def get_telefonnummer(self):
        return self.telefonnummer
    
    def get_has_material(self):
        return self.has_material

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/mitarbeiter')
def mitarbeiter(): # Ändern
    """_summary_

    Returns:
        _type_: _description_
    """    
    employees_with_material = get_employees_with_material()
    
    mitarbeiter = list()
    try: 
        mit = db.execute_select("SELECT id, vorname, nachname, abteilung, telefonnummer FROM Mitarbeiter ORDER BY nachname ")
        for ma in mit:
            has_material = ma[0] in employees_with_material
            mitarbeiter.append( # OBJEKT-RELATIONALES MAPPING
                Mitarbeiter(ma[0], ma[1], 
                            ma[2], ma[3], 
                             ma[4], has_material))
        return render_template("mitarbeiter.html", alle_mitarbeiter=mitarbeiter)
    except:
        # TODO: Exception behandeln
        pass

@app.route('/impressum')
def impressum():
    return render_template("impressum.html")

@app.route('/view_employee/<employee_id>')
def view_employee(employee_id):




    sql = "SELECT id, vorname, nachname, abteilung, telefonnummer FROM Mitarbeiter WHERE id = ?"
    try:
        ma = db.execute_select(sql, (employee_id,)) 
        employee = Mitarbeiter(ma[0], ma[1], 
                            ma[2], ma[3], 
                             ma[4])
        return render_template("view_employee.html", employee=employee)
    except Exception as e:
        return render_template("error.html")

@app.route('/material')
def material():
    """Route zur Materialseite. Auflistung des existierenden Materials.
    Returns:
        str: gerendertes HTML-Template, entweder Materialliste oder Fehlermeldung
    """    
    try: 
        material = db.execute_select("SELECT id, typ, seriennummer, kaufdatum  FROM Material")
        return render_template("material.html", material=material)
    except Exception as e:
            if app.config["ENVIRONMENT"] == "dev": # TODO Auslagern in eine externe Funktion, sowas wie is_developement()
                return e
            else:
                return render_template("error.html")

@app.route('/create_employee', methods=['POST', 'GET'])
def create_employee():
    # wir brauchen hier das Formular-Objekt, um es ans Template übergeben zu können
    form = forms.MitarbeiterFormular()
    if form.validate_on_submit():
        a            = form.vorname.data
        b            = form.nachname.data
        c            = form.abteilung.data
        d            = form.telefonnummer.data

        sql = "INSERT INTO Mitarbeiter (vorname, nachname, abteilung, telefonnummer) VALUES (?, ?, ?, ?)"
        try:
            db.execute_change(sql, (a, b, c, d))
        except Exception as e:
            return render_template("error.html")
        else: 
            return render_template("success.html")
    return render_template("create_employee.html", formular=form)


@app.route('/create_material', methods=['POST', 'GET'])
def create_material():
    # wir brauchen hier das Formular-Objekt, um es ans Template übergeben zu können
    form = forms.MaterialFormular()
    if form.validate_on_submit():
        a            = form.typ.data
        b            = form.seriennummer.data
        c            = form.kaufdatum.data

        sql = "INSERT INTO material (typ, seriennummer, kaufdatum) VALUES (?, ?, ?) RETURNING *"
        try:
            inserted = db.execute_change(sql, (a, b, c))
        except Exception as e:

            return render_template("error.html")
        else: 
            return render_template("success.html", inserted = inserted)
    return render_template("create_material.html", formular=form)

@app.route('/material_ausgabe', methods=['POST', 'GET'])
def material_ausgabe():
    form = forms.MaterialausgabeFormular()
    #TODO Was machen wir, wenn eine der Listen oder beide leer sind? 
    form.mitarbeiter.choices = get_data_for_forms.get_employee_data()
    form.material.choices    = get_data_for_forms.get_material_data()
    if form.mitarbeiter.choices is None or form.material.choices is None:
        return render_template("error.html")
    
    if form.validate_on_submit():

        a        = form.mitarbeiter.data
        b        = form.material.data
        c        = form.ausgabedatum.data
        d        = form.zustand.data

        sql = "INSERT INTO Materialausgabe (mitarbeiter_id, material_id, ausgabedatum, zustand) VALUES (?, ?, ?, ?) RETURNING *"
        try:
            db.execute_change(sql, (a, b, c, d))
        except Exception as e:
            return render_template("error.html")

        else:
            return render_template("success.html")
    return render_template("material_ausgabe.html", formular=form)

@app.route('/material_rueckgabe/<ma_id>')
def material_rueckgabe(ma_id):

    sql = f"""SELECT Material.id, Material.typ, Material.seriennummer, Materialausgabe.zustand, Mitarbeiter.vorname, Mitarbeiter.nachname FROM Materialausgabe JOIN
      Material ON Materialausgabe.material_id = Material.id 
      JOIN Mitarbeiter ON Mitarbeiter.id = Materialausgabe.mitarbeiter_id
      WHERE mitarbeiter_id = ?"""

    try:
        material_des_mitarbeiters= db.execute_select(sql, (ma_id,))
        if len(material_des_mitarbeiters) == 0:
            return render_template("no_material.html", ma= ma_id)

    except Exception as e:
        # TODO: Aufräumen. error-Template anzeigen!
        return str(e) + " " + ma_id
        return render_template("error.html") # Ändern mit komma arbeiten dopplung von return meiden return render_template("error.html"), str(e) + " " + ma_id 
    else: 
        return render_template("material_rueckgabe_2.html", material=material_des_mitarbeiters)
    

@app.route('/configtest')
def configtest():
    return app.config["MYSQL_USERNAME"]