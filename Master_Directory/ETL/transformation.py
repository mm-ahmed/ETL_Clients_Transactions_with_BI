from typing import List
import pandas as pd
from datetime import datetime
from Model.client_payments_transactions import (
    ClientPaymentDetails,
    ClientRecords,
    TransactionsSummary,
)


def get_clients(clients: List = []) -> pd.DataFrame:

    clients_df = pd.DataFrame()

    for item in clients:
        if len(item) == 3:
            row = pd.DataFrame(
                {
                    "client_id": item[0],
                    "entity_type": item[1],
                    "entity_year_established": item[2],
                },
                index=[0],
            )

            clients_df = pd.concat([clients_df, row], ignore_index=True)

    return clients_df


def get_payments(payments: List = []) -> pd.DataFrame:

    payments_df = pd.DataFrame()

    for item in payments:
        if len(item) == 6:
            row = pd.DataFrame(
                {
                    "transaction_id": item[0],
                    "contract_id": item[1],
                    "client_id": item[2],
                    "transaction_date": datetime.fromtimestamp(item[3]).isoformat(),
                    "payment_amt": item[4],
                    "payment_code": item[5],
                },
                index=[0],
            )

            payments_df = pd.concat([payments_df, row], ignore_index=True)

    return payments_df


def merge_dataframes(clients_df: pd.DataFrame, payments_df: pd.DataFrame):

    dataset_df = clients_df.merge(
        payments_df, how="inner", left_on="client_id", right_on="client_id"
    )

    return dataset_df


def get_client_payment_total(payments_df: pd.DataFrame):
    return (
        payments_df[["client_id", "payment_amt"]]
        .groupby(["client_id"])
        .sum()
        .reset_index()
    )


def get_client_payment_count(payments_df: pd.DataFrame):
    return (
        payments_df[["client_id", "transaction_id"]]
        .groupby(["client_id"])
        .count()
        .reset_index()
    )


def transform_payments(dataset_df: pd.DataFrame) -> List[ClientPaymentDetails]:
    payment_details_list: List = []

    for index, row in dataset_df.iterrows():

        payment_details = ClientPaymentDetails()

        payment_details.client_id = row["client_id"]
        payment_details.transaction_id = row["transaction_id"]
        payment_details.contract_id = row["contract_id"]
        payment_details.transaction_date = row["transaction_date"]
        payment_details.payment_amt = "$" + str(
            format(round(row["payment_amt"] / 100.0, 2), ",")
        )
        payment_details.payment_code = row["payment_code"]

        payment_details_list.append(payment_details)

    return payment_details_list


def transform_clients(
    clients_df: pd.DataFrame, payments_df: pd.DataFrame
) -> List[ClientRecords]:

    client_records_list: List = []
    df_client_payment_total = get_client_payment_total(payments_df)
    df_client_payment_count = get_client_payment_count(payments_df)

    for index, row in clients_df.iterrows():

        client_records = ClientRecords()

        client_records.client_id = row["client_id"]
        client_records.entity_type = row["entity_type"]
        client_records.entity_year_established = row["entity_year_established"]

        total_transactions = df_client_payment_count[
            df_client_payment_count.client_id == row["client_id"]
        ]["transaction_id"].values
        client_records.total_payments = (
            int(total_transactions[0]) if total_transactions.size == 1 else 0
        )

        payment_amt = df_client_payment_total[
            df_client_payment_total.client_id == row["client_id"]
        ]["payment_amt"].values
        client_records.total_amt_paid = (
            "$" + str(format(round(payment_amt[0] / 100.0, 2), ","))
            if payment_amt.size == 1
            else 0
        )

        client_records_list.append(client_records)

    return client_records_list


def generate_summary(dataset_df: pd.DataFrame) -> TransactionsSummary:

    clients_transaction_summary = TransactionsSummary()

    clients_transaction_summary.total_clients_ = dataset_df.client_id.nunique()

    clients_transaction_summary.total_payments_ = dataset_df.transaction_id.nunique()

    clients_transaction_summary.oldest_payment_ = dataset_df.transaction_date.min()

    clients_transaction_summary.newest_payment_ = dataset_df.transaction_date.max()

    clients_transaction_summary.sum_all_payments_ = "$" + str(
        format(round(dataset_df.payment_amt.sum() / 100.0, 2), ",")
    )

    clients_transaction_summary.average_payment_ = "$" + str(
        format(round(dataset_df.payment_amt.mean() / 100.0, 2), ",")
    )

    clients_transaction_summary.payment_min_ = "$" + str(
        format(round(dataset_df.payment_amt.min() / 100.0, 2), ",")
    )

    clients_transaction_summary.payment_quartile_1_ = "$" + str(
        format(round(dataset_df.payment_amt.quantile(0.25) / 100.0, 2), ",")
    )

    clients_transaction_summary.payment_median_ = "$" + str(
        format(round(dataset_df.payment_amt.median() / 100.0, 2), ",")
    )

    clients_transaction_summary.payment_quartile_3_ = "$" + str(
        format(round(dataset_df.payment_amt.quantile(0.75) / 100.0, 2), ",")
    )

    clients_transaction_summary.payment_max_ = "$" + str(
        format(round(dataset_df.payment_amt.max() / 100.0, 2), ",")
    )

    clients_transaction_summary.total_amt_paid_in_june_and_july_ = "$" + str(
        format(
            (
                (
                    dataset_df.groupby(
                        pd.to_datetime(dataset_df["transaction_date"]).dt.month.apply(
                            lambda x: x in [6, 7]
                        )
                    )["payment_amt"].sum()
                    / 100.0
                )
                .to_dict()
                .get(True)
            ),
            ",",
        )
    )

    clients_transaction_summary.total_private_companies_ = dataset_df[
        (dataset_df.entity_type.str.contains("private", case=False))
    ]["client_id"].nunique()

    clients_transaction_summary.total_num_payments_under_1_dollar_ = dataset_df[
        dataset_df.payment_amt / 100.0 < 1.0
    ].index.size

    clients_transaction_summary.average_sole_trader_payment_in_2017_ = "$" + str(
        format(
            round(
                dataset_df[
                    (
                        (dataset_df.entity_type.str.contains("sole trader", case=False))
                        == True
                    )
                    & (dataset_df["entity_year_established"] == 2017)
                ].payment_amt.mean(),
                2,
            ),
            ",",
        )
    )

    return clients_transaction_summary
