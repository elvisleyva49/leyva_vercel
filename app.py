# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    grades = []
    weights = []

    # Obtener los datos del formulario
    for i in range(1, 5):  # Iterar sobre las 4 posibles notas
        grade_key = 'grade' + str(i)
        weight_key = 'weight' + str(i)

        if request.form.get(grade_key):
            grade = float(request.form[grade_key])
            grades.append(grade)
        
        if request.form.get(weight_key):
            weight = float(request.form[weight_key])
            weights.append(weight)

    # Calcular el promedio ponderado
    weighted_sum = sum(grade * weight / 100 for grade, weight in zip(grades, weights))
    total_weight = sum(weights)
    
    if total_weight > 0:
        average = weighted_sum / total_weight * 100
    else:
        average = 0

    # Determinar si aprobó o no
    if average >= 10.5:
        result = 'Aprobado'
    else:
        result = 'Desaprobado'

    return render_template('result.html', average=average, result=result)

if __name__ == '__main__':
    app.run(debug=True)
