from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/") #Login
def homepage():
    return 'Home page'

@app.route("/contatos")
def contatos():
 return render_template('contatos.html', title="Página de Teste", heading="Olá, Flask!", content="Este é um exemplo de template.")
if __name__ =='__main__':
    app.run(debug= True)

