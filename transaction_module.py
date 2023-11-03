# transaction_module.py

# Initialize an empty list to store sales transaction records.
transactions = []

# Function to add a new sales transaction for a given customer.
def add_transaction(customer_id, date, category, value):
    # Generate a unique transaction ID based on the number of existing transactions.
    transaction_id = len(transactions) + 1

    # Create a transaction dictionary and add it to the list of transactions.
    transaction = {
        'transaction_id': transaction_id,
        'customer_id': customer_id,
        'date': date,
        'category': category,
        'value': value
    }
    transactions.append(transaction)

    return transaction_id  # Return the auto-generated transaction ID.

# Function to search for sales transactions using a search string.
def search_transactions(search_string):
    matching_transactions = []
    search_string = search_string.lower()  # Convert to lowercase for case-insensitive search.

    for transaction in transactions:
        # Check if the search string is found in any transaction details.
        if search_string in str(transaction['transaction_id']).lower() \
            or search_string in str(transaction['customer_id']).lower() \
            or search_string in transaction['date'].lower() \
            or search_string in transaction['category'].lower() \
            or search_string in str(transaction['value']).lower():
            matching_transactions.append(transaction)

    return matching_transactions

# Function to delete a transaction record with a given transaction ID.
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['transaction_id'] == transaction_id:
            transactions.remove(transaction)
            return True  # Transaction deleted successfully.
    return False  # Transaction not found.

# Other transaction-related functions can be added as needed.

