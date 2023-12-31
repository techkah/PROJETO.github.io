from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        nome= request.form['nome']
        sobrenome= request.form['sobrenome']
        email= request.form['email']
        telefone= request.form['telefone']
        estudo= request.form.get('estudo')
        trabalho= request.form.get('trabalho')
        curiosidade= request.form.get('curiosidade')
        conhecimento= request.form.get('conhecimento')
        permissao= request.form.get('permissao')
        negado= request.form.get('negado')
        feedback= request.form.get('feedback')

        #validacao dos campos#

        if not nome or not sobrenome or not email:

             return "Por favor, preencha todos os campos obrigatórios."
        #Processando dados#
        return f"nome: {nome} <br> sobrenome: {sobrenome} <br> email: {email} <br> telefone: {telefone} <br> estudo: {estudo} <br> trabalho: {trabalho} <br> curiosidade: {curiosidade} <br> conhecimento: {conhecimento} <br> permissao: {permissao} <br> negado: {negado} <br> feedback: {feedback}"
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

        
