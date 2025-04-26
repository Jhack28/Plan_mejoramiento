from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Usuario
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('user', __name__)

@bp.route('/register', methods=['POST'])
def register():
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    correo = request.form['correo']
    contraseña = request.form['contraseña']

    if Usuario.query.filter_by(correo=correo).first():
        flash('El correo ya está registrado, inicia sesión.', 'error')
        return redirect(url_for('index'))

    hash_contraseña = generate_password_hash(contraseña)
    nuevo_usuario = Usuario(nombres=nombres, apellidos=apellidos, correo=correo, contraseña=hash_contraseña)
    db.session.add(nuevo_usuario)
    db.session.commit()
    flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
    return redirect(url_for('index'))

@bp.route('/login', methods=['POST'])
def login():
    correo = request.form['correo']
    contraseña = request.form['contraseña']
    usuario = Usuario.query.filter_by(correo=correo).first()

    if usuario and check_password_hash(usuario.contraseña, contraseña):
        flash('Login exitoso', 'success')
        return redirect(url_for('user.perfil'))
    else:
        flash('Correo o contraseña incorrectos. Regístrate si no tienes cuenta.', 'error')
        return redirect(url_for('index'))

@bp.route('/perfil')
def perfil():
    return render_template('perfil.html')

def index():
    return render_template('index.html')
