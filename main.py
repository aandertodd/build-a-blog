from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(2000))

    def __init__(self, title, body):
        self.title = title
        self.body = body


# main blog page url
@app.route('/blog', methods=['GET', 'POST'])
def index():

    # POST requests
    if request.method == 'POST':

        # get user input
        blog_title = request.form['new_blog_title']
        blog_body = request.form['new_blog_body']
        new_post = Blog(blog_title, blog_body)


        title_error = ''
        body_error = ''

        # submit it to database

        if blog_title == '':
            title_error = 'danggg man'
            blog_title = ''


        if blog_body == '':
            blog_body_error = 'danggg'
            blog_body = ''

            return render_template('newpost.html', blog_body_error=body_error, blog_title_error=title_error)
        else:

            db.session.add(new_post)
            db.session.commit()
        # put new entry into database



    # retrieve all entries from database
    blog_posts = db.session.query(Blog)

    return render_template('blog.html', blog_posts=blog_posts)

@app.route('/blog')
def blog_list():
    return render_template('blog.html')



@app.route('/newpost', methods=['GET'])
#if request.method == 'POST':
def new_post():
    return render_template('newpost.html')






    # new_blog_title = request.form['new_blog_title']
    # new_blog_body = request.form['new_blog_body']
    # new_entry_title = Blog(new_blog_title)
    # new_entry_body = Blog(new_blog_body)
    # db.session.add_all()
    # db.session.commit()

@app.route('/blog?id={{blog.id}}')
def blog_view():
    return render_template('blogview.html')


# # add blog page url
# @app.route('/newpost', methods=['GET', 'POST'])
# def new_post():
#
#     return render_template('newpost.html')
#
#
#
# new blog url (query param string)
#
#



if __name__ == '__main__':
    app.run()
