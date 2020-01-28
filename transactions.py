import json
import subprocess


class SaleTransaction:

    def __init__(self, card_number, cvv, expiration_date, amount, usage, transaction_type, card_holder, email, address):
        self.card_number = card_number
        self.cvv = cvv
        self.expiration_date = expiration_date
        self.amount = amount
        self.usage = usage
        self.transaction_type = transaction_type
        self.card_holder = card_holder
        self.email = email
        self.address = address

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class VoidTransaction:

    def __init__(self, reference_id, transaction_type):
        self.reference_id = reference_id
        self.transaction_type = transaction_type

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def get_config():
    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
    return data


def get_card_number():
    return "4200000000000000"


def get_cvv():
    return '123'


def get_expiration_date():
    return '06/2019'


def get_amount():
    return '500'


def get_usage():
    return 'Coffeemaker'


def get_transaction_type():
    return 'sale'


def get_card_holder():
    return 'Panda Panda'


def get_email():
    return 'panda@example.com'


def get_address():
    return 'Panda Street, China'


def get_authorization():
    config = get_config()
    return config['auth_key']


def get_reference_id():
    return None


def get_void_transaction_type():
    return "void"


def create_random_void_transaction():
    transaction_type = get_void_transaction_type()
    tr = VoidTransaction(None, transaction_type)
    return tr


def create_random_payment_transaction():
    card_number = get_card_number()
    cvv = get_cvv()
    expiration_date = get_expiration_date()
    amount = get_amount()
    usage = get_usage()
    transaction_type = get_transaction_type()
    card_holder = get_card_holder()
    email = get_email()
    address = get_address()
    tr = SaleTransaction(card_number, cvv, expiration_date, amount, usage, transaction_type, card_holder,
                         email, address)
    return tr


def payment_transaction_request(transaction_json, auth_key=get_authorization()):
    return create_request(transaction_json, auth_key, "payment_transactions")


def create_request(transaction_json, auth_key, end_point):
    command = 'curl -s -w \'ResponseCode:%{response_code}\' http://localhost:3001/' + end_point + \
              ' -H  "Content-Type: application/json;charset=UTF-8"' \
              ' -H "Authorization: Basic ' + auth_key + '"'\
              ' -d \'{' + \
              '"payment_transaction": ' + transaction_json + \
              '}\' '
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    r = out.split(b"ResponseCode:")
    return r[0], r[1].decode()
