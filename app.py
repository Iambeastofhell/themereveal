from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def hello():
      return render_template('index.html')

@app.route('/mystery')
def ans():
      return render_template('ans.html')