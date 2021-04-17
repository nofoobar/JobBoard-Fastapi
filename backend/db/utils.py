import databases
from db.session import SQLALCHEMY_DATABASE_URL


async def check_db_connected():
    try:
        if not str(SQLALCHEMY_DATABASE_URL).__contains__("sqlite"):
            database = databases.Database(SQLALCHEMY_DATABASE_URL)
            if not database.is_connected:
                await database.connect()
                await database.execute("SELECT 1")
        print("Database is connected (^_^)")
    except Exception as e:
        print(
            "Looks like db is missing or is there is some problem in connection,see below traceback"
        )
        raise e


async def check_db_disconnected():
    try:
        if not str(SQLALCHEMY_DATABASE_URL).__contains__("sqlite"):
            database = databases.Database(SQLALCHEMY_DATABASE_URL)
            if database.is_connected:
                await database.disconnect()
        print("Database is Disconnected (-_-) zZZ")
    except Exception as e:
        raise e
