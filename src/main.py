from db_utils import create_database, create_table, insert_data_from_csv, drop_database

def main():
    # Drop the database if it exists (for debugging purposes)
    drop_database()
    
    # Create the database and table
    create_database()
    create_table()
    
    # Insert data from CSV file
    csv_file_path = 'c:\\Users\\spac-23\\Documents\\SpecialisterneProjektMappe\\Uge Opgaver\\uge4\\Uge-4\\Data\\orders_combined.csv'
    insert_data_from_csv(csv_file_path)
    
    print("Data inserted successfully.")

if __name__ == "__main__":
    main()
