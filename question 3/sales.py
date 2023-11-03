import numpy as np
import matplotlib.pyplot as plt

# Initialize customer and transaction records as NumPy ndarrays
customer_records = np.empty((0, 4), dtype=object)  # Columns: customer_id, name, postcode, phone
transaction_records = np.empty((0, 5), dtype=object)  # Columns: transaction_id, customer_id, date, category, value

# Function to add a new customer
def add_customer(name, postcode='', phone=''):
    global customer_records
    customer_id = len(customer_records) + 1
    new_customer = np.array([[customer_id, name, postcode, phone]], dtype=object)
    customer_records = np.vstack([customer_records, new_customer])
    return customer_id

# Function to add a new transaction
def add_transaction(customer_id, date, category, value):
    global transaction_records
    transaction_id = len(transaction_records) + 1
    new_transaction = np.array([[transaction_id, customer_id, date, category, value]], dtype=object)
    transaction_records = np.vstack([transaction_records, new_transaction])
    return transaction_id

# Function to display the monthly sales values and transaction numbers with a line graph
def display_monthly_sales():
    # Extract transaction dates and values
    dates = transaction_records[:, 2]
    values = transaction_records[:, 4].astype(float)

    # Convert dates to a suitable format (e.g., 'YYYY-MM')
    monthly_dates = np.array([d[:7] for d in dates])

    # Group and sum values by month
    unique_months, total_values = np.unique(monthly_dates, return_counts=True)
    total_sales = np.zeros(len(unique_months))
    for i, month in enumerate(unique_months):
        total_sales[i] = np.sum(values[monthly_dates == month])

    # Create a line graph
    plt.figure(figsize=(10, 6))
    plt.plot(unique_months, total_sales, label='Total Sales')
    plt.plot(unique_months, total_values, label='Total Transactions')
    plt.xlabel('Month')
    plt.ylabel('Value / Transactions')
    plt.title('Monthly Sales and Transaction Numbers')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

# Function to display the monthly sales values and transaction numbers for a given customer
def display_customer_monthly_sales(customer_id):
    # Filter transactions for the given customer
    customer_transactions = transaction_records[transaction_records[:, 1] == str(customer_id)]

    # Extract transaction dates and values
    dates = customer_transactions[:, 2]
    values = customer_transactions[:, 4].astype(float)

    # Convert dates to a suitable format (e.g., 'YYYY-MM')
    monthly_dates = np.array([d[:7] for d in dates])

    # Group and sum values by month
    unique_months, total_values = np.unique(monthly_dates, return_counts=True)
    total_sales = np.zeros(len(unique_months))
    for i, month in enumerate(unique_months):
        total_sales[i] = np.sum(values[monthly_dates == month])

    # Create a line graph
    plt.figure(figsize=(10, 6))
    plt.plot(unique_months, total_sales, label='Total Sales')
    plt.plot(unique_months, total_values, label='Total Transactions')
    plt.xlabel('Month')
    plt.ylabel('Value / Transactions')
    plt.title(f'Monthly Sales and Transaction Numbers for Customer {customer_id}')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

# Function to display the monthly sales values and transaction numbers for a given postcode
def display_postcode_monthly_sales(postcode):
    # Filter customers with the given postcode
    matching_customers = customer_records[customer_records[:, 2] == postcode]

    if len(matching_customers) == 0:
        print("No customers found in the specified postcode.")
        return

    # Extract customer IDs
    customer_ids = matching_customers[:, 0]

    # Filter transactions for customers in the specified postcode
    postcode_transactions = transaction_records[np.isin(transaction_records[:, 1].astype(int), customer_ids)]

    # Extract transaction dates and values
    dates = postcode_transactions[:, 2]
    values = postcode_transactions[:, 4].astype(float)

    # Convert dates to a suitable format (e.g., 'YYYY-MM')
    monthly_dates = np.array([d[:7] for d in dates])

    # Group and sum values by month
    unique_months, total_values = np.unique(monthly_dates, return_counts=True)
    total_sales = np.zeros(len(unique_months))
    for i, month in enumerate(unique_months):
        total_sales[i] = np.sum(values[monthly_dates == month])

    # Create a line graph
    plt.figure(figsize=(10, 6))
    plt.plot(unique_months, total_sales, label='Total Sales')
    plt.plot(unique_months, total_values, label='Total Transactions')
    plt.xlabel('Month')
    plt.ylabel('Value / Transactions')
    plt.title(f'Monthly Sales and Transaction Numbers for Postcode {postcode}')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

# Sample usage of the functions
add_customer("John Doe", "12345", "555-123-4567")
add_customer("Jane Smith", "54321", "555-987-6543")
add_customer("Bob Johnson", "67890", "555-456-7890")
add_transaction(1, "2023-10-01", "Food", 50.00)
add_transaction(2, "2023-10-02", "Apparel", 75.00)
add_transaction(3, "2023-10-03", "Electronics", 120.00)

display_monthly_sales()
display_customer_monthly_sales(2)
display_postcode_monthly_sales("12345")
