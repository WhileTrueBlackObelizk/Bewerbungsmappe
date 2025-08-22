import pytest
from app import get_data_for_forms
import sqlite3

def test_get_employee_data():
    #fnuktion abrufen
    result = get_data_for_forms.get_employee_data()
    # prüfen, ob der eingefügte mitarbeiter im egebnis enthalten ist
    # das ergebnis ist eine Liste von Tupeln: (id,vorname nchname - Ateilung")
    assert ((15, "Hans Hansen - Hausmeisterei")) in result