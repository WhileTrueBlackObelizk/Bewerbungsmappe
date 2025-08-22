from app import app
import mysql.connector

def get_connection():

    """_summary_

    Returns:
        _type_: _description_
    """    
    mydb = mysql.connector.connect(
        host = app.config["MYSQL_HOST_IP"],
        user = app.config["MYSQL_USERNAME"],
        password = app.config["MYSQL_PASSWORD"],
        database = app.config["MYSQL_DATABASE"]
    )
    return mydb

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
        cursor = connection.cursor(prepared=True)    
        
        if query_parameters:
            cursor.execute(sql, query_parameters)
        else:
            cursor.execute(sql)

        return_value = cursor.fetchall()

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

