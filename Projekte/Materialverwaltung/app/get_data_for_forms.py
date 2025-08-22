from app import app

if app.config["DATABASE_TYPE"] == "mysql":
    from app import db_mysql as db
else:
    from app import db_sqlite as db

def get_employee_data():
    """Gibt alle Mitarbeiter geordnet nach ihrem Nachnamen zurück (als Liste von Tupeln).

        Die Tupel, die jeweils einen Mitarbeiter repräsentieren, sehen folgendermaßen aus:
        (id, "vorname nachname - abteilung").
        
        Returns:
            list: Alle Mitarbeiter als Liste von Tupeln.
    """
    sql = "SELECT id, vorname, nachname, abteilung FROM Mitarbeiter ORDER BY nachname"
    try: 
        rows = db.execute_select(sql)
        alle_mitarbeiter = list()
        for row in rows:
            alle_mitarbeiter.append( (row[0], f"{row[1]} {row[2]} - {row[3]}") )
        return alle_mitarbeiter
    except Exception as e:#
        return None

def get_material_data():
    """Gibt die matterialien zurück, die noch nicht ausgegeben oder bereits zurückgegeben 
        wurden (als Liste von Tupeln)
        Diese werden z.B. in einem dropdwon menue im formular "materialausgabe" benoetigt.
        
        Die Tupel, die jeweils ein Material (z.B. Gerät) repräsentieren, sehen folgendermaßen aus:
        (id, "typ - seriennummer").
        
    Returns:
        list[Tupel(int, str)]: Alle verfügbaren Materialien als Liste von Tupeln.
    """    
    sql = """
        SELECT mat.id, mat.typ, mat.seriennummer
        FROM Material mat
        WHERE mat.id NOT IN (
        SELECT ma.material_id
        FROM Materialausgabe ma
        LEFT JOIN Materialrueckgabe mr ON ma.id = mr.ausgabe_id
        WHERE mr.id IS NULL)
        """
    try:
        rows = db.execute_select(sql)
        material = list()
        for row in rows:
            material.append( (row[0], f"{row[1]} - {row[2]}" ))
        return material
    except Exception as e:#
        return None


