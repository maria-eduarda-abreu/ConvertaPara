import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# Configurações do Flask
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'docx', 'xlsx', 'pptx', 'jpg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Funções auxiliares
def allowed_file(filename):
    """
    Verifica se a extensão do arquivo é permitida.
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Rota principal (página inicial)
@app.route('/')
def home():
    """
    Exibe a página inicial.
    """
    return render_template('index.html')

# Rota para o upload
@app.route('/upload-word-to-pdf', methods=['POST'])
def upload_word_to_pdf():
    """
    Gerencia o upload e a conversão de Word para PDF.
    """
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Cria a pasta 'uploads' se ela não existir
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        
        file.save(filepath)
        
        # Aqui, no futuro, vamos chamar a função de conversão
        print(f"Arquivo '{filename}' salvo com sucesso para conversão.")
        
        return "Upload de arquivo Word concluído! Conversão em andamento..."
    
    return "Tipo de arquivo não permitido."

if __name__ == '__main__':
    app.run(debug=True)