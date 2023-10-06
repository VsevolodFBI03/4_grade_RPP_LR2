from flask import Flask, request, jsonify

app = Flask(__name__)

# Создадим словарь для хранения данных
data_dict = {'reg_id': [],
             'tax_rate': []}


@app.route('/v1/add/tax', methods=['POST'])
def add_tax():
    data = request.get_json()
    reg_id = data.get('reg_id')
    tax_rate = data.get('tax_rate')
    if data_dict['reg_id'] == reg_id:
        return jsonify({'ERROR': 'Reg_id существует!'}), 400
    else:
        data_dict['reg_id'] = reg_id
        data_dict['tax_rate'] = tax_rate
        print(data_dict)
        return jsonify({'message': 'Данные добавлены успешно!'})


@app.route('/v1/fetch/taxes', methods=['GET'])
def fetch_taxes():
    return jsonify(data_dict)


@app.route('/v1/fetch/tax', methods=['GET'])
def fetch_tax():
    data_1 = request.get_json()
    reg_id = data_1.get('reg_id')
    if data_dict['reg_id'] == reg_id:
        return data_dict
    else:
        return ({'ERROR': 'Такого reg_id нет в словаре'}), 400


@app.route('/v1/fetch/calc', methods=['GET'])
def fetch_calc():
    data_2 = request.get_json()
    reg_id = data_2.get('reg_id')
    price = data_2.get('price')
    mounth = data_2.get('mounth')
    if data_dict['reg_id'] != reg_id:
        return jsonify({'ERROR': 'Такого reg_id нет в словаре'}), 400
    else:
        tax = data_dict['tax_rate'] * price * mounth / 12
        return jsonify({'Налог за год': tax})


@app.route('/v1/update/tax', methods=['POST'])
def update_tax():
    data_3 = request.get_json()
    reg_id = data_3.get('reg_id')
    tax_rate = data_3.get('tax_rate')
    if data_dict['reg_id'] == reg_id:
        data_dict['tax_rate'] = tax_rate
    else:
        return jsonify({'ERROR': 'Такого reg_id нет в словаре'}), 400
    print(data_dict)
    return jsonify({'SUCCESS': 'Данные обновлены!'}), 200


if __name__ == '__main__':
    app.run()
