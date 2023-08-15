from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        nome= request.form['nome']
        email= request.form['email']
        number= request.form['number']
        estudo= request.form['estudo']
        trabalho= request.form['trabalho']
        curiosidade= request.form['curiosidade']
        colaborador= request.form['colaborador']
        outros= request.form['outros']
        permissao= request.form['permissao']
        return f"nome: {nome} <br> email: {email} <br> number: {number} <br> estudo: {estudo} <br> trabalho: {trabalho} <br> curiosidade: {curiosidade} <br> colaborador: {colaborador} <br> outros: {outros} <br> permissao: {permissao}"
    return render_template ('index.html')

if __name__ == '_main_':
    app.run(debug=True)