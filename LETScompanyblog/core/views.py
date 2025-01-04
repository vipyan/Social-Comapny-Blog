#core/views.py
from flask import render_template, request, Blueprint
from LETScompanyblog.models import BlogPost

core = Blueprint('core', __name__)

@core.route('/')
def index():
    pages = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=pages, per_page=5)
    return render_template('index.html', blog_posts=blog_posts)


    return render_template('index.html')

@core.route('/info')
def info(): 
    
    return render_template('info.html')