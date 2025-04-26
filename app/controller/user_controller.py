from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import db, Usuario
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('user', __name__)

#controllers de usuario

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
    flash('Registro exitoso en la base de datos. Ahora puedes iniciar sesión.', 'success')
    return redirect(url_for('index'))

@bp.route('/login', methods=['POST'])
def login():
    correo = request.form['correo']
    contraseña = request.form['contraseña']
    usuario = Usuario.query.filter_by(correo=correo).first()

    if usuario and check_password_hash(usuario.contraseña, contraseña):
        session['usuario_id'] = usuario.ID
        flash('Inicio de sesión exitoso, bienvenido usuario', 'success')
        return redirect(url_for('user.perfil'))
    else:
        flash('Correo o contraseña incorrectos. Regístrate si no tienes cuenta.', 'error')
        return redirect(url_for('index'))


@bp.route('/perfil')
def perfil():
    if 'usuario_id' not in session:
        flash('Debes iniciar sesión para ver tu perfil.', 'error')
        return redirect(url_for('index'))
    usuario = Usuario.query.get(session['usuario_id'])
    return render_template('perfil.html', usuario=usuario)

def index():
    return render_template('index.html')


#controllers perfil

@bp.route('/logout', methods=['POST'])
def logout():
    session.pop('usuario_id', None)
    flash('Sesión cerrada correctamente.', 'success')
    return redirect(url_for('index'))

@bp.route('/delete_account', methods=['POST'])
def delete_account():
    user_id = session.get('usuario_id')
    if user_id:
        usuario = Usuario.query.get(user_id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            session.pop('usuario_id', None)
            flash('Tu cuenta ha sido eliminada.', 'success')
    return redirect(url_for('index'))



@bp.route('/change_password', methods=['POST'])
def change_password():
    user_id = session.get('usuario_id')
    if not user_id:
        flash('Debes iniciar sesión.', 'error')
        return redirect(url_for('index'))
    usuario = Usuario.query.get(user_id)
    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')

    if not check_password_hash(usuario.contraseña, current_password):
        flash('La contraseña actual es incorrecta.', 'error')
        return redirect(url_for('user.perfil'))

    if new_password != confirm_password:
        flash('Las contraseñas nuevas no coinciden.', 'error')
        return redirect(url_for('user.perfil'))

    usuario.contraseña = generate_password_hash(new_password)
    db.session.commit()
    flash('Contraseña actualizada correctamente.', 'success')
    return redirect(url_for('user.perfil'))
