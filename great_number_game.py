from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "SuperSecretYo"

@app.route('/')
def startGame():