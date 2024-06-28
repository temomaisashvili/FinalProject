import datetime



class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db"
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=1)
    FLASK_ADMIN_SWATCH = 'cerulean'
    FLASK_APP = 'app.py'
    SECRET_KEY = 'kandswhqoiehoqn2442ewjhrNDLJKD'