from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_smorest import Blueprint as SmorestBlueprint
from flask.views import MethodView
from model.blog import *
import requests

blogs = Blueprint('blogs', __name__)
blogApi = SmorestBlueprint('blogApi', 'blogApi', url_prefix='/api', description='API for blogs')

# @blogs.route('/blogs')
# def home():
#     return render_template('index.html')


@blogApi.route('/blogs')
class BlogApi(MethodView):

    def get(self):
        blogs = Blog.query.order_by(Blog.created_at.desc()).all()
        blog_list = []

        for blog in blogs:
            author = Blog.query.join(User, Blog.user_id == User.id).filter(Blog.id == blog.id).with_entities(User.user_name, User.last_name, User.first_name).first()
            authorName = author[1].title() + ' ' + author[2].title() + '-' + author[0] 
            blog_list.append({"id": blog.id,"title": blog.title, "synopsis": blog.synopsis, "content": blog.content, "created_at": blog.created_at, "Author": authorName})
    
        return jsonify(blog_list), 200

    def post(self):
        data = request.form
        if data['title'] == '' or data['synopsis'] == '' or data['content'] == '':
            return jsonify({"message":'Title or Content cannot be empty'}), 400
        
        try:
            blog = Blog(title=data['title'], synopsis=data['synopsis'], content=data['content'], user_id=1)
            db.session.add(blog)
            db.session.commit()
            return jsonify({"message": 'Blog created successfully'}), 201
        except Exception as e:
            db.session.rollback()
            error = str(e)
            return jsonify({"message": "Error Creating Blog", "error": error}),500
        
@blogApi.route('/blogs/<int:id>')
class UDblog(MethodView):
    def patch(self, id):
        data = request.form
        blog = Blog.query.filter_by(id=id).first()
        if blog == None:
            return jsonify({"message": "Blog Not Found"}), 404
        
        try:
            for key, value in data.items():
                if hasattr(blog, key):
                    setattr(blog, key, value)
            db.session.commit()
            return jsonify({"message": "Blog Updated Successfully"}), 200
        except Exception as e:
            db.session.rollback()
            error = str(e)
            return jsonify({"message": "Error Updating Blog", "error": error}),500  
        
    def delete(self, id):
        blog = Blog.query.filter_by(id=id).first()
        if blog == None:
            return jsonify({"message": "Blog Not Found"}), 404
        
        try:
            db.session.delete(blog)
            db.session.commit()
            return jsonify({"message": "Blog Deleted Successfully"}), 200
        except Exception as e:
            db.session.rollback()
            error = str(e)
            return jsonify({"message": "Error Deleting Blog", "error": error}),500
    