from flask import Flask, json
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'devangmaru6663@gmail.com'
app.config['MAIL_PASSWORD'] = 'gaum gbbr nhxk nmpv'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route('/')
def email():
    try:
        msg = Message(subject='important message', sender='devangmaru6663@gmail.com', recipients=['devangmaru6663@gmail.com'])
        msg.body = "hello this is demo email for flask python ."
        mail.send(msg)
    except Exception as e:
        return f'Error sending email: {str(e)}'
    
    return 'email sent'

if __name__ == "__main__":
    app.run(debug=True)
