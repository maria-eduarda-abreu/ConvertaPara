#Importa ferramentas necessárias do Flask

from flask import Flask, render_template

#Cria a aplicação Flask
app = Flask(__name__)

#É o endereço da página. O / significa a página inicial do site 
@app.route('/')
#Esta função é executada quando o usuário acessa a página inicial
def home():
    """
    Exibe a página inicial do site.
    """
# Diz ao Flask para carregar e exibir o arquivo HTML chamado index.html
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)