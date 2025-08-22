from app import app
import sqlite3

def get_connection():
    """_summary_

    Returns:
        _type_: _description_
    """    
    connection = sqlite3.connect(app.config["SQLITE_DATABASE_FILENAME"])
    connection.execute("PRAGMA foreign_keys=ON")
 
    return connection

def __execute_statement(sql, query_parameters = None, commit = False):
    """_summary_

    Args:
        sql (_type_): _description_
        query_parameters (_type_, optional): _description_. Defaults to None.
        commit (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """    
    try: 
        connection = get_connection()
        cursor = connection.cursor()    
        
        if query_parameters:
            result = cursor.execute(sql, query_parameters)
        else:
            result = cursor.execute(sql)

        return_value = result.fetchall()

        if commit:
            connection.commit()

        return return_value
    finally:
        connection.close()

def execute_select(sql, query_parameters = None):
    """_summary_

    Args:
        sql (_type_): _description_
        query_parameters (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """    
    try:
        return __execute_statement(sql, query_parameters)
    except:
        raise
        
def execute_change(sql, query_parameters = None):
    """_summary_

    Args:
        sql (_type_): _description_
        parameters (tuple, optional):  Defaults to None.

    Returns:
        _type_: _description_
    """    
    try: 
        return __execute_statement(sql, query_parameters, True)
    except:
        raise

