import csv

# ...

# Function to load transaction records from a CSV file.
def load_transactions_from_csv(file_path):
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transaction_id = int(row['transaction_id'])
                customer_id = int(row['customer_id'])
                # Check if the customer exists in the memory before adding the transaction.
                if any(cust['customer_id'] == customer_id for cust in customers):
                    # Generate a new transaction ID to avoid clashes.
                    new_transaction_id = len(transactions) + 1
                    transactions.append({
                        'transaction_id': new_transaction_id,
                        'customer_id': customer_id,
                        'date': row['date'],
                        'category': row['category'],
                        'value': float(row['value'])
                    })
    except FileNotFoundError:
        print("File not found. No transaction records were loaded.")
    except Exception as e:
        print(f"Error loading transaction records: {e}")

# Function to save transaction records to a CSV file.
def save_transactions_to_csv(file_path):
    try:
        with open(file_path, 'w', newline='') as file:
            fieldnames = ['transaction_id', 'customer_id', 'date', 'category', 'value']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transactions)
    except Exception as e:
        print(f"Error saving transaction records: {e}")

# ...
