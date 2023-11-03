from customer_module import *
from transaction_module import *

while True:
    print("\nMenu Options:")
    print("1. Add a new customer")
    print("2. Add a new transaction for a customer")
    print("3. Search for customers")
    print("4. Search for sales transactions")
    print("5. Display sales transactions for a customer")
    print("6. Delete a transaction record")
    print("7. Delete a customer and related transactions")
    print("8. Load customer records from a CSV file")
    print("9. Save customer records to a CSV file")
    print("10. Load transaction records from a CSV file")
    print("11. Save transaction records to a CSV file")
    print("12. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Existing code for adding a new customer.
        pass

    # ... Existing code for other menu options ...

    elif choice == "5":
        customer_id = int(input("Enter customer ID: "))
        # Implement a function to display sales transactions for the given customer.
        pass

    elif choice == "6":
        transaction_id = int(input("Enter transaction ID to delete: "))
        if delete_transaction(transaction_id):
            print("Transaction deleted successfully.")
        else:
            print("Transaction not found.")

    elif choice == "7":
        customer_id = int(input("Enter customer ID to delete: "))
        if delete_customer(customer_id):
            print("Customer and related transactions deleted successfully.")
        else:
            print("Customer not found.")

    elif choice == "8":
        file_path = input("Enter the file path to load customer records from: ")
        load_customers_from_csv(file_path)

    elif choice == "9":
        file_path = input("Enter the file path to save customer records to: ")
        save_customers_to_csv(file_path)

    elif choice == "10":
        file_path = input("Enter the file path to load transaction records from: ")
        load_transactions_from_csv(file_path)

    elif choice == "11":
        file_path = input("Enter the file path to save transaction records to: ")
        save_transactions_to_csv(file_path)

    elif choice == "12":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
