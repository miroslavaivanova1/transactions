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


def create_request(transaction_json):
    command = 'curl http://localhost:3001/payment_transactions' \
              ' -H  "Content-Type: application/json;charset=UTF-8"' \
              ' -H "Authorization: Basic cGFuZGFoYXB2YTprYWNoYW1haw=="'\
              ' -d \'{' + \
              '"payment_transaction": ' + transaction_json + \
              '}\' '
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out


tr = create_random_payment_transaction()
create_request(tr.toJSON())
