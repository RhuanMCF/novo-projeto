from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'segredo123'  # depois muda pra algo forte

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        if usuario == 'admin' and senha == 'admin123':
            session['usuario'] = 'admin'
            return redirect('/admin')
        elif usuario == 'bruno' and senha == 'bruno123':
            session['usuario'] = 'bruno'
            return redirect('/bruno')
        elif usuario == 'ícaro' and senha == 'ícaro123':
            session['usuario'] = 'ícaro'
            return redirect('/icaro')
        else:
            flash('Usuário ou senha incorretos!')

    return render_template('login.html')

@app.route('/admin')
def admin():
    if session.get('usuario') != 'admin':
        return redirect('/')
    return render_template('admin.html')

@app.route('/bruno')
def bruno():
    if session.get('usuario') != 'bruno':
        return redirect('/')
    return render_template('bruno.html')

@app.route('/icaro')
def icaro():
    if session.get('usuario') != 'ícaro':
        return redirect('/')
    return render_template('icaro.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)