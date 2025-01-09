from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set-cookie', methods=['POST'])
def set_cookie():
    cookie_name = request.form['cookie_name']
    cookie_value = request.form['cookie_value']
    resp = make_response("Cookie has been set!")
    resp.set_cookie(cookie_name, cookie_value)
    return resp

@app.route('/get-cookie', methods=['GET'])
def get_cookie():
    cookies = request.cookies   # it will return all available cookies in dictionary
    cookie_name = request.args.get('cookie_name')
    cookie_value = request.cookies.get(cookie_name)
    if cookie_value:
        return f"{cookies}<br><br>The value of the cookie '{cookie_name}' is: {cookie_value}</p>"
    else:
        return f"Cookie '{cookie_name}' not found!"

@app.route('/delete-cookie', methods=['POST'])
def delete_cookie():
    cookie_name = request.form['cookie_name']
    resp = make_response(f"Cookie '{cookie_name}' has been deleted!")
    resp.delete_cookie(cookie_name)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
