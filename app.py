from flask import Flask, render_template, url_for, redirect, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os
from forms import *
from datetime import date


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY']= "adasfasf"

app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQLAlchemy(app)

Migrate(app,db)



class Blog(db.Model):

    __tablename__ = 'Blog'

    id = db.Column(db.Integer,primary_key=True)

    dat = db.Column(db.Text)

    title = db.Column(db.Text,nullable=False)

    short = db.Column(db.Text,nullable=False)

    breif = db.Column(db.Text,nullable=False)



    def __init__(self,title,short,breif,dat):

        self.title= title

        self.short = short

        self.breif = breif

        self.dat = dat

    def __repr__(self):

        return f"{self.id}"





@app.route('/')
def blogList():

    data = Blog.query.all()

    # data.sort(key = lambda x: -int(x[id]))

    return render_template("index.html",data = data)



@app.route('/add',methods = ['GET','POST'])
def add():

    form = Add()

    if form.validate_on_submit():

        title = form.title.data

        dat = form.dat.data.strftime("%Y-%m-%d")

        short = form.short.data

        breif = form.breif.data

        new_blog = Blog(title,short,breif,dat)

        db.session.add(new_blog)

        db.session.commit()

        print("commited")

        return render_template('view.html',blog = new_blog)

    else:

        print(form.errors)#for printing errors if form does not validate


    return render_template("add.html",form=form)

@app.route('/del',methods = ['GET','POST'])
def delete():

    form = Remove()

    i = request.args.get('delete')

    blog = Blog.query.get(i)


    if form.validate_on_submit():


        choice = form.choice.data

        if choice == 1:


            db.session.delete(blog)

            db.session.commit()

            return redirect(url_for('blogList'))

        else:

            return redirect(url_for('blogList'))
    else:

        print(form.errors)

    return render_template('delete.html',form = form,blog  = blog)


@app.route('/view')
def view():


    i = request.args.get('view')

    blog = Blog.query.get(i)

    return render_template('view.html',blog = blog)



@app.route('/edit',methods=['GET','POST'])
def edit():


    form = Edit()

    i = request.args.get('edit')

    blog = Blog.query.get(i)
    # print(blog.title)


    if request.method == "POST":


        if form.validate_on_submit():


            print(form.title.data)

            blog.title = form.title.data

            blog.dat = form.dat.data.strftime("%Y-%m-%d")

            blog.short = form.short.data

            blog.breif = form.breif.data

        # new_blog = Blog(title, short, breif, dat)
        # db.session.add(new_blog)
            db.session.commit()
            print("commited")
            return render_template('view.html',blog = blog)

    elif request.method == "GET":



        print("not validate")

        form.title.data = blog.title

        form.short.data = blog.short

        form.breif.data = blog.breif

        y,m,d = list(map(int,blog.dat.split("-")))

        form.dat.data = date(y,m,d)
        # print(date(y,m,d))


    return render_template("edit.html", form=form)

if __name__ == '__main__':


    app.run(debug=True,port=5000)
