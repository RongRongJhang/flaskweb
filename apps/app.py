from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from apps.config import config

db = SQLAlchemy()
csrf = CSRFProtect()

login_manager = LoginManager()
login_manager.login_view = "auth.signup"
login_manager.login_message = ""


def create_app(config_key):
    app = Flask(__name__)

    # 會根據 .env 傳來的 "local" 參數到 config.py 載入相對應的配置
    app.config.from_object(config[config_key])

    login_manager.init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    Migrate(app, db)

    from apps.auth import views as auth_views
    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    return app
