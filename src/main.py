from db_utils import create_database, create_table, insert_data_from_csv, drop_database

def main():

    drop_database()
    create_database()
    create_table()

    csv_file_path = "c:\\Users\\spac-23\\Documents\\SpecialisterneProjektMappe\\Uge Opgaver\\uge4\\Uge-4\\Data\\orders_combined.csv"
    insert_data_from_csv(csv_file_path)

    print("Data inserted successfully")

if __name__ == "__main__":
    main()