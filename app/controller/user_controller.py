from flask import render_template
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, Usuario


def index():
    return render_template('index.html')


bp = Blueprint('user', __name__)

@bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombres = request.form.get('nombres')
        apellidos = request.form.get('apellidos')
        email = request.form.get('email')
        password = request.form.get('password')
        usuario = Usuario(contraseña=password, email=email)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('user.registro'))
    return render_template('registro.html')

