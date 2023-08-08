from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        email = request.form.get('email')
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        mensagem = f"Cadastro concluído para {nome} com o email {email} e telefone {telefone}."
        return redirect(url_for('feedback', mensagem=mensagem))
    
    return render_template('formulario.html')

@app.route('/feedback')
def feedback():
    mensagem = request.args.get('mensagem')
    return render_template('feedback.html', mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)