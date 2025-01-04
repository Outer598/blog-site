from flask import Flask, render_template
from model.blog import db
from routes.signup import userApi
from routes.login import loginApi
from routes.blogs import blogApi
from routes.search import searchApi
import flask_smorest
import pymysql
from dotenv import load_dotenv, dotenv_values
import os


load_dotenv()
config = dotenv_values(".env")

app = Flask(__name__)

pymysql.install_as_MySQLdb()
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{os.getenv("myDatabaseUsername")}:{os.getenv("myDatabasePassword")}@{os.getenv("myDatabaseHost")}/{os.getenv("myDatabaseName")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["API_TITLE"] = "Example API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/openapi"
app.config["OPENAPI_JSON_PATH"] = "openapi.json"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["OPENAPI_REDOC_PATH"] = "/redoc"
app.config["OPENAPI_REDOC_URL"] = "https://cdn.jsdelivr.net/npm/redoc/bundles/redoc.standalone.js"
api = flask_smorest.Api(app)

db.init_app(app)

api.register_blueprint(userApi)
api.register_blueprint(loginApi)
api.register_blueprint(blogApi)
api.register_blueprint(searchApi)



if __name__ == '__main__':
    app.run(debug=True)
