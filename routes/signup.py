from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_smorest import Blueprint as SmorestBlueprint
from flask.views import MethodView
from model.blog import *
from model.blog import db, Blog
import hashlib

user = Blueprint('user', __name__)
userApi = SmorestBlueprint('userApi', 'userApi', url_prefix='/api', description='API for Users')


@userApi.route('/create_users')
class UserApi(MethodView):

    def get(self):
        user_name = User.query.with_entities(User.user_name).all()
        print(user_name)
        return jsonify(user_name[0][0])
    
    def post(self):
        user_name = User.query.with_entities(User.user_name).all()
        data = request.form
        hash256 = hashlib.sha256()
        hash256.update(data['password'].encode('utf-8'))

        firstName = data['firstName']
        lastName = data['lastName']

        for i in user_name:
            if data['userName'] == i[0]:
                return jsonify({"message": "Username already exists"}), 400
            else:
                userName = data['userName']
            
        email = data['email']
        password = hash256.hexdigest()
        
        try:
            user = User(first_name=firstName, last_name=lastName, user_name=userName, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            return jsonify({"message": 'User created successfully'}), 201
        except Exception as e:
            db.session.rollback()
            error = str(e)
            return jsonify({"message": "Error Creating User", "error": error}),500