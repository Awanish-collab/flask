from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for sessions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_session', methods=['GET', 'POST'])
def set_session():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username  # Store data in session
        flash('Session data set successfully!', 'success')
        return redirect(url_for('get_session'))
    return render_template('set_session.html')

@app.route('/get_session')
def get_session():
    
    username = session.get('username')  # Retrieve session data
    return f"{dict(session)} <br><br> {render_template('get_session.html', username=username)}"

@app.route('/clear_session')
def clear_session():
    session.clear()  # Clear session data
    flash('Session data cleared successfully!', 'info')
    return render_template('clear_session.html')

if __name__ == '__main__':
    app.run(debug=True)
