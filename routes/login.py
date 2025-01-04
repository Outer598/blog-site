from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_smorest import Blueprint as SmorestBlueprint
from flask.views import MethodView
from model.blog import *
from model.blog import db, Blog
import hashlib


login = Blueprint('login', __name__)
loginApi = SmorestBlueprint('loginApi', 'loginApi', url_prefix='/api', description='API for Users')


@loginApi.route('/login')
class LoginApi(MethodView):
    def get(self):
        data = request.form

        hash256 = hashlib.sha256()
        hash256.update(data['password'].encode('utf-8'))
        hashed_password = hash256.hexdigest()

        user = User.query.filter_by(user_name=data['userName']).first()
        if user == None:
            return jsonify({"message": "User Name Not Found"}), 404
        
        if user.password == hashed_password:
            return jsonify({"message": "Login Succesfully"}), 200
        else:
            return jsonify({"message": "Invalid Password"}), 401
