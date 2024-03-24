from flask import Flask, render_template, redirect, session, request
import datetime
import random

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    # var1 = [request.form['farm', 'cave', 'house']]
    if request.form['action'] == 'farm':
        earn = random.randint(10, 20)
        session['gold'] += earn
        session['activities'].append(f'<li class="green">Earned {earn} golds at the farm! ({datetime.datetime.now()})</li>')
    elif request.form['action'] == 'cave':
        earn = random.randint(5, 10)
        session['gold'] += earn
        session['activities'].append(f'<li class="green">Earned {earn} golds at the cave! ({datetime.datetime.now()})</li>')
    elif request.form['action'] == 'house':
        earn = random.randint(2, 5)
        session['gold'] += earn 
        session['activities'].append(f'<li class="green">Earned {earn} golds at the house! ({datetime.datetime.now()})</li>')
    elif request.form['action'] == 'casino':
        earn = random.randint(-50, 50)
        session['gold'] -= earn 
        session['activities'].append(f'<li class="red"> Entered a casino and lost {earn} golds... ouch.. ({datetime.datetime.now()})</li>')
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy():
    session.clear()
    return redirect('/') 
 
 

if __name__ == '__main__':
    app.run(debug=True)

