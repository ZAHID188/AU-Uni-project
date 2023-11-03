import csv

# ...

# Function to load customer records from a CSV file.
def load_customers_from_csv(file_path):
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                customer_id = int(row['customer_id'])
                # Check for duplicate customer IDs and ignore them.
                if not any(cust['customer_id'] == customer_id for cust in customers):
                    customers.append({
                        'customer_id': customer_id,
                        'customer_name': row['customer_name'],
                        'customer_postcode': row['customer_postcode'],
                        'customer_phone': row['customer_phone']
                    })
    except FileNotFoundError:
        print("File not found. No customer records were loaded.")
    except Exception as e:
        print(f"Error loading customer records: {e}")

# Function to save customer records to a CSV file.
def save_customers_to_csv(file_path):
    try:
        with open(file_path, 'w', newline='') as file:
            fieldnames = ['customer_id', 'customer_name', 'customer_postcode', 'customer_phone']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(customers)
    except Exception as e:
        print(f"Error saving customer records: {e}")

# ...
