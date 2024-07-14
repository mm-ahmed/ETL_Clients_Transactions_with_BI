import glob, os
from typing import Dict, List
from ETL import extract, transformation, load

DATABASE_FILE_NAME = "edgered.db"


def initiate_extraction_process(configured_database_path: str = ""):
    print("\nExtraction process started... Please wait!")
    return extract.initiate_extraction(configured_database_path)


def initiate_transformation_process(clients: List = [], payments: List = []):
    print("\nTransformation process started... Please wait!")

    clients_df = transformation.get_clients(clients)

    payments_df = transformation.get_payments(payments)

    dataset_df = transformation.merge_dataframes(clients_df, payments_df)

    return (
        transformation.transform_payments(dataset_df),
        transformation.transform_clients(clients_df, payments_df),
        transformation.generate_summary(dataset_df).__dict__,
    )


def initiate_loading_process(
    payment_details_list: List = [],
    client_records_list: List = [],
    clients_transaction_summary: Dict = {},
    input_resultset_output_path: str = "",
):
    print("\nLoading process started... Please wait!")
    return load.load_resultset(
        payment_details_list,
        client_records_list,
        clients_transaction_summary,
        input_resultset_output_path,
    )


def main():
    if __name__ == "__main__":

        input_database_path = input(
            "Configure database file path (or press 1 to re-enter): "
        )
        configured_database_path = glob.glob(input_database_path)
        input_resultset_output_path = input("Configure output resultset path: ")
        if not os.path.exists(input_resultset_output_path):
            input_resultset_output_path = "Output"
            print(
                "\nIt seems the resultset path is invalid or doesn't exist, hence, the resultset file 'output.json' will be stored at path: 'Output\output.json'"
            )

        if len(configured_database_path) > 0:
            if DATABASE_FILE_NAME in configured_database_path[0]:

                clients, payments = initiate_extraction_process(
                    configured_database_path[0]
                )

                (
                    payment_details_list,
                    client_records_list,
                    clients_transaction_summary,
                ) = initiate_transformation_process(clients, payments)

                load_status = initiate_loading_process(
                    payment_details_list,
                    client_records_list,
                    clients_transaction_summary,
                    input_resultset_output_path,
                )
                if load_status:
                    print(
                        "\nETL pipeline completed successfully. See the results in the 'output.json' file.\n"
                    )
                else:
                    print("\nETL piepline failed. Please investigate and retun.\n")

        elif input_database_path == "1":
            main()

        else:
            print("\nInvalid database configuration path. Now exiting.\n")
            exit()


main()
