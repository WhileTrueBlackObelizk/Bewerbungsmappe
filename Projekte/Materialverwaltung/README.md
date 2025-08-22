# materialverwaltung

## Konfiguration: 

In der Datei ```config.toml``` sind folgende Konfigurations-Einstellungen möglich: 

### allgemeine Konfiguration

```DATABASE_TYPE``` - Datenbanktyp, derzeit entweder ```mysql``` oder ```sqlite``` <br>
* Wird ```mysql``` gewählt, müssen die mit ```MYSQL``` beginnenden Einstellungen gesetzt werden, um eine Verbindung zur mysql-Datenbank aufzubauen.
* ACHTUNG: Die Konfigurationsvariable `MYSQL_PASSWORD` muss in der Datei /etc/MATERIAL_CONFIG/credentials.toml gesetzt sein, die Datei muss existieren! Bei Fragen zum Anlegen dieser Datei wenden Sie sich bitte an Ihren Systemadministrator!
* Wird ```sqlite``` gewählt, muss die Konfigurationsvariable ```SQLITE_DATABASE_FILENAME``` gesetzt werden. 

```ENVIRONMENT``` - Umgebung, derzeit entweder ```dev``` (Entwicklungsumgebung) oder ```prod``` (Produktivumgebung). 

* Hat Einfluss auf die im Frontend angezeigten Fehlermeldungen. Im prod-Environment werden nur generelle Fehlerseiten angezeigt, im ```dev```-Environment detaillierte Fehlermeldungen vom flask-Server.

### mysql-Konfiguration

```MYSQL_HOST_IP```

```MYSQL_USERNAME```




## Zum Starten:
flask --app materialverwaltung run --debug
