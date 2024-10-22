from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from sqlalchemy.orm import Session
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
from models.users import init_models, User, db

app = Flask(__name__)
app.config['SECRET_KEY'] = '26bf39c0b5f2ea242dc806f7af06a8449cbb8a54ffcb78e83a11489e85ca3fe8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
init_models(app)


@login_manager.user_loader
def load_user(user_id):
    with Session(db.engine) as session:
        return session.get(User, int(user_id))


@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/painel')
@login_required
def painel():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('painel.html', title='Dashboard', username=current_user.username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=False)  # Adiciona parametro remember=True
            # flash('Autenticado com sucesso!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Usuário ou senha inválido. Verifique novamente', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout feito com sucesso', 'sucess')
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registro realizado com sucesso! Por favor, realize o login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.errorhandler(404)
def page404(error):
    # Página não encontrada
    return render_template('page404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)