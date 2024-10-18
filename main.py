from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = "hello"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/painel')
def home():
    return render_template('painel.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['nm']
        session['user'] = user
        return redirect(url_for('user'))
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logout com sucesso!', 'info')
    return redirect(url_for('login'))

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        flash(f'Hello, {user}.', 'info')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)