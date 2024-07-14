import sqlite3
from typing import List


def initiate_extraction(configured_database_path: str):
    connection = sqlite3.connect(configured_database_path)

    cursor = connection.execute("SELECT * FROM clients;")
    clients: List = []
    for row in cursor:
        if len(row) > 0:
            clients.append(row)

    cursor = connection.execute("SELECT * FROM payments;")
    payments: List = []
    for row in cursor:
        if len(row) > 0:
            payments.append(row)

    connection.close()

    return clients, payments
