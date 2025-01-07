import csv
import os

def csv_editor():
    def display_menu():
        print("\n=== CSV Editor ===")
        print("1. Create a New CSV File")
        print("2. View an Existing CSV File")
        print("3. Add Rows to an Existing CSV File")
        print("4. Modify Data in an Existing CSV File")
        print("5. Exit")

    def create_csv():
        file_name = input("Enter the name of the new CSV file (e.g., data.csv): ")
        headers = input("Enter column headers (comma-separated): ").split(",")
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
        print(f"{file_name} created successfully.")

    def view_csv():
        file_name = input("Enter the name of the CSV file to view: ")
        if not os.path.exists(file_name):
            print("File not found.")
            return
        with open(file_name, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(", ".join(row))

    def add_rows():
        file_name = input("Enter the name of the CSV file to add rows to: ")
        if not os.path.exists(file_name):
            print("File not found.")
            return
        rows = []
        while True:
            row = input("Enter row data (comma-separated, type 'done' to stop): ")
            if row.lower() == "done":
                break
            rows.append(row.split(","))
        with open(file_name, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Rows added successfully.")

    def modify_csv():
        file_name = input("Enter the name of the CSV file to modify: ")
        if not os.path.exists(file_name):
            print("File not found.")
            return
        with open(file_name, mode="r") as file:
            rows = list(csv.reader(file))

        print("Current Data:")
        for i, row in enumerate(rows):
            print(f"{i}: {', '.join(row)}")

        row_index = int(input("Enter the row number to modify: "))
        col_index = int(input("Enter the column number to modify: "))
        new_value = input("Enter the new value: ")

        if 0 <= row_index < len(rows) and 0 <= col_index < len(rows[row_index]):
            rows[row_index][col_index] = new_value
            with open(file_name, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Data modified successfully.")
        else:
            print("Invalid row or column index.")

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            create_csv()
        elif choice == '2':
            view_csv()
        elif choice == '3':
            add_rows()
        elif choice == '4':
            modify_csv()
        elif choice == '5':
            print("Exiting CSV Editor.")
            break
        else:
            print("Invalid choice. Please try again!")