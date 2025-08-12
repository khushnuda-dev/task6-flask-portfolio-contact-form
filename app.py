from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you can handle the form data (e.g., save to DB, send email)
        print(f"New message from {name} ({email}): {message}")
        return redirect(url_for('home'))
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)