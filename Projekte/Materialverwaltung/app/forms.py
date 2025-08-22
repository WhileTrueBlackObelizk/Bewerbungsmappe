from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField, StringField, DateField, TextAreaField
from wtforms.validators import InputRequired, NumberRange, Length
from wtforms.fields.html5 import DateField

from app import get_data_for_forms

class MitarbeiterFormular(FlaskForm):

    abteilungen = [("HR", "HR"), ("Sales", "Sales"), 
                   ("Hausmeisterei", "Hausmeisterei"), ("Geschäftsleitung", "Geschäftsleitung")]

    vorname         = StringField('vorname', validators=[InputRequired(), Length(min=2, max=100)])
    nachname        = StringField('nachname', validators=[InputRequired(), Length(min=2, max=100)])
    abteilung       = SelectField('abteilung', choices=abteilungen, validators=[InputRequired()])
    telefonnummer   = IntegerField('telefonnummer', validators=[InputRequired(), NumberRange(min=100, max=999)])
    submit          = SubmitField('Mitarbeiter anlegen')

#so? Regexp(r'^(\+49|0)\d{9,14}$', message="Bitte eine gültige deutsche Telefonnummer mit maximal 15 Ziffern angeben.")

class MaterialFormular(FlaskForm):

    typ                = StringField('typ', validators=[InputRequired(), Length(min=2, max=100)])
    seriennummer       = StringField('seriennummer', validators=[InputRequired(), Length(min=2, max=100)])
    kaufdatum          = DateField('kaufdatum', validators=[InputRequired()])
    submit             = SubmitField('Material anlegen')

# SQLAlchemy 

class MaterialausgabeFormular(FlaskForm):
    mitarbeiter     = SelectField('mitarbeiter', validators=[InputRequired()])
    material        = SelectField('material', validators=[InputRequired()])
    ausgabedatum    = DateField('ausgabedatum', validators=[InputRequired()])
    zustand        = TextAreaField('zustand', validators=[InputRequired()])
    submit          = SubmitField('Materialausgabe erfassen')
