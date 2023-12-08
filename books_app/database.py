import json
import os
from sqlalchemy import create_engine # we create engine for database to communicate with our appplication
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_DATABASE = "mysql+pymysql://"+os.getenv("DB_USERNAME")+":"+os.getenv("DB_PASSWORD")+"@"+os.getenv("DB_HOST")+"/"+os.getenv("DB_DATABASE")
 
engine = create_engine(URL_DATABASE, echo=True)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
Base = declarative_base()

POOL_SIZE = 20
POOL_RECYCLE = 3600
POOL_TIMEOUT = 15
MAX_OVERFLOW = 2
CONNECT_TIMEOUT = 60

# engine = create_engine(MSSQL_URL, pool_size=POOL_SIZE, pool_recycle=POOL_RECYCLE, pool_timeout=POOL_TIMEOUT, max_overflow=MAX_OVERFLOW)
engine = create_engine(URL_DATABASE)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

file = open(os.getcwd() + '/response_msg.json')
msg = json.load(file)


# # Create a Class that inherits from our class builder
# class SoftDeleteMixin(generate_soft_delete_mixin_class()):
#     # type hint for autocomplete IDE support
#     deleted_at:DateTime

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as ex:
        print("Error getting DB session : ", ex)
        return None
    finally:
        db.close()

def response(status, message, data):
    return {
        "status": status,
        "message": message,
        "data": data,
    }

