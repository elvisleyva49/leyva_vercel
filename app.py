# # app.py
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Obtener los datos del formulario
    grade1 = float(request.form['grade1'])
    grade2 = float(request.form['grade2'])
    grade3 = float(request.form['grade3'])

    # Calcular el promedio
    average = (grade1 + grade2 + grade3) / 3.0

    # Determinar si aprobó o no
    if average >= 10.5:
        result = 'Aprobado'
    else:
        result = 'Desaprobado'

    return render_template('result.html', average=average, result=result)

if __name__ == '__main__':
    app.run(debug=True)
