from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicioPagina():
    return render_template("main.html")

@app.route('/<int:numero1>')
def segundaPagina(numero1):
    return render_template("second.html",numero1=numero1)

@app.route('/<int:numero1>/<int:numero2>')
def terceraPagina(numero1,numero2):
    numero2=int(numero2/2)
    return render_template("third.html",numero1=numero1,numero2=numero2)

if __name__ == "__main__":
    app.run(debug=True)