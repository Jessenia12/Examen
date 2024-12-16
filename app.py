from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Diccionario para almacenar estudiantes (en una base de datos real, esto sería diferente)
students = []

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['POST'])
def add_student():
    # Obtener los datos del formulario
    name = request.form.get('name')
    age = request.form.get('age')

    # Validar que se recibieron los datos
    if name and age:
        students.append({'name': name, 'age': age})
    
    # Redirigir a la página principal para mostrar la lista actualizada
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
