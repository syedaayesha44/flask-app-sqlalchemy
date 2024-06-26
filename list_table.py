from sqlalchemy import create_engine, inspect

# Replace 'sqlite:///ecommerce.db' with your database URI
engine = create_engine('sqlite:///ecommerce.db')

# Create an inspector object
inspector = inspect(engine)

# Get the list of table names
tables = inspector.get_table_names()

print("Tables in the database:")
for table in tables:
    print(table)
