import json

from transactions import create_random_payment_transaction, payment_transaction_request, create_random_void_transaction


def test_payment_transaction_request_correct():
    # send a valid payment transaction request and expect an approved response
    transaction = create_random_payment_transaction()
    response, http_status = payment_transaction_request(transaction.toJSON())
    data = json.loads(response)
    assert data["status"] == "approved" and http_status == '200'
    return data


def test_void_transaction_request_correct():
    # send a valid void transaction request and expect an approved response
    data = test_payment_transaction_request_correct()

    transaction_void = create_random_void_transaction()
    transaction_void.reference_id = data['unique_id']

    void_response, void_http_status = payment_transaction_request(transaction_void.toJSON())
    void_data = json.loads(void_response)

    assert void_data['status'] == "approved" and void_http_status == "200"


def test_invalid_authentication():
    # send a valid payment transaction with an invalid authentication and expect an appropriate response (401 etc)
    data = test_payment_transaction_request_correct()

    transaction_void = create_random_void_transaction()
    transaction_void.reference_id = data['unique_id']

    void_response, void_http_status = payment_transaction_request(transaction_void.toJSON(),
                                                                  "aGFuZGFoYXB2YTprYWNoYW1haw==")
    assert void_http_status == "401"


def test_void_transaction_non_existent_payment():
    # send a void transaction pointing to a non-existent payment transaction
    # and expect 422 etc

    test_payment_transaction_request_correct()

    transaction_void = create_random_void_transaction()
    transaction_void.reference_id = "dasd21312"
    void_response, void_http_status = payment_transaction_request(transaction_void.toJSON())
    assert void_http_status == "422"
