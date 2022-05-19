# importamos librerias
from unicodedata import name
from flask import (Flask, request, jsonify)


# create the Flask app
app = Flask(__name__)


#se crea ruta
@app.route('/calcula-sisdis')
#creamos funcion para almacenar datos
def datos():
    # se define el tipo de operacion
    tipo = request.args.get('tipo')
    # se define el valor1 de la operacion
    valor1 = request.args['valor1']
    # se define el valor2 de la operacion
    valor2 = request.args['valor2']
    # se convierten en numericos para poderlos operar
    valor1 = int(valor1)
    valor2 = int(valor2)
    # se define la logica de la calculadora
    if tipo=='suma':
        operacion = valor1+valor2
        return '''<h1>El resultado de la '''+ (tipo) +'''Es: {}</h1>'''.format(operacion)

    elif tipo=='resta':
        operacion = valor1-valor2
        return '''<h1>El resultado de la '''+ (tipo) +'''Es: {}</h1>'''.format(operacion)
    elif tipo=='multiplicacion': 
        operacion = valor1*valor2
        return '''<h1>El resultado de la '''+ (tipo) +'''Es: {}</h1>'''.format(operacion)
    elif tipo=='division':
        operacion = valor1/valor2
        return '''<h1>El resultado de la '''+ (tipo) +'''Es: {}</h1>'''.format(operacion)
    else:
        return '''<h1>calculo no definido Es: {}</h1>'''   

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

    #ejemplo de url con parametros a utilizar en el cliente
    #  http://127.0.0.1:5000//calcula-sisdis?tipo=suma&valor1=2&valor2=3