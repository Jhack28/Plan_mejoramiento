class Config:
    SECRET_KEY = "clave"
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:SENA123@localhost/Bibliot_DB"
    SQLALCHEMY_TRACK_MODIFICATIONS = False