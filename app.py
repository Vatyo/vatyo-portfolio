from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# ===== EMAIL CONFIGURATION =====
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'vatyoo@gmail.com'

mail = Mail(app)

# ===== MAIN PAGE =====
@app.route('/')
def home():
    return render_template('index.html')

# ===== CONTACT FORM =====
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Send email
    msg = Message(
        subject=f"New message from {name} — vatyo.dev",
        sender=app.config['MAIL_USERNAME'],
        recipients=['vatyoo@gmail.com'],
        body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    )
    mail.send(msg)

    return render_template('index.html', success=True)

# ===== START SERVER =====
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)