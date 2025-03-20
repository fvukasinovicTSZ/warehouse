from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_info = {}
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')

        if first_name and last_name and email:
            user_info = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email
            }
        else:
            user_info = {'error': 'Please fill in all fields.'}

    return render_template('index.html', user_info=user_info)

if __name__ == '__main__':
    app.run(debug=True)
