from flask import Flask, render_template

app = Flask(__name__)

# --- Datos de ejemplo ---
datos_ahorro = {
    'titulo': 'Registro de Ahorro',
    'descripcion': 'Administra tus ahorros personales y lleva el control de tus metas financieras.'
}

tips = [
    "Registra todos tus ingresos y gastos.",
    "Ahorra una parte de tus ingresos cada mes.",
    "Evita las compras impulsivas.",
    "Establece metas financieras a corto y largo plazo.",
    "Compara precios."
]

gastos = [
    {'categoria': 'Comida', 'monto': 1200},
    {'categoria': 'Transporte', 'monto': 800},
    {'categoria': 'Entretenimiento', 'monto': 400},
    {'categoria': 'Servicios', 'monto': 600},
]


# --- Rutas ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ahorro')
def ahorro():
    return render_template('ahorro.html', datos=datos_ahorro)

@app.route('/tips_ahorro')
def tips_ahorro():
    return render_template('tips_ahorro.html', tips=tips)

@app.route('/gastos')
def gastos_view():
    return render_template('gastos.html', gastos=gastos)


if __name__ == '__main__':
    app.run(debug=True)
