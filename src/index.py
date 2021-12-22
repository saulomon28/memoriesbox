from flask import Flask,render_template,request, session
from flask.json import dumps
from os import listdir
import datetime

app = Flask(__name__)
app.secret_key = 'dGVhbW9fbXVjaG8='
app.config['SESSION_TYPE'] = 'filesystem'




@app.context_processor
def inject_today_date():
    anniversary = datetime.date(2020,9,19) # se tiene que agregar un dia antes para que se tome encuenta el 20
    #diaActual = datetime.date(2021,9,20)
    diaActual = datetime.date.today()
    mesDia = 0.0328763520399776
    diasAnniversary = (diaActual-anniversary).days
    
    result = diasAnniversary * mesDia

    meses = int(result)
    dias =int((result-meses) / mesDia)
    anios = int(result/12)

    if(anios >= 1):
        meses = meses - (anios * 12)

    fechaEstreno = datetime.date(2021,8,20)

    return {
        'fulltime' : 'Exactamente... '+ str(anios) + ' año(s) '+ str(meses)+' meses '+str(dias)+' días.',
        'days' : 'Llevamos ' + str(diasAnniversary) + ' días.',
        'rose':app.static_folder+'/patt/rosa.gltf',
        'estreno' : fechaEstreno,
        'diaactual': diaActual
    }

@app.route("/")
def login():
    try:
        if session['TSSId_Token'] == app.secret_key:
            return render_template("inicio.html")
        else:
            return render_template("login.html")
    except KeyError:
        return render_template("login.html")
        
@app.route('/home', methods=['POST','GET'])
def home():
    try:
        if request.method == 'POST':
            token = request.form['TSSId']
            session['TSSId_Token'] = token

        if session['TSSId_Token'] == app.secret_key:
            # print('token= '+session['TSSId_Token'] +'   '+'appSecret= '+app.secret_key)
            return render_template('inicio.html')
        else:
            return render_template('errorPage.html')

    except KeyError:
        return render_template("login.html")
    

@app.route('/inicio')
def inicio():
    try:
        if session['TSSId_Token'] == app.secret_key:
            # print('token= '+session['TSSId_Token'] +'   '+'appSecret= '+app.secret_key)
            return render_template('inicio.html')
        else:
            return render_template('errorPage.html')
    except KeyError:
        return render_template("login.html")

@app.route('/poemas')
def poemas():
    try:
        if session['TSSId_Token'] == app.secret_key:
            # print('token= '+session['TSSId_Token'] +'   '+'appSecret= '+app.secret_key)
            return render_template('poemas.html')
        else:
            return render_template('errorPage.html')
    except KeyError:
        return render_template("login.html")
@app.route('/galeria')
def galeria():
    try:
        
        if session['TSSId_Token'] == app.secret_key:
            list= dumps(listdir(app.static_folder + "/images"))
            # print('token= '+session['TSSId_Token'] +'   '+'appSecret= '+app.secret_key)
            return render_template('galeria.html',list=list)
        else:
            return render_template('errorPage.html')
    except KeyError:
        return render_template("login.html")

@app.route("/nocompatible_device")
def nocompatible_device():
    try:

        if session['TSSId_Token'] == app.secret_key:
            # print('token= '+session['TSSId_Token'] +'   '+'appSecret= '+app.secret_key)
            return render_template("nocompatible_device.html")
        else:
            return render_template('errorPage.html')
    except KeyError:
        return render_template("login.html")


@app.route("/gift")
def gift():
    try:
        if session['TSSId_Token'] == app.secret_key:
            # print('token= '+session['TSSId_Token'] +'   '+'appSecret= '+app.secret_key)
            return render_template('gift.html')
        else:
            return render_template('errorPage.html')
    except KeyError:
        return render_template("login.html")

@app.route("/heart")
def heart():
    try:
        if session['TSSId_Token'] == app.secret_key:
            # print('token= '+session['TSSId_Token'] +'   '+'appSecret= '+app.secret_key)
            return render_template('heart.html')
        else:
            return render_template('errorPage.html')
    except KeyError:
        return render_template("login.html")

@app.route("/akaza")
def akaza():
    try:
        if session['TSSId_Token'] == app.secret_key:
            # print('token= '+session['TSSId_Token'] +'   '+'appSecret= '+app.secret_key)
            return render_template('akaza.html')
        else:
            return render_template('errorPage.html')
    except KeyError:
        return render_template("login.html")


@app.route("/error")
def func():
    return render_template("errorPage.html")
    

if __name__ == '__main__':
    app.run(debug=True)