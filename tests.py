import json

from transactions import create_random_payment_transaction, payment_transaction_request


def test_payment_transaction_request_correct():
    # send a valid payment transaction request and expect an approved response
    transaction = create_random_payment_transaction()
    response, http_status = payment_transaction_request(transaction.toJSON())
    data = json.loads(response)
    assert data["status"] == "approved" and http_status == "200"
    return data


test_payment_transaction_request_correct()
