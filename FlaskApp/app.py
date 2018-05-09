import psycopg2
from flask import Flask, render_template, send_from_directory, request, json


app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignIn():
    return render_template('signup.html')

@app.route('/showSignIn')
def showSignUp():
    return render_template('signin.html')

@app.route('/static/<path:path>') #Enviar el css
def send_static(path):
    return send_from_directory('static', path)

@app.route('/signIn', methods=['POST', 'GET'])
def signIn():
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    if _email and _password:
        conn = psycopg2.connect(dbname='BucketList', user='victor', password='admin')
        cursor = conn.cursor()
       
        cursor.execute('SELECT id_user FROM table_user WHERE user_username = %s', (_email,))
        resultUser = cursor.fetchone()
    
        if resultUser:
            cursor.execute("select id_user from table_user where user_username = %s and user_password = %s", (_email, _password))
            resultPassw = cursor.fetchone()
      
            if resultPassw:
                print("Login correcte")
                conn.close()
                return ("Welcome %s" % (_email))
            else:
                print("Contrasenya incorrecta")
                return ("Contrasenya incorrecta")
        else:
            print("Ususari incorrecte")
            return ("Usuari incorrecte")

    else:
        print("Has d'introduir l'usuari i la contrasenya")
        return ("Has d'introduir l'usuari i la contrasenya")

@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    #llegir els POST valors
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _id = "DEFAULT"
    
    # validar valors rebuts
    if _name and _email and _password:
        
        conn = psycopg2.connect(dbname='BucketList', user='victor', password='admin')
        cursor = conn.cursor()
        #cursor.execute("INSERT INTO table_user VALUES(%s, %s, %s)", (_name, _email, _password))
        
        cursor.execute("SELECT sp_createuser (%s, %s, %s)", (_name, _email, _password))
        conn.commit()
        
        data = cursor.fetchall() 

        if len(data) is 0:
            print("Donat d'alta")
            conn.close()
            return "Usuari donat d'alta"
        else:
            return "L'usuari ja existeix"


    else:
        return "Has d'omplir tots els camps"

    



if __name__ == "__main__":
    app.run()

