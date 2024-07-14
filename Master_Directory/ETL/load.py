import json, copy
from typing import List, Dict
from Model.client_payments_transactions import ClientRecords


def load_resultset(
    payment_details_list: List,
    client_records_list: List,
    clients_transaction_summary: Dict,
    input_resultset_output_path: str,
) -> bool:

    records: List = []

    for client_record in client_records_list:
        temp_payment: List = []
        client_obj = ClientRecords()
        for payment_record in payment_details_list:

            if payment_record.__dict__.get("client_id") == client_record.__dict__.get(
                "client_id"
            ):

                payment_record_deep_copy = copy.deepcopy(payment_record.__dict__)
                payment_record_deep_copy.pop("client_id")
                temp_payment.append(payment_record_deep_copy)

        if len(temp_payment) > 0:
            client_obj.client_id = client_record.client_id
            client_obj.entity_type = client_record.entity_type
            client_obj.entity_year_established = client_record.entity_year_established
            client_obj.total_payments = client_record.total_payments
            client_obj.total_amt_paid = client_record.total_amt_paid
            client_obj.payments = temp_payment

            records.append(client_obj)

    if clients_transaction_summary is not None and len(records) > 0:
        with open(f"{input_resultset_output_path}/output.json", "w") as outfile:
            json.dump(
                {
                    "summary": clients_transaction_summary,
                    "records": [item.__dict__ for item in records],
                },
                outfile,
                indent=4,
            )

        return True

    return False
