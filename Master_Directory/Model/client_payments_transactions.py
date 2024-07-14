from datetime import datetime
from typing import List


class ClientPaymentTransactions:
    def __init___(self) -> None:
        pass


class TransactionsSummary(ClientPaymentTransactions):
    def __init___(self) -> None:
        super().__init__()

        self.total_clients: int = 0
        self.total_payments: int = 0
        self.oldest_payment: datetime = ""
        self.newest_payment: datetime = ""
        self.sum_all_payments: str = ""
        self.average_payment: str = ""
        self.payment_min: str = ""
        self.payment_quartile_1: str = ""
        self.payment_median: str = ""
        self.payment_quartile_3: str = ""
        self.payment_max: str = ""
        self.total_amt_paid_in_june_and_july: str = ""
        self.total_private_companies: int = 0
        self.total_num_payments_under_1_dollar: int = 0
        self.average_sole_trader_payment_in_2017: str = ""

    @property
    def total_clients_(self):
        return self.total_clients

    @total_clients_.setter
    def total_clients_(self, total_clients: int = 0):
        self.total_clients = total_clients

    @property
    def total_payments_(self):
        return self.total_payments

    @total_payments_.setter
    def total_payments_(self, total_payments: int = 0):
        self.total_payments = total_payments

    @property
    def oldest_payment_(self):
        return self.oldest_payment

    @oldest_payment_.setter
    def oldest_payment_(self, oldest_payment: datetime = ""):
        self.oldest_payment = oldest_payment

    @property
    def newest_payment_(self):
        return self.newest_payment

    @newest_payment_.setter
    def newest_payment_(self, newest_payment: datetime = ""):
        self.newest_payment = newest_payment

    @property
    def sum_all_payments_(self):
        return self.sum_all_payments

    @sum_all_payments_.setter
    def sum_all_payments_(self, sum_all_payments: str = ""):
        self.sum_all_payments = sum_all_payments

    @property
    def average_payment_(self):
        return self.average_payment

    @average_payment_.setter
    def average_payment_(self, average_payment: str = ""):
        self.average_payment = average_payment

    @property
    def payment_min_(self):
        return self.payment_min

    @payment_min_.setter
    def payment_min_(self, payment_min: str = ""):
        self.payment_min = payment_min

    @property
    def payment_quartile_1_(self):
        return self.payment_quartile_1

    @payment_quartile_1_.setter
    def payment_quartile_1_(self, payment_quartile_1: str = ""):
        self.payment_quartile_1 = payment_quartile_1

    @property
    def payment_median_(self):
        return self.payment_median

    @payment_median_.setter
    def payment_median_(self, payment_median: str = ""):
        self.payment_median = payment_median

    @property
    def payment_quartile_3_(self):
        return self.payment_quartile_3

    @payment_quartile_3_.setter
    def payment_quartile_3_(self, payment_quartile_3: str = ""):
        self.payment_quartile_3 = payment_quartile_3

    @property
    def payment_max_(self):
        return self.payment_max

    @payment_max_.setter
    def payment_max_(self, payment_max: str = ""):
        self.payment_max = payment_max

    @property
    def total_amt_paid_in_june_and_july_(self):
        return self.total_amt_paid_in_june_and_july

    @total_amt_paid_in_june_and_july_.setter
    def total_amt_paid_in_june_and_july_(
        self, total_amt_paid_in_june_and_july: str = ""
    ):
        self.total_amt_paid_in_june_and_july = total_amt_paid_in_june_and_july

    @property
    def total_private_companies_(self):
        return self.total_private_companies

    @total_private_companies_.setter
    def total_private_companies_(self, total_private_companies: int = 0):
        self.total_private_companies = total_private_companies

    @property
    def total_num_payments_under_1_dollar_(self):
        return self.total_num_payments_under_1_dollar

    @total_num_payments_under_1_dollar_.setter
    def total_num_payments_under_1_dollar_(
        self, total_num_payments_under_1_dollar: int = 0
    ):
        self.total_num_payments_under_1_dollar = total_num_payments_under_1_dollar

    @property
    def average_sole_trader_payment_in_2017_(self):
        return self.average_sole_trader_payment_in_2017

    @average_sole_trader_payment_in_2017_.setter
    def average_sole_trader_payment_in_2017_(
        self, average_sole_trader_payment_in_2017: str = ""
    ):
        self.average_sole_trader_payment_in_2017 = average_sole_trader_payment_in_2017


class ClientRecords(ClientPaymentTransactions):
    def __init___(self) -> None:
        super().__init__()

        self.client_id: int = 0
        self.entity_type: str = ""
        self.entity_year_established: int = 0
        self.total_payments: int = 0
        self.total_amt_paid: str = ""

        self.payments: List = []

    @property
    def client_id_(self):
        return self.client_id

    @client_id_.setter
    def client_id_(self, client_id: int = 0):
        self.client_id = client_id

    @property
    def entity_type_(self):
        return self.entity_type

    @entity_type_.setter
    def entity_type_(self, entity_type: str = ""):
        self.entity_type = entity_type

    @property
    def entity_year_established_(self):
        return self.entity_year_established

    @entity_year_established_.setter
    def entity_year_established_(self, entity_year_established: int = 0):
        self.entity_year_established = entity_year_established

    @property
    def total_payments_(self):
        return self.total_payments

    @total_payments_.setter
    def total_payments_(self, total_payments: int = 0):
        self.total_payments = total_payments

    @property
    def total_amt_paid_(self):
        return self.total_amt_paid

    @total_amt_paid_.setter
    def total_amt_paid_(self, total_amt_paid: str = ""):
        self.total_amt_paid = total_amt_paid


class ClientPaymentDetails(ClientRecords):
    def __init___(self) -> None:

        self.client_id: int = 0
        self.transaction_id: int = 0
        self.contract_id: int = 0
        self.transaction_date: datetime = ""
        self.payment_amt: str = ""

    @property
    def client_id_(self):
        return self.client_id

    @client_id_.setter
    def client_id_(self, client_id: int = 0):
        self.client_id = client_id

    @property
    def transaction_id_(self):
        return self.transaction_id

    @transaction_id_.setter
    def transaction_id_(self, transaction_id: int = 0):
        self.transaction_id = transaction_id

    @property
    def contract_id_(self):
        return self.contract_id

    @contract_id_.setter
    def contract_id_(self, contract_id: int = 0):
        self.contract_id = contract_id

    @property
    def transaction_date_(self):
        return self.transaction_date

    @transaction_date_.setter
    def transaction_date_(self, transaction_date: datetime = ""):
        self.transaction_date = transaction_date

    @property
    def payment_amt_(self):
        return self.payment_amt

    @payment_amt_.setter
    def payment_amt_(self, payment_amt: str = ""):
        self.payment_amt = payment_amt

    @property
    def payment_code_(self):
        return self.payment_code

    @payment_code_.setter
    def payment_code_(self, payment_code: str = ""):
        self.payment_code = payment_code
