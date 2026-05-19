from flask import Flask, render_template, request, jsonify
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Configure Brevo API
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = os.environ.get('BREVO_API_KEY')

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    # Create email
    send_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": "vatyoo@gmail.com", "name": "Vasile"}],
        sender={"email": "vatyoo@gmail.com", "name": "vatyo.dev"},
        subject=f"New message from {name} — vatyo.dev",
        text_content=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    )

    try:
        api_instance.send_transac_email(send_email)
        return jsonify({'success': True})
    except ApiException as e:
        print(f"Error: {e}")
        return jsonify({'success': False}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)