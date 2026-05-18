from flask import Flask, render_template, request
import os   
#Create a Flask application
app = Flask(__name__)
#Define a route for the home page
@app.route('/')
def index():
    return render_template('index.html')
# Contact form route
@app.route('/contact', methods=['POST'])
def contact():  
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
     # For now just print - later we can add email sending
    print(f"New message from {name} ({email}): {message}")
    # Here you can add code to save the contact form data to a database or send an email
    return render_template('contact_success.html', name=name)
#start server
if __name__ == '__main__':
   port = int(os.environ.get('PORT', 5000))
   app.run(host='0.0.0.0', port=port, debug=True)