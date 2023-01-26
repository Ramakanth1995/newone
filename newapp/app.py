from flask import Flask, render_template, request, redirect,json, jsonify,url_for,flash
from database import db, Products
#from flask_login import LoginManager,login_user,logout_user,login_required,logout_user,current_user
import os
from sqlalchemy import func
import pandas as pd
import streamlit as st
import plotly.express as px
from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
todo = ''
previews_amount = 0
@app.before_first_request
def create_table():
    db.create_all()


@app.route('/', methods=["GET",'POST'])
def group_data():

    group_data = db.session.query(Products.category, func.sum(Products.total_amount)).group_by(Products.category).all()
    print(group_data)

    df = pd.DataFrame(group_data,
                      columns=['Name', 'Total'])
    print(df)

    col = ['Violet','Indigo','Blue','Green','Yellow','Orange','Pink','red']

    fig = px.bar(df, x='Name', y='Total', color='Name',color_discrete_sequence = col, barmode='group')

    # Create graphJSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('icon.html', productlist=group_data,graphJSON=graphJSON)

@app.route('/products', methods=["GET",'POST'])
def products():

    if request.method == "POST":
        todo.category = request.form['category']
        todo.paid_amount = int(request.form['paid_amount'])
        todo.remaning_amount = int(request.form['total_amount'])-int(todo.paid_amount)
        todo.total_amount = request.form['total_amount']

        if int(request.form['total_amount'])<int(request.form['paid_amount']):
            flash('Login successful')
            exit()
        db.session.add(todo)
        db.session.commit()


        productlist = Products.query.all()

        return render_template('amount.html', productlist=productlist)

    productlist = Products.query.all()

    sum_of_total_price = 0
    balance_amount = 0

    for i in productlist:
        sum_of_total_price = sum_of_total_price+i.total_amount

        balance_amount = balance_amount+i.paid_amount

    bal_am = sum_of_total_price-balance_amount


    group_data = db.session.query(Products.category,func.sum(Products.total_amount)).group_by(Products.category).all()

    #return render_template('icon.html', productlist=group_data)

    return render_template('amount.html',productlist = productlist,sum_of_total_price=sum_of_total_price,balance_amount = bal_am)

@app.route('/edit', methods=["GET",'POST'])
def edit():

    if request.method == "POST":
        id = request.form['id']

        name = request.form['name']
        paid_amount = request.form['paid_amount']
        remaning_amount = request.form['remaning_amount']
        total_amount = request.form['total_amount']
        productlist = Products.query.all()
        global todo
        todo = Products.query.filter_by(id=id).first()
        print(todo)
        return render_template('edit_page.html', productlist=todo)
    return render_template('amount.html', productlist=todo)


@app.route('/add', methods=["GET",'POST'])
def add():
    if request.method == "POST":
        name = request.form['name']
        category = request.form['category']
        paid_amount = request.form['paid_amount']
        remaning_amount =int(request.form['total_amount']) - int(request.form['paid_amount'])
        total_amount = request.form['total_amount']

        todo = Products(name=name,category=category, paid_amount=paid_amount, remaning_amount=remaning_amount, total_amount=total_amount)

        db.session.add(todo)
        db.session.commit()

        productlist = Products.query.all()

        return render_template('amount.html', productlist=productlist)
    else:

        return render_template('add_new.html')


    productlist = Products.query.all()

    return render_template('amount.html', productlist=productlist)


app.run(host='localhost', port=5000,debug=True)