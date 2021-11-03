import smtplib
from getpass import getpass
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'llavesecreta'

@app.route('/', methods=['GET','POST'])
def inicio():
    if request.method == 'POST':
        subject_not = request.form["asunto"]
        body_not = request.form["cuerpo"]

        fichero = open('datos.txt')
        lineas = fichero.readlines()
        usernameX = lineas[0]
        password = lineas[1]
        usernameY = lineas[2]

        message = 'Subject:{}\n\n{}'.format(subject_not, body_not)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(usernameX , password)
        server.sendmail(usernameX, usernameY, message)
        server.quit()

    return render_template('index.html')

if __name__ == '__main__':
   		app.run(debug=True)
