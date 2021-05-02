from flask import Flask, render_template, request, redirect, url_for, flash
import os
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np

categories = ["Clothing_and_Accessories", "Software_Apparels"]
subCategories = {"Clothing_and_Accessories":["Mens_Accessories", "Mens_Clothing", "Kids_Clothing", "Womens_Accessories", "Womens_Bags"]
}
subCategoryData = {}


for data in subCategories["Clothing_and_Accessories"]:
    df = pd.read_csv(data+".csv")
    # print(df.shape)
    df = df.iloc[:, 1:]
    arr = np.array(df)
    subCategoryData[data] = arr
    # print(arr)

app = Flask(__name__)
app.secret_key = "Secret Key"

db_user = os.environ.get('DB_USER_mysql')
db_pass = os.environ.get('DB_PASS_mysql')


app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:"{db_pass}"@localhost/eCommerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def Catalogue():
    return render_template("index.html")