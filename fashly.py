from flask import Flask, render_template, url_for, redirect, request, session, jsonify
from flask_mysqldb import MySQL
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import jsonify
fashlyApp = Flask(__name__)
db = MySQL(fashlyApp)
sessionManager = LoginManager(fashlyApp)

@sessionManager.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@fashlyApp.route('/')
def home():
    if current_user.is_authenticated:
        if current_user.perfil == 'A':
            return redirect(url_for('homeAdmin'))
        else:
            return redirect(url_for('homeuser'))

    selProductos = db.connection.cursor()
    selProductos.execute("SELECT * FROM productos WHERE catalogo_id=101")
    p = selProductos.fetchall()
    selProductos.close()

    selropa2 = db.connection.cursor()
    selropa2.execute("SELECT * FROM productos WHERE catalogo_id=102")
    p2 = selropa2.fetchall()
    selropa2.close()

    return render_template('home.html', ropa1=p, ropa2=p2)

@fashlyApp.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        clave = request.form['clave']
        claveCifrada = generate_password_hash(clave)
        telefono = request.form['telefono']
        fechareg = datetime.now()
        regUsuario = db.connection.cursor()
        regUsuario.execute(
            "INSERT INTO usuario (nombre,apellido,correo,clave,telefono,fechareg) VALUES (%s,%s,%s,%s,%s,%s)",
            (nombre, apellido, correo, claveCifrada, telefono, fechareg)
        )
        db.connection.commit()
        regUsuario.close()
        return redirect(url_for('home'))
    else:
        return render_template('signup.html')

@fashlyApp.route('/IUsuario', methods=['POST', 'GET'])
def IUsuario():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    clave = request.form['clave']
    claveCifrada = generate_password_hash(clave)
    telefono = request.form['telefono']
    fechareg = datetime.now()
    perfil = request.form['perfil']
    regUsuario = db.connection.cursor()
    regUsuario.execute(
        "INSERT INTO usuario (nombre,apellido,correo,clave,telefono,fechareg,perfil) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (nombre, apellido, correo, claveCifrada, telefono, fechareg, perfil)
    )
    db.connection.commit()
    regUsuario.close()
    return redirect(url_for('sUsuario'))

@fashlyApp.route('/uUsuario/<int:id>', methods=['POST', 'GET'])
def uUsuario(id):
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    telefono = request.form['telefono']
    perfil = request.form['perfil']
    fechareg = datetime.now()
    actUsuario = db.connection.cursor()
    actUsuario.execute(
        "UPDATE usuario SET nombre = %s, apellido = %s, correo = %s, telefono = %s, perfil = %s, fechareg = %s WHERE id = %s",
        (nombre, apellido, correo, telefono, perfil, fechareg, id)
    )
    db.connection.commit()
    actUsuario.close()
    return redirect(url_for('sUsuario'))

@fashlyApp.route('/dUsuario/<int:id>', methods=['POST', 'GET'])
def dUsuario(id):
    delUsuario = db.connection.cursor()
    delUsuario.execute("DELETE FROM usuario WHERE id = %s", (id,))
    db.connection.commit()
    delUsuario.close()
    return redirect(url_for('sUsuario'))

@fashlyApp.route('/iCarritto/<int:producto_id>/<string:precio>')
def iCarritto(producto_id, precio):
    usuario_id = session.get('id')
    if usuario_id is None:
        return jsonify({'ok': False, 'error': 'Usuario no autenticado'}), 401

    cur = db.connection.cursor()
    cur.execute(
        "SELECT * FROM carritto WHERE producto_id = %s AND usuario_id = %s AND status = 'T'",
        (producto_id, usuario_id)
    )
    item = cur.fetchone()

    if item:
        id_car = item[0]
        cantidad_actual = item[4]
        nueva_cant = cantidad_actual + 1
        nuevo_importe = float(precio) * nueva_cant
        cur.execute(
            "UPDATE carritto SET cantidad = %s, importe = %s WHERE id = %s",
            (nueva_cant, nuevo_importe, id_car)
        )
    else:
        cur.execute(
            "INSERT INTO carritto (producto_id, usuario_id, cantidad, importe, status) VALUES (%s, %s, %s, %s, %s)",
            (producto_id, usuario_id, 1, float(precio), 'T')
        )

    # Actualizar cantidad total en la sesión
    cur.execute("SELECT cantidad FROM carritto WHERE usuario_id = %s AND status = 'T'", (usuario_id,))
    cantidades = cur.fetchall()
    session['carritto'] = sum([item[0] for item in cantidades])

    db.connection.commit()
    cur.close()

    # Si es AJAX, devolvemos JSON con el nuevo total
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'ok': True, 'carritto': session['carritto']})

    # Si no, redirigimos (sin flash)
    return redirect(url_for('sCarritto'))

@fashlyApp.route('/dCarritto/<int:car_id>')
@login_required
def dCarritto(car_id):
    cur = db.connection.cursor()
    cur.execute("DELETE FROM carritto WHERE id = %s", (car_id,))
    db.connection.commit()
    cur.close()
    return redirect(url_for('sCarritto'))

@fashlyApp.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        usuario = User(0, None, None, request.form['correo'], request.form['clave'], None, None, None)
        usuarioAutenticado = ModelUser.signin(db, usuario)
        if usuarioAutenticado is not None:
            if usuarioAutenticado.clave:
                login_user(usuarioAutenticado)
                session['id'] = usuarioAutenticado.id
                session['nombre'] = usuarioAutenticado.nombre
                session['perfil'] = usuarioAutenticado.perfil
                if usuarioAutenticado.perfil == 'A':
                    return render_template('admin.html')
                else:
                    selProductos = db.connection.cursor()
                    selProductos.execute("SELECT * FROM productos WHERE catalogo_id=101")
                    p = selProductos.fetchall()
                    selProductos.close()

                    selropa2 = db.connection.cursor()
                    selropa2.execute("SELECT * FROM productos WHERE catalogo_id=102")
                    p2 = selropa2.fetchall()
                    selropa2.close()

                    selCarritto = db.connection.cursor()
                    selCarritto.execute(
                        "SELECT * FROM carritto WHERE usuario_id = %s AND status = 'T'",
                        (usuarioAutenticado.id,)
                    )
                    c = selCarritto.fetchall()
                    session['carritto'] = sum([item[4] for item in c])
                    selCarritto.close()

                    return render_template('user.html', ropa1=p, ropa2=p2)
            else:
                flash('❌ Error: contraseña incorrecta', 'login')
                return redirect(request.url)
        else:
            flash('❌ Error: correo o teléfono incorrecto', 'login')
            return redirect(request.url)
    else:
        return render_template('home.html')

@fashlyApp.route('/signout', methods=['POST', 'GET'])
def signout():
    logout_user()
    return redirect(url_for('home'))

@fashlyApp.route('/home-admin', methods=['GET', 'POST'])
def homeAdmin():
    return render_template('admin.html')

@fashlyApp.route('/home-user', methods=['GET', 'POST'])
def homeuser():
    selProductos = db.connection.cursor()
    selProductos.execute("SELECT * FROM productos WHERE catalogo_id=101")
    p = selProductos.fetchall()
    selProductos.close()

    selropa2 = db.connection.cursor()
    selropa2.execute("SELECT * FROM productos WHERE catalogo_id=102")
    p2 = selropa2.fetchall()
    selropa2.close()

    selCarritto = db.connection.cursor()
    selCarritto.execute(
        "SELECT * FROM carritto WHERE usuario_id = %s AND status = 'T'",
        (session['id'],)
    )
    c = selCarritto.fetchall()
    session['carritto'] = sum([item[4] for item in c])
    selCarritto.close()

    return render_template('user.html', ropa1=p, ropa2=p2)

@fashlyApp.route('/sUsuario', methods=['GET', 'POST'])
def sUsuario():
    selUsuario = db.connection.cursor()
    selUsuario.execute("SELECT * FROM usuario")
    u = selUsuario.fetchall()
    selUsuario.close()
    return render_template('users.html', usuarios=u)

@fashlyApp.route('/sProductos', methods=['POST', 'GET'])
def sproductos():
    selProductos = db.connection.cursor()
    selProductos.execute("SELECT * FROM productos")
    p = selProductos.fetchall()
    selProductos.close()
    return render_template('products.html', productos=p)

@fashlyApp.route('/iProducto', methods=['POST'])
def iProducto():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    catalogo_id = request.form['catalogo_id']
    nombre_imagen = request.form['nombre_imagen']

    cur = db.connection.cursor()
    cur.execute(
        "INSERT INTO productos (nombre, descripcion, precio, catalogo_id, nombre_imagen) VALUES (%s, %s, %s, %s, %s)",
        (nombre, descripcion, precio, catalogo_id, nombre_imagen)
    )
    db.connection.commit()
    cur.close()

    return redirect(url_for('sproductos'))

@fashlyApp.route('/uProducto/<int:id>', methods=['POST'])
def uProducto(id):
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    catalogo_id = request.form['catalogo_id']
    nombre_imagen = request.form['nombre_imagen']

    cur = db.connection.cursor()
    cur.execute(
        "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, catalogo_id = %s, nombre_imagen = %s WHERE id = %s",
        (nombre, descripcion, precio, catalogo_id, nombre_imagen, id)
    )
    db.connection.commit()
    cur.close()

    return redirect(url_for('sproductos'))

@fashlyApp.route('/dProducto/<int:id>', methods=['POST'])
def dProducto(id):
    cur = db.connection.cursor()
    cur.execute("DELETE FROM productos WHERE id = %s", (id,))
    db.connection.commit()
    cur.close()
    return redirect(url_for('sproductos'))




@fashlyApp.route('/sCarritto', methods=['POST', 'GET'])
def sCarritto():
    selCarritto = db.connection.cursor()
    selCarritto.execute(
        """
        SELECT 
            carritto.id,
            carritto.producto_id,
            carritto.usuario_id,
            carritto.pedidos_id,
            carritto.cantidad,
            carritto.importe,
            carritto.status,
            productos.id,
            productos.nombre,
            productos.descripcion,
            productos.precio,
            productos.catalogo_id,
            productos.nombre_imagen
        FROM carritto
        INNER JOIN productos ON carritto.producto_id = productos.id
        WHERE carritto.usuario_id = %s AND carritto.status = 'T'
        """,
        (session['id'],),
    )
    c = selCarritto.fetchall()
    selCarritto.close()

    total = sum([item[5] for item in c])
    return render_template('carritto.html', carritto=c, total=total)

@fashlyApp.route('/decrementarCarritto/<int:car_id>/<string:precio>')
@login_required
def decrementarCarritto(car_id, precio):
    cur = db.connection.cursor()
    cur.execute("SELECT cantidad FROM carritto WHERE id = %s", (car_id,))
    cantidad_actual = cur.fetchone()[0]

    if cantidad_actual > 1:
        nueva_cantidad = cantidad_actual - 1
        nuevo_importe = float(precio) * nueva_cantidad
        cur.execute(
            "UPDATE carritto SET cantidad = %s, importe = %s WHERE id = %s",
            (nueva_cantidad, nuevo_importe, car_id)
        )
    else:
        cur.execute("DELETE FROM carritto WHERE id = %s", (car_id,))

    cur.execute("SELECT cantidad FROM carritto WHERE usuario_id = %s AND status = 'T'", (session['id'],))
    cantidades = cur.fetchall()
    session['carritto'] = sum([item[0] for item in cantidades])

    db.connection.commit()
    cur.close()
    return redirect(url_for('sCarritto'))

@fashlyApp.route('/incrementarCarritto/<int:car_id>/<string:precio>')
@login_required
def incrementarCarritto(car_id, precio):
    cur = db.connection.cursor()
    cur.execute("SELECT cantidad FROM carritto WHERE id = %s", (car_id,))
    item = cur.fetchone()
    if item:
        nueva_cant = item[0] + 1
        nuevo_importe = float(precio) * nueva_cant
        cur.execute(
            "UPDATE carritto SET cantidad = %s, importe = %s WHERE id = %s",
            (nueva_cant, nuevo_importe, car_id)
        )
        db.connection.commit()

    cur.execute("SELECT cantidad FROM carritto WHERE usuario_id = %s AND status = 'T'", (session['id'],))
    cantidades = cur.fetchall()
    session['carritto'] = sum([item[0] for item in cantidades])

    cur.close()
    return redirect(url_for('sCarritto'))

@fashlyApp.route('/buscar')
def buscar():
    q = request.args.get('q', '').strip()
    if not q:
        return jsonify([])

    try:
        q_sin_puntos = q.replace('.', '').lower()

        cur = db.connection.cursor()

        # Solo busca en nombre y descripcion, elimina categoria si no existe
        sql = """
            SELECT id, nombre, descripcion, precio, nombre_imagen
            FROM productos
            WHERE LOWER(REPLACE(nombre, '.', '')) LIKE %s
               OR LOWER(REPLACE(descripcion, '.', '')) LIKE %s
            LIMIT 10
        """
        term = f"%{q_sin_puntos}%"
        cur.execute(sql, (term, term))
        rows = cur.fetchall()
        cur.close()

        resultados = []
        for (prod_id, nombre, descripcion, precio, nombre_imagen) in rows:
            resultados.append({
                'id': prod_id,
                'nombre': nombre,
                'descripcion': descripcion,
                'precio': precio,
                'imagen': nombre_imagen
            })
        return jsonify(resultados)
    except Exception as e:
        print("Error en /buscar:", e)
        return jsonify({'error': 'Error interno en el servidor'}), 500




@fashlyApp.route('/procesar_pago', methods=['POST'])
@login_required
def procesar_pago():
    usuario_id = session.get('id')
    if not usuario_id:
        return jsonify({'success': False, 'error': 'Usuario no autenticado'}), 401

    cur = db.connection.cursor()
    # Marcar todos los productos en carrito como comprados o eliminar
    # Por ejemplo aquí borramos el carrito
    cur.execute("DELETE FROM carritto WHERE usuario_id = %s AND status = 'T'", (usuario_id,))
    db.connection.commit()
    cur.close()

    # Actualizamos la cantidad en sesión a 0
    session['carritto'] = 0

    return jsonify({'success': True})


@fashlyApp.route('/flower')
def flower_page():
    return render_template('flower.html')



@fashlyApp.route('/finalizar_pedido', methods=['POST'])
@login_required
def finalizar_pedido():
    try:
        usuario_id = session['id']
        cur = db.connection.cursor()

        # Aquí podrías insertar datos del pedido en una tabla pedidos si tienes
        # Por ahora simulamos finalización

        # Cambiar status de carrito a 'F' (finalizado) para simular pedido realizado
        cur.execute(
            "UPDATE carritto SET status = 'F' WHERE usuario_id = %s AND status = 'T'",
            (usuario_id,)
        )
        db.connection.commit()
        cur.close()

        # Vaciar el carrito en la sesión
        session['carritto'] = 0

        return jsonify({'success': True, 'message': 'Pedido finalizado correctamente'})
    except Exception as e:
        print("Error al finalizar pedido:", e)
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    fashlyApp.config.from_object(config['development'])
    fashlyApp.run(port=3300)
