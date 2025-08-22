import pytest
from app import app

@pytest.fixture()
def client():
    app.config['testing'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    return app.test_client()

@pytest.fixture()
def runner():
    return app.test_cli_runner()

def test_request_index(client):
    response = client.get("/index")
    assert b"<h1>Mitarbeiter-Liste</h1>" in response.data

def test_request_index_dorothee(client):
    response = client.get("/index")
    assert b'''        <tr>
            <td>
                <a href="/material_rueckgabe/8">8</a>
            </td>
            <td>
                Dorothee''' in response.data


def test_request_root(client):
    response = client.get("/")
    assert b"<h1>Mitarbeiter-Liste</h1>" in response.data

def test_request_material(client):
    response = client.get("/material")
    assert b"""        <tr>
            <td>
                1
            </td>
            <td>
                Laptop
            </td>
            <td>
                100001
            </td>
            <td>
                2025-01-01
            </td>
        </tr>""" in response.data

def test_add_user(client):
    response = client.post("/create_employee", 
        data={"vorname": "Hubertus",
        "nachname": "Schmidt",
        "telefonnummer": "12",
        "abteilung": "HR"}, follow_redirects=True)
    assert response.status_code == 200
    
def test_add_material(client):
    response = client.post("/create_material", 
        data={"typ": "Korkenziehe",
        "seriennummer": "777555333",
        "kaufdatum": "2025-01-01"}, follow_redirects=True)
    assert response.status_code == 200

# TODO Tests für alle Routen


def test_material_ausgabe(client):
    response = client.post("/material_ausgabe",
    data={"mitarbeiter" :"8", 
        "material" : "34",
        "ausgabedatum" : "2025-01-01", "zustand": "gut"}, follow_redirects=True)
    assert response.status_code == 200
    #assert b"Eingabe erfolgreich" in response.data

