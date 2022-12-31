from utils.read import read_file
from src.process.process import get_summary
from database import repository


# Read transactions file
file_name = 'C:\\Projects\\Python\\process-transactions\\file\\txn.csv'
data = read_file(file_name)

# Insert data on database
repository.insert(data)

# Generate summary and send it
get_summary(data)
