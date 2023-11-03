from customer import *
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
    print("8. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        customer_name = input("Enter customer's name: ")
        customer_postcode = input("Enter customer's postcode (optional): ")
        customer_phone = input("Enter customer's phone number (optional): ")
        customer_id = add_customer(customer_name, customer_postcode, customer_phone)
        print(f"Customer added with ID: {customer_id}")

    elif choice == "2":
        customer_id = int(input("Enter customer ID: "))
        date = input("Enter transaction date: ")
        category = input("Enter transaction category: ")
        value = float(input("Enter transaction value: "))
        transaction_id = add_transaction(customer_id, date, category, value)
        print(f"Transaction added with ID: {transaction_id}")

    elif choice == "3":
        search_string = input("Enter search string: ")
        matching_customers = search_customers(search_string)
        for customer in matching_customers:
            print(customer)

    elif choice == "4":
        search_string = input("Enter search string: ")
        matching_transactions = search_transactions(search_string)
        for transaction in matching_transactions:
            print(transaction)

    elif choice == "5":
        customer_id = int(input("Enter customer ID: "))
        # Implement a function to display sales transactions for the given customer.

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
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
