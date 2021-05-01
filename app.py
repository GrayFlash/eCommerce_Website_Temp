from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "Secret Key"


@app.route('/')
def Catalogue():
    return render_template("index.html")