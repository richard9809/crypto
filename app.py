import codecs
import secrets
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from triple import encrypt, decrypt
from sendSMS import *

iv = '2132435465768797'
key = secrets.token_hex(24)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'rmulu333@gmail.com',
    "MAIL_PASSWORD": 'mhxnceufumjwpryl'
}

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/encrypt")
def do_encrypt():
    return render_template('encrypt.html')

@app.route("/encryptedMessage", methods=['POST'])
def encryptedMessage():
    email = request.form['email']
    phone = request.form['phone']
    msg = request.form['msg']
    
    cipher_text = encrypt(iv, key, msg)
    cipherString = cipher_text.decode('utf-8')
    
    print(cipherString)
    print(cipher_text)
    print(key)
    
    with app.app_context():
        message = Message(subject= "Encryption",
                       sender=app.config.get("MAIL_USERNAME"),
                       recipients=[email],
                       body= cipherString + "")
        
        mail.send(message)
        
    sendSMS(key, phone)
    
    return "Successful!!!"

@app.route("/decrypt")
def do_decrypt():
    return render_template('decrypt.html')

@app.route("/decryptMessage", methods=['POST'])
def decryptMessage():
    key = request.form['OTE']
    msg = request.form['msg']
    finalMessage, _ = codecs.escape_decode(msg, 'hex')
    
    decryptedMessage = decrypt(iv, key, finalMessage)
    return decryptedMessage

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == '__main__':
    app.run(debug=True)