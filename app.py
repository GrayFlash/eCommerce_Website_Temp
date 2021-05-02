from flask import Flask, render_template, request, redirect, url_for, flash
import os
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np

noOfItems = 0

categories = ["Clothing_and_Accessories", "Software_Apparels"]
subCategories = {"Clothing_and_Accessories":["Mens_Accessories", "Mens_Clothing", "Kids_Clothing", "Womens_Accessories", "Womens_Bags"]
}
subCategoryData = {}
# category_img = ["images/clothing_accesories.jpg", "images/software_devices.jpg"]
category_img = ["https://www.shutterstock.com/image-vector/fashion-store-boutique-accessories-bags-footwear-786450895", "https://www.shutterstock.com/image-photo/business-devices-on-brown-wooden-desk-1373777756"]

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
    pass_data = []
    for i in range(len(categories)):
        name = categories[i]
        link = category_img[i]
        pass_data.append([name, link])
    return render_template("index.html", pass_data=pass_data, noOfItems=noOfItems)