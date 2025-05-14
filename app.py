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

@app.route('/add.html', methods=['GET', 'POST'])
def add():

    user_info = {}
    sqlEntry = ""

    if request.method == 'POST':
        item_name = request.form.get('item_name')
        quantity = request.form.get('quantity')
        weight = request.form.get('weight')
        price = request.form.get('price')
        min_order = request.form.get('min_order')

        if all([item_name, quantity, weight, price, min_order]):
            user_info = {
                'item_name': item_name,
                'quantity': quantity,
                'weight': weight,
                'price': price,
                'min_order': min_order
            }

            sqlEntry = f"INSERT INTO items (item_name, quantity, weight, price, min_order) VALUES ('{user_info['item_name']}', '{user_info['quantity']}', '{user_info['weight']}', '{user_info['price']}', '{user_info['min_order']}');"

        else:
            user_info = {'error': 'Please fill in all fields.'}

    return render_template('add.html', user_info=user_info, sqlEntry=sqlEntry)

@app.route('/edit.html', methods=['GET', 'POST'])
def edit():
    user_info = {}
    sqlUpdate = "Nothing"

    if request.method == 'POST':
        item_id = request.form.get('item_id')
        item_name = request.form.get('item_name')
        quantity = request.form.get('quantity')
        weight = request.form.get('weight')
        price = request.form.get('price')
        min_order = request.form.get('min_order')
        
        if item_id:
            user_info = {
            'item_id': item_id,
            'item_name': item_name,
            'quantity': quantity,
            'weight': weight,
            'price': price,
            'min_order': min_order
            }

            update_fields = []
            if item_name:
                update_fields.append(f"item_name='{item_name}'")
            if quantity:
                update_fields.append(f"quantity='{quantity}'")
            if weight:
                update_fields.append(f"weight='{weight}'")
            if price:
                update_fields.append(f"price='{price}'")
            if min_order:
                update_fields.append(f"min_order='{min_order}'")

            sqlUpdate = (
                f"UPDATE items SET {', '.join(update_fields)} "
                f"WHERE id='{item_id}';"
            )

        else:
            user_info = {'error': 'Item ID is required.'}

    return render_template('edit.html', user_info=user_info, sqlUpdate=sqlUpdate)

if __name__ == '__main__':
    app.run(debug=True)
