from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_smorest import Blueprint as SmorestBlueprint
from flask.views import MethodView
from model.blog import *

search = Blueprint('search', __name__)
searchApi = SmorestBlueprint('searchApi', 'searchApi', url_prefix='/api', description='API for Users')


@searchApi.route('/search')
class Searchapi(MethodView):
    def get(self):
        search = request.args.get('search')

        blogs_title = Blog.query.join(User, Blog.user_id == User.id).filter(Blog.title.like(f'%{search}%')).all()
        blogs_firstName = Blog.query.join(User, Blog.user_id == User.id).filter(User.first_name.like(f"%{search}%")).all()
        blogs_lastName = Blog.query.join(User, Blog.user_id == User.id).filter(User.last_name.like(f"%{search}%")).all()
        blogs_userName = Blog.query.join(User, Blog.user_id == User.id).filter(User.user_name.like(f"%{search}%")).all()
        
        blog_list = []
        blogs = blogs_title + blogs_firstName + blogs_lastName + blogs_userName

        for blog in blogs:
            authorName = blog.user.first_name.title() + ' ' + blog.user.last_name.title() + '-' + blog.user.user_name
            item  = {"id": blog.id, "title": blog.title, "synopsis": blog.synopsis, "content": blog.content, "created_at": blog.created_at, "Author": authorName}
            blog_list.append(item)
            
        return jsonify(blog_list), 200